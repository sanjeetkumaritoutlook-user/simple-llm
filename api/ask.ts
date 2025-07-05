export default async function handler(req, res) {
  const token = process.env.GITHUB_TOKEN;

  // 🔐 Quick test: check if secret is present (safe to leave temporarily)
  if (!token) {
    return res.status(500).json({ error: "GITHUB_TOKEN is missing!" });
  }

  // ✅ Optional: confirm secret loaded (but don’t show full token!)
  if (req.query.test === "true") {
    return res.status(200).json({
      message: "Secret loaded securely 🎉",
      tokenPreview: token.slice(0, 4) + "...[hidden]",
    });
  }

  // 🔄 Actual AI inference logic
  const { question } = req.body;
  const endpoint = "https://models.github.ai/inference";
  const model = "openai/gpt-4.1";

  try {
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

    if (!response.ok) {
      const errorBody = await response.text();
      return res.status(response.status).json({
        error: "Inference API failed",
        details: errorBody,
      });
    }

    const result = await response.json();
    return res.status(200).json(result);

  } catch (err) {
    return res.status(500).json({
      error: "Unexpected error",
      details: err.message || err.toString(),
    });
  }
}
