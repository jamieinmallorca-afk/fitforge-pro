from models import UserProfile, TrainingPlan, WeekPlan, WorkoutDay, Exercise, BMIInfo
from exercise_database import EXERCISE_DB
from utils import calculate_bmi, get_bmi_category, filter_exercises
from typing import List

class TrainingEngine:

    VOLUME = {
        "beginner":     {"sets_per_muscle": 9,  "rep_range": "12-15", "rest": 90},
        "intermediate": {"sets_per_muscle": 15, "rep_range": "8-12",  "rest": 75},
        "advanced":     {"sets_per_muscle": 20, "rep_range": "5-8",   "rest": 60},
    }

    GOAL_OVERRIDES = {
        "fat_loss":    {"rep_range": "12-20", "rest": 45,  "sets_mod": -1},
        "muscle_gain": {"rep_range": "8-12",  "rest": 75,  "sets_mod": 0},
        "strength":    {"rep_range": "3-6",   "rest": 180, "sets_mod": +1},
        "endurance":   {"rep_range": "15-25", "rest": 30,  "sets_mod": -2},
    }

    WEEK_THEMES = [
        (1, "Foundation — learn movement patterns",    70),
        (2, "Build — increase working sets",           80),
        (3, "Overload — push intensity",               90),
        (4, "Deload — recover and consolidate",        60),
    ]

    def generate(self, profile: UserProfile) -> TrainingPlan:
        bmi_val  = calculate_bmi(profile.weight_kg, profile.height_cm)
        bmi_info = BMIInfo(
            value=bmi_val,
            category=get_bmi_category(bmi_val),
            healthy_range="18.5 - 24.9"
        )

        goal_ov  = self.GOAL_OVERRIDES[profile.goal]
        rep_range    = goal_ov["rep_range"]
        rest_secs    = goal_ov["rest"]
        sets_per_ex  = max(2, min(5, 3 + goal_ov["sets_mod"]))

        age_factor = 0.85 if profile.age >= 50 else 1.0
        bmi_factor = 0.9 if bmi_val > 30 else 1.0

        environments = profile.environment if isinstance(profile.environment, list) else [profile.environment]

        exercises = filter_exercises(
            EXERCISE_DB,
            environments=environments,
            injuries=profile.injuries,
            goal=profile.goal
        )

        split = self._get_split(profile.days_per_week)
        weeks = []

        for wk_num, theme, intensity in self.WEEK_THEMES:
            adjusted_sets = max(2, round(sets_per_ex * age_factor * bmi_factor * intensity / 100))
            days = self._build_week(
                split, exercises, adjusted_sets, rep_range,
                rest_secs, profile.session_minutes
            )
            weeks.append(WeekPlan(
                week_number=wk_num,
                theme=theme,
                intensity_pct=intensity,
                days=days
            ))

        return TrainingPlan(
            bmi=bmi_info,
            goal=profile.goal,
            weeks=weeks,
            weekly_split=split["name"],
            tips=self._tips(profile)
        )

    def _get_split(self, days: int) -> dict:
        splits = {
            2: {"name": "Full Body x2",
                "days": [{"focus":"Full Body","muscles":["chest","back","legs","shoulders","arms"]},
                         {"focus":"Full Body","muscles":["chest","back","legs","core"]}]},
            3: {"name": "Push / Pull / Legs",
                "days": [{"focus":"Push","muscles":["chest","shoulders","triceps"]},
                         {"focus":"Pull","muscles":["back","biceps","rear_delt"]},
                         {"focus":"Legs","muscles":["quads","hamstrings","glutes","calves"]}]},
            4: {"name": "Upper / Lower x2",
                "days": [{"focus":"Upper A","muscles":["chest","back","shoulders"]},
                         {"focus":"Lower A","muscles":["quads","hamstrings","glutes"]},
                         {"focus":"Upper B","muscles":["chest","back","arms"]},
                         {"focus":"Lower B","muscles":["hamstrings","glutes","calves","core"]}]},
            5: {"name": "PPL + Full Body",
                "days": [{"focus":"Push","muscles":["chest","shoulders","triceps"]},
                         {"focus":"Pull","muscles":["back","biceps"]},
                         {"focus":"Legs","muscles":["quads","hamstrings","glutes"]},
                         {"focus":"Full Body","muscles":["chest","back","legs","shoulders"]},
                         {"focus":"Core & Conditioning","muscles":["core","cardio"]}]},
            6: {"name": "Arnold Split",
                "days": [{"focus":"Chest & Back","muscles":["chest","back"]},
                         {"focus":"Shoulders & Arms","muscles":["shoulders","biceps","triceps"]},
                         {"focus":"Legs","muscles":["quads","hamstrings","glutes","calves"]},
                         {"focus":"Chest & Back","muscles":["chest","back"]},
                         {"focus":"Shoulders & Arms","muscles":["shoulders","biceps","triceps"]},
                         {"focus":"Legs","muscles":["quads","hamstrings","glutes","calves"]}]},
        }
        return splits.get(days, splits[3])

    def _build_week(self, split, exercises, sets, reps, rest, session_min) -> List[WorkoutDay]:
        days = []
        day_names = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        for i, day_info in enumerate(split["days"]):
            muscles = day_info["muscles"]
            pool = [e for e in exercises if any(m in e.get("muscles",[]) for m in muscles)]
            # Always show between 5 and 8 exercises per day
            min_ex = 5
            max_ex = max(min_ex, session_min // 10)
            # If pool is smaller than min, reuse from full exercise list
            if len(pool) < min_ex:
                extras = [e for e in exercises if e not in pool]
                pool = pool + extras[:min_ex - len(pool)]
            pool = pool[:max_ex]
            exs = [Exercise(name=e["name"], sets=sets,
                            reps=reps, rest_seconds=rest,
                            notes=e.get("notes","")) for e in pool]
            days.append(WorkoutDay(
                day_number   = i + 1,
                day_name     = day_names[i],
                focus        = day_info["focus"],
                exercises    = exs,
                total_volume = sets * len(exs)
            ))
        return days

    def _tips(self, p: UserProfile) -> List[str]:
        tips = ["Always warm up for 5-10 minutes before each session.",
                "Track your workouts in a journal or app to monitor progress.",
                "Sleep 7-9 hours per night — it is when you actually grow stronger."]
        if p.fitness_level == "beginner":
            tips.append("Focus on form over weight. Watch tutorial videos for new exercises.")
        if p.goal == "fat_loss":
            tips.append("Combine training with a 300-500 kcal daily deficit for best fat loss results.")
        if p.goal == "muscle_gain":
            tips.append("Eat 0.8-1g of protein per pound of bodyweight daily for muscle growth.")
        if p.age >= 50:
            tips.append("Include extra mobility work. Joint health is critical for long-term training.")
        return tips
