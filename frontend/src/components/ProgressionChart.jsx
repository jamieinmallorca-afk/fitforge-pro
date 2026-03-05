export default function ProgressionChart({ weeks }) {
  const max = 100;
  const colors = ["#3B82F6","#10B981","#EF4444","#8B5CF6"];

  return (
    <div className="bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700 p-4">
      <p className="text-xs font-semibold text-gray-500 dark:text-gray-400 mb-3">4-Week Progression</p>
      <div className="flex items-end gap-3 h-20">
        {weeks.map((w, i) => (
          <div key={i} className="flex-1 flex flex-col items-center gap-1">
            <span className="text-xs font-bold" style={{color: colors[i]}}>{w.intensity_pct}%</span>
            <div className="w-full rounded-t-md transition-all" style={{
              height: `${(w.intensity_pct / max) * 64}px`,
              backgroundColor: colors[i]
            }} />
            <span className="text-xs text-gray-400">Wk{w.week_number}</span>
          </div>
        ))}
      </div>
    </div>
  );
}
