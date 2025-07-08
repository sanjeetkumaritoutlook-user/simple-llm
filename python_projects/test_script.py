import requests

token = "ghp_your_token_here"
endpoint = "https://models.github.ai/inference/chat/completions"

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

data = {
    "model": "openai/gpt-4.1",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello"}
    ],
    "temperature": 1.0,
    "top_p": 1.0
}

response = requests.post(endpoint, headers=headers, json=data)
print("Status:", response.status_code)
print("Response:", response.text)
