import { useState } from "react";
import Home from "./pages/Home";
import Dashboard from "./pages/Dashboard";
import DarkModeToggle from "./components/DarkModeToggle";

export default function App() {
  const [plan, setPlan]     = useState(null);
  const [dark, setDark]     = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError]   = useState(null);

  return (
    <div className={dark ? "dark" : ""}>
      <div className="min-h-screen bg-gray-50 dark:bg-gray-950 transition-colors">
        <header className="bg-gradient-to-r from-blue-900 to-teal-700 text-white px-4 py-4 flex justify-between items-center shadow-lg">
          <div>
            <h1 className="text-xl font-bold tracking-tight">FitForge Pro</h1>
            <p className="text-xs text-blue-200">AI-powered training plans</p>
          </div>
          <DarkModeToggle dark={dark} toggle={() => setDark(!dark)} />
        </header>
        <main className="max-w-2xl mx-auto px-4 py-6">
          {!plan ? (
            <Home
              setLoading={setLoading}
              setPlan={setPlan}
              setError={setError}
              loading={loading}
              error={error}
            />
          ) : (
            <Dashboard plan={plan} reset={() => setPlan(null)} />
          )}
        </main>
      </div>
    </div>
  );
}
