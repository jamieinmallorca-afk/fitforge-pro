const BASE_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

export async function generatePlan(profileData) {
  const response = await fetch(`${BASE_URL}/generate-plan`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(profileData),
  });
  if (!response.ok) {
    const err = await response.json();
    throw new Error(err.detail || "Failed to generate plan");
  }
  return response.json();
}

export async function checkHealth() {
  const res = await fetch(`${BASE_URL}/health`);
  return res.json();
}
