export default async function handler(req, res) {
  try {
    const token = process.env.GITHUB_TOKEN;

    if (!token) {
      return res.status(500).json({ error: "GITHUB_TOKEN is missing!" });
    }

    const { question } = req.body || {};

    if (!question) {
      return res.status(400).json({ error: "Missing 'question' in request body." });
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

    const result = await response.json();

    if (!response.ok) {
      return res.status(response.status).json({
        error: result.error || "Failed to fetch from inference API",
      });
    }

    return res.status(200).json(result);

  } catch (err) {
    console.error("Internal Server Error:", err);
    return res.status(500).json({
      error: "Internal Server Error",
      details: err.message || err.toString(),
    });
  }
}
