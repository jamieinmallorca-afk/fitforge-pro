from pydantic import BaseModel, Field
from typing import List, Optional, Union
from enum import Enum

class FitnessLevel(str, Enum):
    beginner     = "beginner"
    intermediate = "intermediate"
    advanced     = "advanced"

class Environment(str, Enum):
    home_gym    = "home_gym"
    pro_gym     = "pro_gym"
    outdoor     = "outdoor"
    bodyweight  = "bodyweight"

class Goal(str, Enum):
    fat_loss     = "fat_loss"
    muscle_gain  = "muscle_gain"
    strength     = "strength"
    endurance    = "endurance"

class InjuryArea(str, Enum):
    none          = "none"
    lower_back    = "lower_back"
    knee          = "knee"
    shoulder      = "shoulder"
    wrist         = "wrist"
    ankle         = "ankle"
    neck          = "neck"
    hip           = "hip"
    elbow         = "elbow"

class UserProfile(BaseModel):
    age:          int       = Field(..., ge=16, le=80)
    weight_kg:    float     = Field(..., ge=30, le=300)
    height_cm:    float     = Field(..., ge=100, le=250)
    fitness_level: FitnessLevel
    injuries:     List[InjuryArea] = []
    environment:  Union[List[Environment], Environment]
    goal:         Union[List[Goal], Goal]
    days_per_week: int      = Field(..., ge=2, le=7)
    session_minutes: int    = Field(..., ge=20, le=120)

class Exercise(BaseModel):
    name:         str
    sets:         int
    reps:         str
    rest_seconds: int
    notes:        Optional[str] = None

class WorkoutDay(BaseModel):
    day_number:   int
    day_name:     str
    focus:        str
    exercises:    List[Exercise]
    total_volume: int

class WeekPlan(BaseModel):
    week_number:  int
    theme:        str
    intensity_pct: int
    days:         List[WorkoutDay]

class BMIInfo(BaseModel):
    value:    float
    category: str
    healthy_range: str

class TrainingPlan(BaseModel):
    user_name:    str = "Athlete"
    bmi:          BMIInfo
    goal:         str
    weeks:        List[WeekPlan]
    weekly_split: str
    tips:         List[str]
