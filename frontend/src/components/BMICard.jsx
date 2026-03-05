export default function BMICard({ bmi }) {
  const colors = {
    "Underweight": "blue", "Normal weight": "green",
    "Overweight": "yellow", "Obese": "red"
  };
  const color = colors[bmi.category] || "gray";
  const pct   = Math.min(100, Math.max(0, ((bmi.value - 10) / 35) * 100));

  return (
    <div className="bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700 p-4">
      <div className="flex justify-between items-start">
        <div>
          <p className="text-xs text-gray-500 dark:text-gray-400">BMI Score</p>
          <p className="text-3xl font-bold text-gray-800 dark:text-white">{bmi.value}</p>
          <span className={`text-xs font-semibold px-2 py-0.5 rounded-full bg-${color}-100 text-${color}-700`}>
            {bmi.category}
          </span>
        </div>
        <div className="text-right text-xs text-gray-400">
          <p>Healthy range</p>
          <p className="font-semibold text-gray-700 dark:text-gray-300">{bmi.healthy_range}</p>
        </div>
      </div>
      <div className="mt-3 bg-gradient-to-r from-blue-300 via-green-400 via-yellow-400 to-red-400 rounded-full h-2 relative">
        <div className="absolute top-1/2 -translate-y-1/2 w-3 h-3 bg-white border-2 border-gray-700 rounded-full shadow"
          style={{left:`calc(${pct}% - 6px)`}} />
      </div>
      <div className="flex justify-between text-xs text-gray-400 mt-1">
        <span>10</span><span>18.5</span><span>25</span><span>30</span><span>45</span>
      </div>
    </div>
  );
}
