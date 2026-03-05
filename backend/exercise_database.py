# backend/exercise_database.py
# Each entry: name, muscles[], environments[], avoid_injuries[], goals[]
 
EXERCISE_DB = [
  # ── CHEST ─────────────────────────────────────────────────────────────
  {"name":"Barbell Bench Press","muscles":["chest","triceps","shoulders"],
   "environments":["pro_gym"],"avoid_injuries":["shoulder","wrist","elbow"],
   "goals":["muscle_gain","strength"]},
 
  {"name":"Dumbbell Bench Press","muscles":["chest","triceps","shoulders"],
   "environments":["pro_gym","home_gym"],"avoid_injuries":["shoulder","wrist"],
   "goals":["muscle_gain","fat_loss","strength"]},
 
  {"name":"Push-Up","muscles":["chest","triceps","core"],
   "environments":["pro_gym","home_gym","outdoor","bodyweight"],
   "avoid_injuries":["wrist"],"goals":["muscle_gain","fat_loss","endurance"]},
 
  {"name":"Incline Dumbbell Press","muscles":["chest","shoulders"],
   "environments":["pro_gym","home_gym"],"avoid_injuries":["shoulder","wrist"],
   "goals":["muscle_gain","strength"]},
 
  {"name":"Cable Fly","muscles":["chest"],"environments":["pro_gym"],
   "avoid_injuries":["shoulder"],"goals":["muscle_gain","fat_loss"]},
 
  {"name":"Dumbbell Fly","muscles":["chest"],"environments":["pro_gym","home_gym"],
   "avoid_injuries":["shoulder"],"goals":["muscle_gain"]},
 
  # ── BACK ──────────────────────────────────────────────────────────────
  {"name":"Barbell Deadlift","muscles":["back","glutes","hamstrings"],
   "environments":["pro_gym"],"avoid_injuries":["lower_back","knee"],
   "goals":["strength","muscle_gain"]},
 
  {"name":"Pull-Up","muscles":["back","biceps"],
   "environments":["pro_gym","home_gym","outdoor","bodyweight"],
   "avoid_injuries":["shoulder","elbow","wrist"],"goals":["muscle_gain","strength"]},
 
  {"name":"Dumbbell Row","muscles":["back","biceps"],
   "environments":["pro_gym","home_gym"],"avoid_injuries":["lower_back","wrist"],
   "goals":["muscle_gain","strength"]},
 
  {"name":"Lat Pulldown","muscles":["back","biceps"],
   "environments":["pro_gym"],"avoid_injuries":["shoulder","elbow"],
   "goals":["muscle_gain","fat_loss"]},
 
  {"name":"Seated Cable Row","muscles":["back","biceps","rear_delt"],
   "environments":["pro_gym"],"avoid_injuries":["lower_back","wrist"],
   "goals":["muscle_gain","strength"]},
 
  {"name":"Inverted Row","muscles":["back","biceps","rear_delt"],
   "environments":["pro_gym","home_gym","outdoor","bodyweight"],
   "avoid_injuries":["shoulder"],"goals":["muscle_gain","endurance"]},
 
  # ── LEGS ──────────────────────────────────────────────────────────────
  {"name":"Barbell Squat","muscles":["quads","glutes","hamstrings"],
   "environments":["pro_gym"],"avoid_injuries":["knee","lower_back","hip"],
   "goals":["strength","muscle_gain"]},
 
  {"name":"Goblet Squat","muscles":["quads","glutes","core"],
   "environments":["pro_gym","home_gym"],"avoid_injuries":["knee","lower_back"],
   "goals":["fat_loss","muscle_gain","endurance"]},
 
  {"name":"Bodyweight Squat","muscles":["quads","glutes"],
   "environments":["pro_gym","home_gym","outdoor","bodyweight"],
   "avoid_injuries":["knee"],"goals":["fat_loss","endurance","muscle_gain"]},
 
  {"name":"Romanian Deadlift","muscles":["hamstrings","glutes","lower_back"],
   "environments":["pro_gym","home_gym"],"avoid_injuries":["lower_back","knee"],
   "goals":["muscle_gain","strength"]},
 
  {"name":"Walking Lunge","muscles":["quads","glutes","hamstrings"],
   "environments":["pro_gym","outdoor","bodyweight"],
   "avoid_injuries":["knee","hip","ankle"],"goals":["fat_loss","muscle_gain"]},
 
  {"name":"Leg Press","muscles":["quads","glutes"],
   "environments":["pro_gym"],"avoid_injuries":["knee","lower_back"],
   "goals":["muscle_gain","strength"]},
 
  {"name":"Calf Raise","muscles":["calves"],
   "environments":["pro_gym","home_gym","outdoor","bodyweight"],
   "avoid_injuries":["ankle"],"goals":["muscle_gain","endurance"]},
 
  # ── SHOULDERS ─────────────────────────────────────────────────────────
  {"name":"Overhead Press","muscles":["shoulders","triceps"],
   "environments":["pro_gym","home_gym"],"avoid_injuries":["shoulder","wrist","neck"],
   "goals":["strength","muscle_gain"]},
 
  {"name":"Lateral Raise","muscles":["shoulders"],
   "environments":["pro_gym","home_gym"],"avoid_injuries":["shoulder"],
   "goals":["muscle_gain","fat_loss"]},
 
  {"name":"Face Pull","muscles":["rear_delt","shoulders"],
   "environments":["pro_gym"],"avoid_injuries":["shoulder","elbow"],
   "goals":["muscle_gain","fat_loss"]},
 
  {"name":"Pike Push-Up","muscles":["shoulders","triceps"],
   "environments":["pro_gym","home_gym","outdoor","bodyweight"],
   "avoid_injuries":["shoulder","wrist","neck"],"goals":["muscle_gain","endurance"]},
 
  # ── CORE ──────────────────────────────────────────────────────────────
  {"name":"Plank","muscles":["core"],"environments":["pro_gym","home_gym","outdoor","bodyweight"],
   "avoid_injuries":["wrist","shoulder"],"goals":["fat_loss","endurance","strength"]},
 
  {"name":"Dead Bug","muscles":["core"],"environments":["pro_gym","home_gym","bodyweight"],
   "avoid_injuries":[],"goals":["fat_loss","endurance"]},
 
  {"name":"Hanging Knee Raise","muscles":["core"],"environments":["pro_gym","outdoor"],
   "avoid_injuries":["shoulder","wrist","elbow"],"goals":["muscle_gain","fat_loss"]},
 
  {"name":"Ab Wheel Rollout","muscles":["core"],"environments":["pro_gym","home_gym"],
   "avoid_injuries":["lower_back","wrist","shoulder"],"goals":["strength","muscle_gain"]},
 
  # ── CARDIO / CONDITIONING ─────────────────────────────────────────────
  {"name":"Burpees","muscles":["cardio","core","chest"],"environments":["pro_gym","home_gym","outdoor","bodyweight"],
   "avoid_injuries":["knee","wrist","shoulder"],"goals":["fat_loss","endurance"]},
 
  {"name":"Box Jump","muscles":["cardio","quads","glutes"],"environments":["pro_gym","outdoor"],
   "avoid_injuries":["knee","ankle"],"goals":["fat_loss","endurance","strength"]},
 
  {"name":"Jump Rope","muscles":["cardio","calves"],"environments":["pro_gym","home_gym","outdoor"],
   "avoid_injuries":["ankle","knee"],"goals":["fat_loss","endurance"]},
 
  {"name":"Treadmill Sprint Intervals","muscles":["cardio","legs"],
   "environments":["pro_gym"],"avoid_injuries":["knee","ankle","hip"],
   "goals":["fat_loss","endurance"]},
]