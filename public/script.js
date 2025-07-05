const form = document.getElementById('ask-form');
const input = document.getElementById('question');
const output = document.getElementById('answer');

form.addEventListener('submit', async (e) => {
  e.preventDefault();

  const question = input.value.trim();
  if (!question) return;

  output.textContent = "⏳ Thinking...";

  try {
    const res = await fetch("/api/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question })
    });

    const data = await res.json();
    const markdown = data?.choices?.[0]?.message?.content || "⚠️ No answer received.";
    output.innerHTML = marked.parse(markdown);
  } catch (err) {
    output.textContent = "❌ Failed to fetch response.";
    console.error("API error:", err);
  }
});
