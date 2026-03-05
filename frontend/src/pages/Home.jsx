import { useState } from "react";
import { generatePlan } from "../api";

const INJURIES = ["none","lower_back","knee","shoulder","wrist","ankle","neck","hip","elbow"];
const ENVS = [{v:"home_gym",l:"Home Gym"},{v:"pro_gym",l:"Pro Gym"},
              {v:"outdoor",l:"Outdoor"},{v:"bodyweight",l:"Bodyweight Only"}];
const GOALS = [{v:"fat_loss",l:"Fat Loss"},{v:"muscle_gain",l:"Muscle Gain"},
               {v:"strength",l:"Strength"},{v:"endurance",l:"Endurance"}];
const LEVELS = ["beginner","intermediate","advanced"];

export default function Home({ setLoading, setPlan, setError, loading, error }) {
  const [form, setForm] = useState({
    age:20, weight_kg:70, height_cm:175,
    fitness_level:"beginner", injuries:["none"],
    environment:["bodyweight"], goal:"fat_loss",
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
    } catch(e) { setError(e.message); }
    finally   { setLoading(false); }
  };

  const inp = "w-full border border-gray-300 dark:border-gray-600 rounded-lg px-3 py-2 bg-white dark:bg-gray-800 dark:text-white text-sm focus:outline-none focus:ring-2 focus:ring-blue-500";

  return (
    <div className="space-y-5">
      <div className="text-center py-4">
        <h2 className="text-2xl font-bold text-gray-800 dark:text-white">Build Your Plan</h2>
        <p className="text-gray-500 dark:text-gray-400 text-sm mt-1">Complete the form to get a personalised 4-week programme</p>
      </div>

      <Card title="Basic Stats">
        <div className="grid grid-cols-3 gap-3">
          {[["Age","age",16,80],["Weight (kg)","weight_kg",30,300],["Height (cm)","height_cm",100,250]].map(([lbl,key,min,max]) => (
            <div key={key}>
              <label className="text-xs text-gray-500 dark:text-gray-400 block mb-1">{lbl}</label>
              <input type="number" min={min} max={max} value={form[key]}
                onChange={e => setForm({...form,[key]:+e.target.value})}
                className={inp} />
            </div>
          ))}
        </div>
      </Card>

      <Card title="Fitness Level">
        <div className="flex gap-2">
          {LEVELS.map(l => (
            <button key={l} onClick={() => setForm({...form,fitness_level:l})}
              className={`flex-1 py-2 rounded-lg text-sm font-medium capitalize transition ${form.fitness_level===l ? "bg-blue-600 text-white" : "bg-gray-100 dark:bg-gray-700 dark:text-gray-300"}`}>
              {l}
            </button>
          ))}
        </div>
      </Card>

      <Card title="Your Goal">
        <div className="grid grid-cols-2 gap-2">
          {GOALS.map(({v,l}) => (
            <button key={v} onClick={() => setForm({...form,goal:v})}
              className={`py-3 rounded-lg text-sm font-medium transition ${form.goal===v ? "bg-teal-600 text-white" : "bg-gray-100 dark:bg-gray-700 dark:text-gray-300"}`}>
              {l}
            </button>
          ))}
        </div>
      </Card>

      <Card title="Training Environment (multi-select)">
        <div className="grid grid-cols-2 gap-2">
          {ENVS.map(({v,l}) => (
            <button key={v} onClick={() => toggleList("environment", v)}
              className={`py-3 rounded-lg text-sm font-medium transition ${form.environment.includes(v) ? "bg-orange-500 text-white" : "bg-gray-100 dark:bg-gray-700 dark:text-gray-300"}`}>
              {l}
            </button>
          ))}
        </div>
      </Card>

      <Card title="Injuries (multi-select)">
        <div className="flex flex-wrap gap-2">
          {INJURIES.map(inj => (
            <button key={inj} onClick={() => toggleList("injuries", inj)}
              className={`px-3 py-1 rounded-full text-xs font-medium capitalize transition ${form.injuries.includes(inj) ? "bg-red-500 text-white" : "bg-gray-100 dark:bg-gray-700 dark:text-gray-300"}`}>
              {inj.replace("_"," ")}
            </button>
          ))}
        </div>
      </Card>

      <Card title="Schedule">
        <div className="grid grid-cols-2 gap-4">
          <div>
            <label className="text-xs text-gray-500 dark:text-gray-400 block mb-1">Days per week: {form.days_per_week}</label>
            <input type="range" min={2} max={6} value={form.days_per_week}
              onChange={e => setForm({...form,days_per_week:+e.target.value})}
              className="w-full accent-blue-600" />
          </div>
          <div>
            <label className="text-xs text-gray-500 dark:text-gray-400 block mb-1">Session: {form.session_minutes} min</label>
            <input type="range" min={20} max={120} step={5} value={form.session_minutes}
              onChange={e => setForm({...form,session_minutes:+e.target.value})}
              className="w-full accent-teal-600" />
          </div>
        </div>
      </Card>

      {error && <div className="bg-red-50 dark:bg-red-900/30 text-red-600 dark:text-red-400 rounded-lg p-3 text-sm">{error}</div>}

      <button onClick={submit} disabled={loading}
        className="w-full py-4 bg-gradient-to-r from-blue-700 to-teal-600 text-white font-bold rounded-xl text-base shadow-lg active:scale-95 transition disabled:opacity-60">
        {loading ? "Generating your plan..." : "Generate My Training Plan →"}
      </button>
    </div>
  );
}

function Card({ title, children }) {
  return (
    <div className="bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700 p-4">
      <h3 className="text-sm font-semibold text-gray-700 dark:text-gray-300 mb-3">{title}</h3>
      {children}
    </div>
  );
}
