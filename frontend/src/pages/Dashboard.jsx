import BMICard from "../components/BMICard";
import WorkoutDay from "../components/WorkoutDay";
import ProgressionChart from "../components/ProgressionChart";
import DownloadPlan from "../components/DownloadPlan";
import { useState } from "react";

export default function Dashboard({ plan, reset }) {
  const [activeWeek, setActiveWeek] = useState(0);
  const week = plan.weeks[activeWeek];

  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center">
        <div>
          <h2 className="text-xl font-bold text-gray-800 dark:text-white">Your Plan</h2>
          <p className="text-xs text-gray-500 dark:text-gray-400">{plan.weekly_split}</p>
        </div>
        <button onClick={reset} className="text-sm text-blue-600 dark:text-blue-400 font-medium">← Edit</button>
      </div>

      <BMICard bmi={plan.bmi} />

      <ProgressionChart weeks={plan.weeks} />

      <div className="flex gap-2 overflow-x-auto pb-1">
        {plan.weeks.map((w, i) => (
          <button key={i} onClick={() => setActiveWeek(i)}
            className={`flex-shrink-0 px-4 py-2 rounded-full text-sm font-medium transition ${activeWeek===i ? "bg-blue-600 text-white" : "bg-gray-200 dark:bg-gray-700 dark:text-gray-300"}`}>
            Week {w.week_number}
          </button>
        ))}
      </div>

      <div className="bg-gradient-to-r from-blue-600 to-teal-600 rounded-xl p-4 text-white">
        <p className="text-xs opacity-80">Week {week.week_number} Theme</p>
        <p className="font-semibold mt-0.5">{week.theme}</p>
        <div className="mt-2 bg-white/20 rounded-full h-2">
          <div className="bg-white rounded-full h-2 transition-all" style={{width:`${week.intensity_pct}%`}} />
        </div>
        <p className="text-xs mt-1 opacity-80">Intensity: {week.intensity_pct}%</p>
      </div>

      {week.days.map(day => <WorkoutDay key={day.day_number} day={day} />)}

      <div className="bg-amber-50 dark:bg-amber-900/20 rounded-xl p-4 border border-amber-200 dark:border-amber-700">
        <h4 className="font-semibold text-amber-800 dark:text-amber-400 mb-2 text-sm">Coach Tips</h4>
        <ul className="space-y-1">
          {plan.tips.map((tip, i) => (
            <li key={i} className="text-xs text-amber-700 dark:text-amber-300">• {tip}</li>
          ))}
        </ul>
      </div>

      <DownloadPlan plan={plan} />
    </div>
  );
}
