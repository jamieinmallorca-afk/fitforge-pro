import BMICard from "../components/BMICard";
import WorkoutDay from "../components/WorkoutDay";
import ProgressionChart from "../components/ProgressionChart";
import DownloadPlan from "../components/DownloadPlan";
import CalorieCard from "../components/CalorieCard";
import ProgressTracker from "../components/ProgressTracker";
import { useState } from "react";

export default function Dashboard({ plan, reset }) {
  const [activeWeek, setActiveWeek] = useState(0);
  const week = plan.weeks[activeWeek];

  const printPlan = () => window.print();

  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center">
        <div>
          <h2 className="text-2xl font-black text-gray-800 dark:text-white">
            {plan.user_name !== "Athlete" ? `${plan.user_name}'s Plan` : "Your Plan"}
          </h2>
          <p className="text-xs text-gray-500 dark:text-gray-400">{plan.weekly_split} · {plan.goal}</p>
        </div>
        <div className="flex gap-2">
          <button onClick={printPlan}
            className="text-xs bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-300 px-3 py-2 rounded-xl font-medium">
            🖨️ Print
          </button>
          <button onClick={reset}
            className="text-xs text-blue-600 dark:text-blue-400 font-semibold px-3 py-2">
            ← Edit
          </button>
        </div>
      </div>

      <BMICard bmi={plan.bmi} />

      <CalorieCard calories={plan.calories} goal={plan.goal} />

      <ProgressionChart weeks={plan.weeks} />

      <ProgressTracker weeks={plan.weeks} />

      <div className="flex gap-2 overflow-x-auto pb-1">
        {plan.weeks.map((w, i) => (
          <button key={i} onClick={() => setActiveWeek(i)}
            className={`flex-shrink-0 px-4 py-2 rounded-full text-sm font-semibold transition ${activeWeek===i ? "bg-blue-600 text-white" : "bg-gray-200 dark:bg-gray-700 dark:text-gray-300"}`}>
            Week {w.week_number}
          </button>
        ))}
      </div>

      <div className="bg-gradient-to-r from-blue-600 to-teal-600 rounded-2xl p-4 text-white">
        <p className="text-xs opacity-80">Week {week.week_number} Theme</p>
        <p className="font-black text-lg mt-0.5">{week.theme}</p>
        <div className="mt-2 bg-white/20 rounded-full h-2">
          <div className="bg-white rounded-full h-2 transition-all" style={{width:`${week.intensity_pct}%`}} />
        </div>
        <p className="text-xs mt-1 opacity-80">Intensity: {week.intensity_pct}%</p>
      </div>

      {week.days.map(day => <WorkoutDay key={day.day_number} day={day} />)}

      <div className="bg-amber-50 dark:bg-amber-900/20 rounded-2xl p-4 border border-amber-200 dark:border-amber-700">
        <h4 className="font-bold text-amber-800 dark:text-amber-400 mb-3 text-sm">💡 Coach Tips</h4>
        <ul className="space-y-2">
          {plan.tips.map((tip, i) => (
            <li key={i} className="text-xs text-amber-700 dark:text-amber-300 flex gap-2">
              <span>•</span><span>{tip}</span>
            </li>
          ))}
        </ul>
      </div>

      <DownloadPlan plan={plan} />
    </div>
  );
}
