EXERCISE_DB = [
  # ── CHEST ──────────────────────────────────────────────────────────────
  {"name":"Barbell Bench Press","muscles":["chest","triceps","shoulders"],
   "environments":["pro_gym"],"avoid_injuries":["shoulder","wrist","elbow"],
   "goals":["muscle_gain","strength"],"video_url":"https://www.youtube.com/watch?v=vcBig73ojpE"},

  {"name":"Dumbbell Bench Press","muscles":["chest","triceps","shoulders"],
   "environments":["pro_gym","home_gym"],"avoid_injuries":["shoulder","wrist"],
   "goals":["muscle_gain","fat_loss","strength"],"video_url":"https://www.youtube.com/watch?v=VmB1G1K7v94"},

  {"name":"Push-Up","muscles":["chest","triceps","core"],
   "environments":["pro_gym","home_gym","outdoor","bodyweight"],
   "avoid_injuries":["wrist"],"goals":["muscle_gain","fat_loss","endurance"],
   "video_url":"https://www.youtube.com/watch?v=IODxDxX7oi4"},

  {"name":"Incline Dumbbell Press","muscles":["chest","shoulders"],
   "environments":["pro_gym","home_gym"],"avoid_injuries":["shoulder","wrist"],
   "goals":["muscle_gain","strength"],"video_url":"https://www.youtube.com/watch?v=8iPEnn-ltC8"},

  {"name":"Decline Push-Up","muscles":["chest","triceps"],
   "environments":["pro_gym","home_gym","outdoor","bodyweight"],
   "avoid_injuries":["wrist","shoulder"],"goals":["muscle_gain","endurance"],
   "video_url":"https://www.youtube.com/watch?v=SKPab2YC8BE"},

  {"name":"Cable Fly","muscles":["chest"],
   "environments":["pro_gym"],"avoid_injuries":["shoulder"],
   "goals":["muscle_gain","fat_loss"],"video_url":"https://www.youtube.com/watch?v=Iwe6AmxVf7o"},

  {"name":"Dumbbell Fly","muscles":["chest"],
   "environments":["pro_gym","home_gym"],"avoid_injuries":["shoulder"],
   "goals":["muscle_gain"],"video_url":"https://www.youtube.com/watch?v=eozdVDA78K0"},

  {"name":"Chest Dip","muscles":["chest","triceps"],
   "environments":["pro_gym","outdoor"],"avoid_injuries":["shoulder","elbow","wrist"],
   "goals":["muscle_gain","strength"],"video_url":"https://www.youtube.com/watch?v=2z8JmcrW-As"},

  {"name":"Close-Grip Push-Up","muscles":["chest","triceps"],
   "environments":["pro_gym","home_gym","outdoor","bodyweight"],
   "avoid_injuries":["wrist","elbow"],"goals":["muscle_gain","endurance"],
   "video_url":"https://www.youtube.com/watch?v=b7pOWdM6_9s"},

  {"name":"Incline Push-Up","muscles":["chest","triceps"],
   "environments":["pro_gym","home_gym","outdoor","bodyweight"],
   "avoid_injuries":["wrist"],"goals":["fat_loss","endurance","muscle_gain"],
   "video_url":"https://www.youtube.com/watch?v=cfns5HQnXFE"},

  # ── BACK ───────────────────────────────────────────────────────────────
  {"name":"Barbell Deadlift","muscles":["back","glutes","hamstrings"],
   "environments":["pro_gym"],"avoid_injuries":["lower_back","knee"],
   "goals":["strength","muscle_gain"],"video_url":"https://www.youtube.com/watch?v=op9kVnSso6Q"},

  {"name":"Romanian Deadlift","muscles":["hamstrings","glutes","back"],
   "environments":["pro_gym","home_gym"],"avoid_injuries":["lower_back","knee"],
   "goals":["muscle_gain","strength"],"video_url":"https://www.youtube.com/watch?v=JCXUYuzwNrM"},

  {"name":"Pull-Up","muscles":["back","biceps"],
   "environments":["pro_gym","home_gym","outdoor","bodyweight"],
   "avoid_injuries":["shoulder","elbow","wrist"],"goals":["muscle_gain","strength"],
   "video_url":"https://www.youtube.com/watch?v=eGo4IYlbE5g"},

  {"name":"Chin-Up","muscles":["back","biceps"],
   "environments":["pro_gym","home_gym","outdoor","bodyweight"],
   "avoid_injuries":["shoulder","elbow","wrist"],"goals":["muscle_gain","strength"],
   "video_url":"https://www.youtube.com/watch?v=brhRXlOhsAM"},

  {"name":"Dumbbell Row","muscles":["back","biceps"],
   "environments":["pro_gym","home_gym"],"avoid_injuries":["lower_back","wrist"],
   "goals":["muscle_gain","strength"],"video_url":"https://www.youtube.com/watch?v=pYcpY20QaE8"},

  {"name":"Barbell Row","muscles":["back","biceps"],
   "environments":["pro_gym"],"avoid_injuries":["lower_back","wrist"],
   "goals":["muscle_gain","strength"],"video_url":"https://www.youtube.com/watch?v=FWJR5Ve8bnQ"},

  {"name":"Lat Pulldown","muscles":["back","biceps"],
   "environments":["pro_gym"],"avoid_injuries":["shoulder","elbow"],
   "goals":["muscle_gain","fat_loss"],"video_url":"https://www.youtube.com/watch?v=CAwf7n6Luuc"},

  {"name":"Seated Cable Row","muscles":["back","biceps","rear_delt"],
   "environments":["pro_gym"],"avoid_injuries":["lower_back","wrist"],
   "goals":["muscle_gain","strength"],"video_url":"https://www.youtube.com/watch?v=GZbfZ033f74"},

  {"name":"Inverted Row","muscles":["back","biceps","rear_delt"],
   "environments":["pro_gym","home_gym","outdoor","bodyweight"],
   "avoid_injuries":["shoulder"],"goals":["muscle_gain","endurance"],
   "video_url":"https://www.youtube.com/watch?v=LkDZXMFoMaY"},

  {"name":"Superman Hold","muscles":["back","glutes"],
   "environments":["pro_gym","home_gym","outdoor","bodyweight"],
   "avoid_injuries":["lower_back"],"goals":["endurance","fat_loss"],
   "video_url":"https://www.youtube.com/watch?v=z6PJMT2y8GQ"},

  {"name":"Good Morning","muscles":["back","hamstrings","glutes"],
   "environments":["pro_gym"],"avoid_injuries":["lower_back","knee"],
   "goals":["strength","muscle_gain"],"video_url":"https://www.youtube.com/watch?v=YA-h3n9L4YU"},

  # ── LEGS ───────────────────────────────────────────────────────────────
  {"name":"Barbell Squat","muscles":["quads","glutes","hamstrings"],
   "environments":["pro_gym"],"avoid_injuries":["knee","lower_back","hip"],
   "goals":["strength","muscle_gain"],"video_url":"https://www.youtube.com/watch?v=ultWZbUMPL8"},

  {"name":"Goblet Squat","muscles":["quads","glutes","core"],
   "environments":["pro_gym","home_gym"],"avoid_injuries":["knee","lower_back"],
   "goals":["fat_loss","muscle_gain","endurance"],"video_url":"https://www.youtube.com/watch?v=MxsFDhcyFyE"},

  {"name":"Bodyweight Squat","muscles":["quads","glutes"],
   "environments":["pro_gym","home_gym","outdoor","bodyweight"],
   "avoid_injuries":["knee"],"goals":["fat_loss","endurance","muscle_gain"],
   "video_url":"https://www.youtube.com/watch?v=aclHkVaku9U"},

  {"name":"Bulgarian Split Squat","muscles":["quads","glutes","hamstrings"],
   "environments":["pro_gym","home_gym","bodyweight"],
   "avoid_injuries":["knee","hip","ankle"],"goals":["muscle_gain","strength"],
   "video_url":"https://www.youtube.com/watch?v=2C-uNgKwPLE"},

  {"name":"Walking Lunge","muscles":["quads","glutes","hamstrings"],
   "environments":["pro_gym","outdoor","bodyweight"],
   "avoid_injuries":["knee","hip","ankle"],"goals":["fat_loss","muscle_gain"],
   "video_url":"https://www.youtube.com/watch?v=L8fvypPrzzs"},

  {"name":"Reverse Lunge","muscles":["quads","glutes"],
   "environments":["pro_gym","home_gym","outdoor","bodyweight"],
   "avoid_injuries":["knee","hip"],"goals":["fat_loss","muscle_gain"],
   "video_url":"https://www.youtube.com/watch?v=xrPteyQLGAo"},

  {"name":"Leg Press","muscles":["quads","glutes"],
   "environments":["pro_gym"],"avoid_injuries":["knee","lower_back"],
   "goals":["muscle_gain","strength"],"video_url":"https://www.youtube.com/watch?v=IZxyjW7MPJQ"},

  {"name":"Leg Curl","muscles":["hamstrings"],
   "environments":["pro_gym"],"avoid_injuries":["knee"],
   "goals":["muscle_gain","strength"],"video_url":"https://www.youtube.com/watch?v=1Tq3QdYUuHs"},

  {"name":"Leg Extension","muscles":["quads"],
   "environments":["pro_gym"],"avoid_injuries":["knee"],
   "goals":["muscle_gain","fat_loss"],"video_url":"https://www.youtube.com/watch?v=YyvSfVjQeL0"},

  {"name":"Calf Raise","muscles":["calves"],
   "environments":["pro_gym","home_gym","outdoor","bodyweight"],
   "avoid_injuries":["ankle"],"goals":["muscle_gain","endurance"],
   "video_url":"https://www.youtube.com/watch?v=-M4-G8p1fCI"},

  {"name":"Glute Bridge","muscles":["glutes","hamstrings"],
   "environments":["pro_gym","home_gym","outdoor","bodyweight"],
   "avoid_injuries":["lower_back"],"goals":["muscle_gain","fat_loss"],
   "video_url":"https://www.youtube.com/watch?v=wPM8icPu6H8"},

  {"name":"Hip Thrust","muscles":["glutes","hamstrings"],
   "environments":["pro_gym","home_gym"],"avoid_injuries":["lower_back","hip"],
   "goals":["muscle_gain","strength"],"video_url":"https://www.youtube.com/watch?v=xDmFkJxPzeM"},

  {"name":"Step-Up","muscles":["quads","glutes"],
   "environments":["pro_gym","outdoor","bodyweight"],
   "avoid_injuries":["knee","ankle"],"goals":["fat_loss","endurance","muscle_gain"],
   "video_url":"https://www.youtube.com/watch?v=dQqApCGd5Ss"},

  {"name":"Wall Sit","muscles":["quads","glutes"],
   "environments":["pro_gym","home_gym","outdoor","bodyweight"],
   "avoid_injuries":["knee"],"goals":["endurance","fat_loss"],
   "video_url":"https://www.youtube.com/watch?v=y-wV4Venusw"},

  # ── SHOULDERS ──────────────────────────────────────────────────────────
  {"name":"Overhead Press","muscles":["shoulders","triceps"],
   "environments":["pro_gym","home_gym"],"avoid_injuries":["shoulder","wrist","neck"],
   "goals":["strength","muscle_gain"],"video_url":"https://www.youtube.com/watch?v=2yjwXTZQDDI"},

  {"name":"Dumbbell Shoulder Press","muscles":["shoulders","triceps"],
   "environments":["pro_gym","home_gym"],"avoid_injuries":["shoulder","wrist"],
   "goals":["muscle_gain","strength"],"video_url":"https://www.youtube.com/watch?v=qEwKCR5JCog"},

  {"name":"Lateral Raise","muscles":["shoulders"],
   "environments":["pro_gym","home_gym"],"avoid_injuries":["shoulder"],
   "goals":["muscle_gain","fat_loss"],"video_url":"https://www.youtube.com/watch?v=3VcKaXpzqRo"},

  {"name":"Front Raise","muscles":["shoulders"],
   "environments":["pro_gym","home_gym"],"avoid_injuries":["shoulder","wrist"],
   "goals":["muscle_gain","fat_loss"],"video_url":"https://www.youtube.com/watch?v=sOm9bazGCqA"},

  {"name":"Face Pull","muscles":["rear_delt","shoulders"],
   "environments":["pro_gym"],"avoid_injuries":["shoulder","elbow"],
   "goals":["muscle_gain","fat_loss"],"video_url":"https://www.youtube.com/watch?v=rep-qVOkqgk"},

  {"name":"Pike Push-Up","muscles":["shoulders","triceps"],
   "environments":["pro_gym","home_gym","outdoor","bodyweight"],
   "avoid_injuries":["shoulder","wrist","neck"],"goals":["muscle_gain","endurance"],
   "video_url":"https://www.youtube.com/watch?v=x7_I5SUAd00"},

  {"name":"Arnold Press","muscles":["shoulders","triceps"],
   "environments":["pro_gym","home_gym"],"avoid_injuries":["shoulder","wrist"],
   "goals":["muscle_gain"],"video_url":"https://www.youtube.com/watch?v=6Z15_WdXmVw"},

  {"name":"Rear Delt Fly","muscles":["rear_delt","shoulders"],
   "environments":["pro_gym","home_gym"],"avoid_injuries":["shoulder"],
   "goals":["muscle_gain","fat_loss"],"video_url":"https://www.youtube.com/watch?v=EA7u4Q_8HQ0"},

  # ── ARMS ───────────────────────────────────────────────────────────────
  {"name":"Barbell Curl","muscles":["biceps"],
   "environments":["pro_gym","home_gym"],"avoid_injuries":["elbow","wrist"],
   "goals":["muscle_gain","strength"],"video_url":"https://www.youtube.com/watch?v=ykJmrZ5v0Oo"},

  {"name":"Dumbbell Curl","muscles":["biceps"],
   "environments":["pro_gym","home_gym"],"avoid_injuries":["elbow","wrist"],
   "goals":["muscle_gain","fat_loss"],"video_url":"https://www.youtube.com/watch?v=ykJmrZ5v0Oo"},

  {"name":"Hammer Curl","muscles":["biceps"],
   "environments":["pro_gym","home_gym"],"avoid_injuries":["elbow","wrist"],
   "goals":["muscle_gain","strength"],"video_url":"https://www.youtube.com/watch?v=zC3nLlEvin4"},

  {"name":"Tricep Dip","muscles":["triceps"],
   "environments":["pro_gym","home_gym","outdoor","bodyweight"],
   "avoid_injuries":["shoulder","elbow","wrist"],"goals":["muscle_gain","strength"],
   "video_url":"https://www.youtube.com/watch?v=0326dy_-CzM"},

  {"name":"Skull Crusher","muscles":["triceps"],
   "environments":["pro_gym","home_gym"],"avoid_injuries":["elbow","wrist"],
   "goals":["muscle_gain","strength"],"video_url":"https://www.youtube.com/watch?v=d_KZxkY_0cM"},

  {"name":"Tricep Pushdown","muscles":["triceps"],
   "environments":["pro_gym"],"avoid_injuries":["elbow","wrist"],
   "goals":["muscle_gain","fat_loss"],"video_url":"https://www.youtube.com/watch?v=2-LAMcpzODU"},

  {"name":"Concentration Curl","muscles":["biceps"],
   "environments":["pro_gym","home_gym"],"avoid_injuries":["elbow"],
   "goals":["muscle_gain"],"video_url":"https://www.youtube.com/watch?v=0AUGkch3tzc"},

  {"name":"Diamond Push-Up","muscles":["triceps","chest"],
   "environments":["pro_gym","home_gym","outdoor","bodyweight"],
   "avoid_injuries":["wrist","elbow"],"goals":["muscle_gain","endurance"],
   "video_url":"https://www.youtube.com/watch?v=J0DnG1_S92I"},

  # ── CORE ───────────────────────────────────────────────────────────────
  {"name":"Plank","muscles":["core"],
   "environments":["pro_gym","home_gym","outdoor","bodyweight"],
   "avoid_injuries":["wrist","shoulder"],"goals":["fat_loss","endurance","strength"],
   "video_url":"https://www.youtube.com/watch?v=pSHjTRCQxIw"},

  {"name":"Side Plank","muscles":["core"],
   "environments":["pro_gym","home_gym","outdoor","bodyweight"],
   "avoid_injuries":["wrist","shoulder"],"goals":["fat_loss","endurance"],
   "video_url":"https://www.youtube.com/watch?v=K2VljzCC16g"},

  {"name":"Dead Bug","muscles":["core"],
   "environments":["pro_gym","home_gym","bodyweight"],
   "avoid_injuries":[],"goals":["fat_loss","endurance"],
   "video_url":"https://www.youtube.com/watch?v=g_BYB0R-4Ws"},

  {"name":"Bicycle Crunch","muscles":["core"],
   "environments":["pro_gym","home_gym","outdoor","bodyweight"],
   "avoid_injuries":["neck","lower_back"],"goals":["fat_loss","endurance"],
   "video_url":"https://www.youtube.com/watch?v=9FGilxCbdz8"},

  {"name":"Hanging Knee Raise","muscles":["core"],
   "environments":["pro_gym","outdoor"],
   "avoid_injuries":["shoulder","wrist","elbow"],"goals":["muscle_gain","fat_loss"],
   "video_url":"https://www.youtube.com/watch?v=Pr1ieGZ5atk"},

  {"name":"Ab Wheel Rollout","muscles":["core"],
   "environments":["pro_gym","home_gym"],
   "avoid_injuries":["lower_back","wrist","shoulder"],"goals":["strength","muscle_gain"],
   "video_url":"https://www.youtube.com/watch?v=IGKjMNsIECg"},

  {"name":"Mountain Climber","muscles":["core","cardio"],
   "environments":["pro_gym","home_gym","outdoor","bodyweight"],
   "avoid_injuries":["wrist","shoulder"],"goals":["fat_loss","endurance"],
   "video_url":"https://www.youtube.com/watch?v=nmwgirgXLYM"},

  {"name":"Russian Twist","muscles":["core"],
   "environments":["pro_gym","home_gym","outdoor","bodyweight"],
   "avoid_injuries":["lower_back"],"goals":["fat_loss","endurance"],
   "video_url":"https://www.youtube.com/watch?v=wkD8rjkodUI"},

  {"name":"Leg Raise","muscles":["core"],
   "environments":["pro_gym","home_gym","outdoor","bodyweight"],
   "avoid_injuries":["lower_back","hip"],"goals":["fat_loss","muscle_gain"],
   "video_url":"https://www.youtube.com/watch?v=JB2oyawG9KI"},

  {"name":"V-Up","muscles":["core"],
   "environments":["pro_gym","home_gym","outdoor","bodyweight"],
   "avoid_injuries":["lower_back","hip"],"goals":["fat_loss","endurance"],
   "video_url":"https://www.youtube.com/watch?v=7UVgs18Y1P4"},

  # ── CARDIO / CONDITIONING ──────────────────────────────────────────────
  {"name":"Burpees","muscles":["cardio","core","chest"],
   "environments":["pro_gym","home_gym","outdoor","bodyweight"],
   "avoid_injuries":["knee","wrist","shoulder"],"goals":["fat_loss","endurance"],
   "video_url":"https://www.youtube.com/watch?v=dZgVxmf6jkA"},

  {"name":"Box Jump","muscles":["cardio","quads","glutes"],
   "environments":["pro_gym","outdoor"],
   "avoid_injuries":["knee","ankle"],"goals":["fat_loss","endurance","strength"],
   "video_url":"https://www.youtube.com/watch?v=52r_Ul5k03g"},

  {"name":"Jump Rope","muscles":["cardio","calves"],
   "environments":["pro_gym","home_gym","outdoor"],
   "avoid_injuries":["ankle","knee"],"goals":["fat_loss","endurance"],
   "video_url":"https://www.youtube.com/watch?v=FJmRQ5iTXKE"},

  {"name":"Treadmill Sprint Intervals","muscles":["cardio","legs"],
   "environments":["pro_gym"],"avoid_injuries":["knee","ankle","hip"],
   "goals":["fat_loss","endurance"],"video_url":"https://www.youtube.com/watch?v=_kGESn8ArrU"},

  {"name":"Jumping Jacks","muscles":["cardio"],
   "environments":["pro_gym","home_gym","outdoor","bodyweight"],
   "avoid_injuries":["ankle","knee"],"goals":["fat_loss","endurance"],
   "video_url":"https://www.youtube.com/watch?v=iSSAk4XCsRA"},

  {"name":"High Knees","muscles":["cardio","core"],
   "environments":["pro_gym","home_gym","outdoor","bodyweight"],
   "avoid_injuries":["knee","ankle","hip"],"goals":["fat_loss","endurance"],
   "video_url":"https://www.youtube.com/watch?v=ZZZoCNMU48U"},

  {"name":"Bear Crawl","muscles":["core","cardio","shoulders"],
   "environments":["pro_gym","home_gym","outdoor","bodyweight"],
   "avoid_injuries":["wrist","shoulder"],"goals":["fat_loss","endurance"],
   "video_url":"https://www.youtube.com/watch?v=pCDoOSCNfhM"},

  {"name":"Battle Ropes","muscles":["cardio","shoulders","core"],
   "environments":["pro_gym"],"avoid_injuries":["shoulder","wrist","elbow"],
   "goals":["fat_loss","endurance"],"video_url":"https://www.youtube.com/watch?v=DZ_BxY2CQJA"},

  {"name":"Sled Push","muscles":["cardio","legs","glutes"],
   "environments":["pro_gym"],"avoid_injuries":["knee","lower_back"],
   "goals":["fat_loss","strength","endurance"],"video_url":"https://www.youtube.com/watch?v=Zi5XapDgtHk"},

  {"name":"Kettlebell Swing","muscles":["glutes","hamstrings","cardio","core"],
   "environments":["pro_gym","home_gym"],"avoid_injuries":["lower_back","wrist","shoulder"],
   "goals":["fat_loss","endurance","strength"],"video_url":"https://www.youtube.com/watch?v=YSxHifyI6s8"},

  {"name":"Rowing Machine","muscles":["cardio","back","legs"],
   "environments":["pro_gym"],"avoid_injuries":["lower_back","wrist"],
   "goals":["fat_loss","endurance"],"video_url":"https://www.youtube.com/watch?v=H0r_3UiUE_k"},

  {"name":"Assault Bike","muscles":["cardio"],
   "environments":["pro_gym"],"avoid_injuries":["knee","shoulder"],
   "goals":["fat_loss","endurance"],"video_url":"https://www.youtube.com/watch?v=2CwryBs7wEI"},
]
