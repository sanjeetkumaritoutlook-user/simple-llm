import os
import requests

def main():
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("❌ Please set the GITHUB_TOKEN environment variable.")
        return

    endpoint = "https://models.github.ai/inference/chat/completions"
    model = "openai/gpt-4.1"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    # Initialize the conversation
    messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    print("💬 Start chatting with the assistant (type 'exit' or 'quit' to end):")

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Ending chat.")
            break

        # Add user message
        messages.append({"role": "user", "content": user_input})

        # Send POST request to GitHub model endpoint
        response = requests.post(endpoint, headers=headers, json={
            "model": model,
            "messages": messages,
            "temperature": 1.0,
            "top_p": 1.0
        })

        # Handle errors
        if response.status_code != 200:
            print("❌ Error:", response.status_code, response.text)
            break

        result = response.json()
        assistant_reply = result["choices"][0]["message"]["content"]
        print(f"🤖 Assistant: {assistant_reply}")

        # Add assistant reply to the conversation
        messages.append({"role": "assistant", "content": assistant_reply})

if __name__ == "__main__":
    main()
