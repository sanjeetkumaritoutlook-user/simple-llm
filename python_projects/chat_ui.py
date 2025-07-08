import os
import streamlit as st
import requests

# Set your token from environment or UI
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
print("🔑 Token in use:", GITHUB_TOKEN[:6] + "..." + GITHUB_TOKEN[-4:])


st.set_page_config(page_title="Chat with LLM", layout="centered")
st.title("💬 GitHub LLM Chatbot")

# Input field for token if not set
if not GITHUB_TOKEN:
    GITHUB_TOKEN = st.text_input("🔐 Enter your GITHUB_TOKEN", type="password")

if not GITHUB_TOKEN:
    st.warning("Please provide your token to continue.")
    st.stop()

endpoint = "https://models.github.ai/inference/chat/completions"
model = "openai/gpt-4.1"

# Initialize conversation state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

# Display past messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    elif msg["role"] == "assistant":
        st.chat_message("assistant").write(msg["content"])

# Chat input
if prompt := st.chat_input("Ask something..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GITHUB_TOKEN}"
    }

    body = {
        "model": model,
        "messages": st.session_state.messages,
        "temperature": 1.0,
        "top_p": 1.0
    }

    try:
        response = requests.post(endpoint, headers=headers, json=body)
        response.raise_for_status()
        assistant_reply = response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        assistant_reply = f"❌ Error: {e}"

    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
    st.chat_message("assistant").write(assistant_reply)
