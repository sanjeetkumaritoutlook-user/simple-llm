export default async function handler(req, res) {
  try {
    const token = process.env.GITHUB_TOKEN;

    if (!token) {
      console.error("❌ Missing GITHUB_TOKEN environment variable");
      return res.status(500).json({ error: "Missing GITHUB_TOKEN" });
    }

    const { question } = req.body || {};
    if (!question) {
      return res.status(400).json({ error: "Missing 'question' in request body" });
    }

    const endpoint = "https://models.github.ai/inference";
    const model = "openai/gpt-4.1";

    const response = await fetch(`${endpoint}/chat/completions`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${token}`
      },
      body: JSON.stringify({
        messages: [
          { role: "system", content: "You are a helpful assistant." },
          { role: "user", content: question }
        ],
        temperature: 1.0,
        top_p: 1.0,
        model
      })
    });

    const text = await response.text();
    try {
      const json = JSON.parse(text);

      if (!response.ok) {
        return res.status(response.status).json({
          error: json.error || "API call failed",
          raw: json,
        });
      }

      return res.status(200).json(json);
    } catch (e) {
      return res.status(500).json({
        error: "Failed to parse API response",
        rawText: text,
      });
    }

  } catch (err) {
    console.error("🔥 API crashed:", err);
    return res.status(500).json({ error: "Server error", details: err.message });
  }
}
