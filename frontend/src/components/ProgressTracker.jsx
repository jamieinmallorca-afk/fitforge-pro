import { useState } from "react";

const STORAGE_KEY = "fitforge_progress";

function getProgress() {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEY) || "{}");
  } catch { return {}; }
}

export default function ProgressTracker({ weeks }) {
  const [progress, setProgress] = useState(getProgress);
  const [open, setOpen] = useState(false);

  const toggle = (weekNum, dayNum) => {
    const key = `w${weekNum}_d${dayNum}`;
    const updated = {...progress, [key]: !progress[key]};
    setProgress(updated);
    localStorage.setItem(STORAGE_KEY, JSON.stringify(updated));
  };

  const total    = weeks.reduce((a, w) => a + w.days.length, 0);
  const completed = Object.values(progress).filter(Boolean).length;
  const pct = Math.round((completed / total) * 100);

  return (
    <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 p-4">
      <button onClick={() => setOpen(!open)} className="w-full">
        <div className="flex justify-between items-center mb-3">
          <p className="text-xs font-bold text-gray-500 dark:text-gray-400">✅ Progress Tracker</p>
          <span className="text-xs font-bold text-green-600">{completed}/{total} sessions</span>
        </div>
        <div className="bg-gray-100 dark:bg-gray-700 rounded-full h-3">
          <div className="h-3 rounded-full bg-gradient-to-r from-green-400 to-teal-500 transition-all"
            style={{width:`${pct}%`}} />
        </div>
        <p className="text-xs text-gray-400 mt-1 text-right">{pct}% complete {open ? "▲" : "▼"}</p>
      </button>

      {open && (
        <div className="mt-4 space-y-3">
          {weeks.map(week => (
            <div key={week.week_number}>
              <p className="text-xs font-bold text-gray-600 dark:text-gray-400 mb-2">Week {week.week_number}</p>
              <div className="flex flex-wrap gap-2">
                {week.days.map(day => {
                  const key = `w${week.week_number}_d${day.day_number}`;
                  const done = progress[key];
                  return (
                    <button key={key} onClick={() => toggle(week.week_number, day.day_number)}
                      className={`px-3 py-1.5 rounded-xl text-xs font-semibold transition-all ${done ? "bg-green-500 text-white" : "bg-gray-100 dark:bg-gray-700 text-gray-500"}`}>
                      {done ? "✓" : ""} {day.day_name.slice(0,3)} · {day.focus}
                    </button>
                  );
                })}
              </div>
            </div>
          ))}
          <button onClick={() => { setProgress({}); localStorage.removeItem(STORAGE_KEY); }}
            className="text-xs text-red-400 hover:text-red-500 mt-2">
            Reset progress
          </button>
        </div>
      )}
    </div>
  );
}
