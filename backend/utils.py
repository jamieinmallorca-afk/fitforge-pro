from typing import List
from models import CalorieInfo

def calculate_bmi(weight_kg: float, height_cm: float) -> float:
    height_m = height_cm / 100
    return round(weight_kg / (height_m ** 2), 1)

def get_bmi_category(bmi: float) -> str:
    if bmi < 18.5: return "Underweight"
    if bmi < 25.0: return "Normal weight"
    if bmi < 30.0: return "Overweight"
    return "Obese"

def calculate_calories(weight_kg: float, height_cm: float, age: int,
                       gender: str, goals: List[str], days_per_week: int) -> CalorieInfo:
    # Mifflin-St Jeor BMR — different formula for male and female
    if gender == "male":
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    else:
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161

    # Activity multiplier
    if days_per_week <= 2:   activity = 1.375
    elif days_per_week <= 4: activity = 1.55
    elif days_per_week <= 5: activity = 1.725
    else:                    activity = 1.9

    tdee = round(bmr * activity)

    if "fat_loss" in goals:
        target = round(tdee - 400)
    elif "muscle_gain" in goals:
        target = round(tdee + 300)
    else:
        target = tdee

    protein_g = round(weight_kg * 2.0)
    fat_g     = round(target * 0.25 / 9)
    carbs_g   = round((target - protein_g * 4 - fat_g * 9) / 4)

    return CalorieInfo(
        tdee=tdee,
        target=target,
        protein_g=protein_g,
        carbs_g=max(0, carbs_g),
        fat_g=fat_g
    )

def filter_exercises(db: list, environments: List[str], injuries: List[str],
                     goals: List[str], gender: str) -> list:
    result = []
    injury_set = set(i for i in injuries if i != "none")
    for ex in db:
        if not any(env in ex.get("environments", []) for env in environments):
            continue
        if injury_set & set(ex.get("avoid_injuries", [])):
            continue
        # Filter by gender preference
        ex_gender = ex.get("gender", "both")
        if ex_gender != "both" and ex_gender != gender:
            continue
        ex_goals = ex.get("goals", [])
        if any(g in ex_goals for g in goals):
            result.insert(0, ex)
        else:
            result.append(ex)
    return result
