import os
from openai import OpenAI
## pip install openai

# Get token from environment
token = os.environ["GITHUB_TOKEN"]

# Ask the user for input from the command line
user_question = input("Ask a question: ")

# Define endpoint and model
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1"

# Initialize the OpenAI client
client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

# Send the chat completion request
response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": user_question,
        }
    ],
    temperature=1.0,
    top_p=1.0,
    model=model
)

# Print the assistant's reply
print(response.choices[0].message.content)

