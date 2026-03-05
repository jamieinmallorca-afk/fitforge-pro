export default function CalorieCard({ calories, goal }) {
  const macros = [
    { label: "Protein", value: calories.protein_g, unit: "g", color: "blue", pct: Math.round(calories.protein_g * 4 / calories.target * 100) },
    { label: "Carbs",   value: calories.carbs_g,   unit: "g", color: "teal", pct: Math.round(calories.carbs_g * 4 / calories.target * 100) },
    { label: "Fat",     value: calories.fat_g,      unit: "g", color: "orange", pct: Math.round(calories.fat_g * 9 / calories.target * 100) },
  ];

  return (
    <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 p-4">
      <p className="text-xs font-bold text-gray-500 dark:text-gray-400 mb-3">🍎 Daily Nutrition Target</p>
      <div className="flex justify-between items-center mb-4">
        <div>
          <p className="text-3xl font-black text-gray-800 dark:text-white">{calories.target}<span className="text-sm font-normal text-gray-400 ml-1">kcal</span></p>
          <p className="text-xs text-gray-400 mt-0.5">TDEE: {calories.tdee} kcal · {goal.includes("fat_loss") || goal.includes("Fat") ? "deficit" : goal.includes("muscle") || goal.includes("Muscle") ? "surplus" : "maintenance"}</p>
        </div>
        <div className="text-right">
          <p className="text-xs text-gray-400">Daily target</p>
        </div>
      </div>
      <div className="space-y-2">
        {macros.map(({label, value, unit, color, pct}) => (
          <div key={label}>
            <div className="flex justify-between text-xs mb-1">
              <span className="font-medium text-gray-600 dark:text-gray-300">{label}</span>
              <span className="font-bold text-gray-800 dark:text-white">{value}{unit} <span className="text-gray-400 font-normal">({pct}%)</span></span>
            </div>
            <div className="bg-gray-100 dark:bg-gray-700 rounded-full h-1.5">
              <div className={`h-1.5 rounded-full bg-${color}-500`} style={{width:`${pct}%`}} />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
