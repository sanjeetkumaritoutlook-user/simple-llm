export default async function handler(req, res) {
  try {
    const token = process.env.GITHUB_TOKEN;

    if (!token) {
      console.error("❌ Missing GITHUB_TOKEN in environment");
      return res.status(500).json({ error: "Missing GITHUB_TOKEN" });
    }

    // Ensure POST method
    if (req.method !== "POST") {
      return res.status(405).json({ error: "Method not allowed. Use POST." });
    }

    // Parse JSON body safely (for edge functions, req.body might be a stream!)
    let body = req.body;
    if (typeof body === "string") {
      try {
        body = JSON.parse(body);
      } catch (err) {
        return res.status(400).json({ error: "Invalid JSON in request body" });
      }
    }

    const question = body?.question;
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

    const rawText = await response.text();

    if (!response.ok) {
      console.error("❌ API error:", rawText);
      return res.status(response.status).json({
        error: "Upstream API call failed",
        details: rawText
      });
    }

    try {
      const json = JSON.parse(rawText);
      return res.status(200).json(json);
    } catch (e) {
      return res.status(500).json({
        error: "Failed to parse response JSON",
        rawText
      });
    }
  } catch (err) {
    console.error("🔥 Crash:", err);
    return res.status(500).json({
      error: "Internal Server Error",
      details: err.message || err.toString()
    });
  }
}
