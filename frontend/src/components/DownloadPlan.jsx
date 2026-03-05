export default function DownloadPlan({ plan }) {
  const downloadJSON = () => {
    const blob = new Blob([JSON.stringify(plan, null, 2)], {type: "application/json"});
    const url  = URL.createObjectURL(blob);
    const a    = document.createElement("a");
    a.href     = url;
    a.download = "fitforge-plan.json";
    a.click();
    URL.revokeObjectURL(url);
  };

  const downloadText = () => {
    let text = `FitForge Pro Training Plan\n${"=".repeat(40)}\n`;
    text += `Goal: ${plan.goal}\nBMI: ${plan.bmi.value} (${plan.bmi.category})\nSplit: ${plan.weekly_split}\n\n`;
    plan.weeks.forEach(wk => {
      text += `WEEK ${wk.week_number}: ${wk.theme} (${wk.intensity_pct}% intensity)\n`;
      wk.days.forEach(d => {
        text += `  ${d.day_name} — ${d.focus}\n`;
        d.exercises.forEach(e => {
          text += `    • ${e.name}: ${e.sets}x${e.reps} | Rest ${e.rest_seconds}s\n`;
        });
      });
      text += "\n";
    });
    const blob = new Blob([text], {type: "text/plain"});
    const url  = URL.createObjectURL(blob);
    const a    = document.createElement("a");
    a.href=url; a.download="fitforge-plan.txt"; a.click();
    URL.revokeObjectURL(url);
  };

  return (
    <div className="flex gap-3 pb-8">
      <button onClick={downloadJSON}
        className="flex-1 py-3 bg-gray-800 dark:bg-gray-700 text-white rounded-xl text-sm font-medium">
        ↓ JSON
      </button>
      <button onClick={downloadText}
        className="flex-1 py-3 bg-teal-600 text-white rounded-xl text-sm font-medium">
        ↓ Text Plan
      </button>
    </div>
  );
}
