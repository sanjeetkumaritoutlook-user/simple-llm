import os
import requests

def main():
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("Please set the GITHUB_TOKEN environment variable.")
        return

    endpoint = "https://models.github.ai/inference/chat/completions"
    model = "openai/gpt-4.1"

    user_input = input("Ask a question: ")

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ],
        "temperature": 1.0,
        "top_p": 1.0
    }

    response = requests.post(endpoint, headers=headers, json=payload)

    if response.status_code != 200:
        print("Error:", response.status_code, response.text)
        return

    result = response.json()
    print("\nAnswer:", result["choices"][0]["message"]["content"])

if __name__ == "__main__":
    main()
