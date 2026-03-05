import { useState } from "react";

export default function WorkoutDay({ day }) {
  const [open, setOpen] = useState(false);

  return (
    <div className="bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700">
      <button onClick={() => setOpen(!open)}
        className="w-full flex justify-between items-center p-4">
        <div className="text-left">
          <p className="font-semibold text-gray-800 dark:text-white text-sm">
            Day {day.day_number} — {day.day_name}
          </p>
          <p className="text-xs text-teal-600 dark:text-teal-400 font-medium">{day.focus}</p>
        </div>
        <div className="flex items-center gap-3">
          <span className="text-xs bg-blue-100 dark:bg-blue-900/30 text-blue-700 dark:text-blue-400 px-2 py-0.5 rounded-full">
            {day.exercises.length} exercises
          </span>
          <span className="text-gray-400 text-sm">{open ? "▲" : "▼"}</span>
        </div>
      </button>

      {open && (
        <div className="border-t border-gray-100 dark:border-gray-700 divide-y divide-gray-50 dark:divide-gray-700">
          {day.exercises.map((ex, i) => (
            <div key={i} className="px-4 py-3 flex justify-between items-center">
              <div>
                <p className="text-sm font-medium text-gray-800 dark:text-white">{ex.name}</p>
                {ex.notes && <p className="text-xs text-gray-400">{ex.notes}</p>}
              </div>
              <div className="text-right text-xs">
                <p className="font-semibold text-blue-600 dark:text-blue-400">{ex.sets} × {ex.reps}</p>
                <p className="text-gray-400">Rest {ex.rest_seconds}s</p>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
