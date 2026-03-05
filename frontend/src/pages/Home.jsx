import { useState } from "react";
import { generatePlan } from "../api";

const INJURIES = ["none","lower_back","knee","shoulder","wrist","ankle","neck","hip","elbow"];
const ENVS = [{v:"home_gym",l:"🏠 Home Gym"},{v:"pro_gym",l:"🏋️ Pro Gym"},
              {v:"outdoor",l:"🌳 Outdoor"},{v:"bodyweight",l:"💪 Bodyweight"}];
const GOALS = [{v:"fat_loss",l:"🔥 Fat Loss"},{v:"muscle_gain",l:"💪 Muscle Gain"},
               {v:"strength",l:"⚡ Strength"},{v:"endurance",l:"🏃 Endurance"}];
const LEVELS = [{v:"beginner",l:"Beginner"},{v:"intermediate",l:"Intermediate"},{v:"advanced",l:"Advanced"}];

export default function Home({ setLoading, setPlan, setError, loading, error }) {
  const [form, setForm] = useState({
    name:"", age:25, weight_kg:75, height_cm:175,
    fitness_level:"beginner", injuries:["none"],
    environment:["bodyweight"], goal:["fat_loss"],
    days_per_week:3, session_minutes:45
  });

  const toggleList = (field, val) => {
    setForm(f => {
      const arr = f[field].includes(val)
        ? f[field].filter(x => x !== val)
        : [...f[field].filter(x => x !== "none"), val];
      return {...f, [field]: arr.length ? arr : [val]};
    });
  };

  const submit = async () => {
    setLoading(true); setError(null);
    try {
      const plan = await generatePlan(form);
      setPlan(plan);
    } catch(e) {
      setError(typeof e.message === "string" ? e.message : "Something went wrong. Please try again.");
    } finally { setLoading(false); }
  };

  const inp = "w-full border border-gray-200 dark:border-gray-600 rounded-xl px-4 py-3 bg-gray-50 dark:bg-gray-900 dark:text-white text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 transition";

  return (
    <div className="space-y-4">
      <div className="text-center py-6">
        <div className="inline-flex items-center justify-center w-16 h-16 bg-gradient-to-br from-blue-600 to-teal-500 rounded-2xl mb-4 shadow-lg">
          <span className="text-3xl">🏋️</span>
        </div>
        <h2 className="text-3xl font-black text-gray-900 dark:text-white">Build Your Plan</h2>
        <p className="text-gray-500 dark:text-gray-400 text-sm mt-2">Fill in your details for a personalised 4-week programme</p>
      </div>

      <Card title="👤 Your Name">
        <input type="text" placeholder="Enter your name" value={form.name}
          onChange={e => setForm({...form, name: e.target.value})}
          className={inp} />
      </Card>

      <Card title="📊 Basic Stats">
        <div className="grid grid-cols-3 gap-3">
          {[["Age","age",16,80,"yrs"],["Weight","weight_kg",30,300,"kg"],["Height","height_cm",100,250,"cm"]].map(([lbl,key,min,max,unit]) => (
            <div key={key} className="text-center">
              <label className="text-xs font-medium text-gray-500 dark:text-gray-400 block mb-2">{lbl}</label>
              <div className="relative">
                <input type="number" min={min} max={max} value={form[key]}
                  onChange={e => setForm({...form,[key]:+e.target.value})}
                  className={inp + " text-center font-bold text-lg pr-8"} />
                <span className="absolute right-3 top-1/2 -translate-y-1/2 text-xs text-gray-400">{unit}</span>
              </div>
            </div>
          ))}
        </div>
      </Card>

      <Card title="🎯 Fitness Level">
        <div className="flex gap-2">
          {LEVELS.map(({v,l}) => (
            <button key={v} onClick={() => setForm({...form,fitness_level:v})}
              className={`flex-1 py-3 rounded-xl text-sm font-semibold transition-all ${form.fitness_level===v ? "bg-blue-600 text-white shadow-md scale-105" : "bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-300 hover:bg-gray-200"}`}>
              {l}
            </button>
          ))}
        </div>
      </Card>

      <Card title="🎯 Your Goals (pick all that apply)">
        <div className="grid grid-cols-2 gap-2">
          {GOALS.map(({v,l}) => (
            <button key={v} onClick={() => toggleList("goal", v)}
              className={`py-3 px-2 rounded-xl text-sm font-semibold transition-all ${form.goal.includes(v) ? "bg-teal-500 text-white shadow-md scale-105" : "bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-300 hover:bg-gray-200"}`}>
              {l}
            </button>
          ))}
        </div>
      </Card>

      <Card title="🏟️ Training Environment (pick all that apply)">
        <div className="grid grid-cols-2 gap-2">
          {ENVS.map(({v,l}) => (
            <button key={v} onClick={() => toggleList("environment", v)}
              className={`py-3 px-2 rounded-xl text-sm font-semibold transition-all ${form.environment.includes(v) ? "bg-orange-500 text-white shadow-md scale-105" : "bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-300 hover:bg-gray-200"}`}>
              {l}
            </button>
          ))}
        </div>
      </Card>

      <Card title="🩹 Injuries (pick all that apply)">
        <div className="flex flex-wrap gap-2">
          {INJURIES.map(inj => (
            <button key={inj} onClick={() => toggleList("injuries", inj)}
              className={`px-3 py-1.5 rounded-full text-xs font-semibold capitalize transition-all ${form.injuries.includes(inj) ? "bg-red-500 text-white shadow-sm" : "bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-300 hover:bg-gray-200"}`}>
              {inj.replace("_"," ")}
            </button>
          ))}
        </div>
      </Card>

      <Card title="📅 Schedule">
        <div className="space-y-4">
          <div>
            <div className="flex justify-between mb-2">
              <label className="text-sm font-medium text-gray-600 dark:text-gray-300">Days per week</label>
              <span className="text-sm font-bold text-blue-600 dark:text-blue-400">{form.days_per_week} days</span>
            </div>
            <input type="range" min={2} max={6} value={form.days_per_week}
              onChange={e => setForm({...form,days_per_week:+e.target.value})}
              className="w-full accent-blue-600 h-2" />
            <div className="flex justify-between text-xs text-gray-400 mt-1">
              <span>2 days</span><span>6 days</span>
            </div>
          </div>
          <div>
            <div className="flex justify-between mb-2">
              <label className="text-sm font-medium text-gray-600 dark:text-gray-300">Session length</label>
              <span className="text-sm font-bold text-teal-600 dark:text-teal-400">{form.session_minutes} min</span>
            </div>
            <input type="range" min={20} max={120} step={5} value={form.session_minutes}
              onChange={e => setForm({...form,session_minutes:+e.target.value})}
              className="w-full accent-teal-600 h-2" />
            <div className="flex justify-between text-xs text-gray-400 mt-1">
              <span>20 min</span><span>120 min</span>
            </div>
          </div>
        </div>
      </Card>

      {error && (
        <div className="bg-red-50 dark:bg-red-900/30 border border-red-200 dark:border-red-700 text-red-700 dark:text-red-400 rounded-xl p-4 text-sm flex items-start gap-2">
          <span>⚠️</span><span>{error}</span>
        </div>
      )}

      <button onClick={submit} disabled={loading}
        className="w-full py-4 bg-gradient-to-r from-blue-700 to-teal-600 text-white font-black rounded-2xl text-lg shadow-xl active:scale-95 transition-all disabled:opacity-60 disabled:cursor-not-allowed">
        {loading ? "⏳ Generating your plan..." : "Generate My Training Plan →"}
      </button>

      <p className="text-center text-xs text-gray-400 pb-4">Powered by evidence-based training science</p>
    </div>
  );
}

function Card({ title, children }) {
  return (
    <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 p-5">
      <h3 className="text-sm font-bold text-gray-700 dark:text-gray-300 mb-4">{title}</h3>
      {children}
    </div>
  );
}
