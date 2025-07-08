import os, requests

token = os.getenv("GITHUB_TOKEN") or input("Enter token: ")

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {token}"
}

payload = {
    "model": "openai/gpt-4.1",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello"}
    ],
    "temperature": 1.0,
    "top_p": 1.0
}

response = requests.post("https://models.github.ai/inference/chat/completions",
                         headers=headers, json=payload)

print("Status:", response.status_code)
print("Response:", response.text)
