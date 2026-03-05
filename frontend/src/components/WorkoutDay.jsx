import { useState } from "react";

export default function WorkoutDay({ day }) {
  const [open, setOpen] = useState(false);

  return (
    <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700">
      <button onClick={() => setOpen(!open)}
        className="w-full flex justify-between items-center p-4">
        <div className="text-left">
          <p className="font-bold text-gray-800 dark:text-white text-sm">
            Day {day.day_number} — {day.day_name}
          </p>
          <p className="text-xs text-teal-600 dark:text-teal-400 font-semibold mt-0.5">{day.focus}</p>
        </div>
        <div className="flex items-center gap-2">
          <span className="text-xs bg-blue-100 dark:bg-blue-900/30 text-blue-700 dark:text-blue-400 px-2 py-1 rounded-full font-medium">
            {day.exercises.length} exercises
          </span>
          <span className="text-gray-400">{open ? "▲" : "▼"}</span>
        </div>
      </button>

      {open && (
        <div className="border-t border-gray-100 dark:border-gray-700 divide-y divide-gray-50 dark:divide-gray-700/50">
          {day.exercises.map((ex, i) => (
            <div key={i} className="px-4 py-3">
              <div className="flex justify-between items-start">
                <div className="flex-1">
                  <p className="text-sm font-semibold text-gray-800 dark:text-white">{ex.name}</p>
                  {ex.notes && <p className="text-xs text-gray-400 mt-0.5">{ex.notes}</p>}
                  {ex.video_url && (
                    <a href={ex.video_url} target="_blank" rel="noopener noreferrer"
                      className="inline-flex items-center gap-1 text-xs text-red-500 hover:text-red-600 mt-1 font-medium">
                      ▶ Watch video
                    </a>
                  )}
                </div>
                <div className="text-right text-xs ml-4 flex-shrink-0">
                  <p className="font-bold text-blue-600 dark:text-blue-400 text-sm">{ex.sets} × {ex.reps}</p>
                  <p className="text-gray-400 mt-0.5">Rest {ex.rest_seconds}s</p>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
