from typing import List

def calculate_bmi(weight_kg: float, height_cm: float) -> float:
    height_m = height_cm / 100
    return round(weight_kg / (height_m ** 2), 1)

def get_bmi_category(bmi: float) -> str:
    if bmi < 18.5: return "Underweight"
    if bmi < 25.0: return "Normal weight"
    if bmi < 30.0: return "Overweight"
    return "Obese"

def filter_exercises(db: list, environments: List[str], injuries: List[str], goals: List[str]) -> list:
    result = []
    injury_set = set(i for i in injuries if i != "none")
    for ex in db:
        if not any(env in ex.get("environments", []) for env in environments):
            continue
        if injury_set & set(ex.get("avoid_injuries", [])):
            continue
        ex_goals = ex.get("goals", [])
        if any(g in ex_goals for g in goals):
            result.insert(0, ex)
        else:
            result.append(ex)
    return result
