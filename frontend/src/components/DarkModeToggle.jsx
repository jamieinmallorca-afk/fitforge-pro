export default function DarkModeToggle({ dark, toggle }) {
  return (
    <button onClick={toggle}
      className="w-12 h-6 rounded-full bg-white/20 flex items-center px-1 transition-all">
      <div className={`w-4 h-4 rounded-full bg-white transition-all ${dark ? "translate-x-6" : "translate-x-0"}`} />
    </button>
  );
}
