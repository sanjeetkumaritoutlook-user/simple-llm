## Full stack app hosted on Vercel
Anyone can see your token in browser dev tools. So, we CANNOT securely use GITHUB_TOKEN (or Azure tokens) in frontend JS directly.

another running app on vercel:

https://space-dashboard-ivory.vercel.app/

Vercel runs your TypeScript API route (api/ask.ts) in a serverless environment, 

and TypeScript doesn’t know about the process object (which is Node-specific) unless you explicitly install the Node types.

npm install --save-dev @types/node

check Vercel project deployment build logs once, as the vercel can still show deployment successful with 500 internal server error

Vercel swallows uncaught exceptions in Serverless Functions and replaces them with a generic 500: FUNCTION_INVOCATION_FAILED,

## Dev Local Vector Store for Genkit
https://www.npmjs.com/package/@genkit-ai/dev-local-vectorstore

Python libraries like NumPy, Pandas, and scikit-learn,

which are core tools for data analysis and machine learning.
## Solution Architecture (2 Parts):
### Frontend UI (hosted on GitHub Pages)
Simple HTML/JS app where user types a question.

Sends a request to your backend.

###  Backend API Proxy (hosted separately, e.g., GitHub Actions, Vercel, or Cloudflare Workers)
Handles the secret GITHUB_TOKEN.

Makes the actual request to https://models.github.ai/inference.

Returns only the result to frontend.

Use Vercel or Netlify Functions to host this, and configure GITHUB_TOKEN in their secret environment variables.

Here its serverless Function

Vercel is better than Netlify in case of full stack app hosting

## Step-by-Step: Configure GITHUB_TOKEN in Vercel
🛠️ 1. Go to your Vercel project

Visit: https://vercel.com/dashboard

Click on your project

🔐 2. Open the “Environment Variables” Section
 
In your project dashboard, go to:

Settings → Environment Variables

➕3. Add a New Environment Variable
 
Key: GITHUB_TOKEN

Value: (paste your actual GitHub token here)

Choose Environment: Production (and optionally Preview, Development)

Click “Add”

Repeat this for any other secret you want (like AZURE_API_KEY, etc.)

💾 4. Redeploy to apply the secret

After adding, go to the Deployments tab

Click “Redeploy” (or make a small commit to trigger redeploy)

Now, in your Vercel api/ask.ts file, you can access the secret like this:

const token = process.env.GITHUB_TOKEN;

5. Optional Test API Route

https://your-vercel-project.vercel.app/api/ask?test=true


⚠️ Notes:

Environment variables are not exposed to the browser (safe).

Never log the token to console.log() or return it in the response.

You can also create secrets from CLI using vercel env add if needed.

Add a test endpoint under api/ask.ts and deploy to confirm secrets are working securely.

## To run in local
in nodejs command prompt

set GITHUB_TOKEN=<your-github-token-goes-here>

running node command if error:

UNABLE_TO_GET_ISSUER_CERT_LOCALLY

set NODE_TLS_REJECT_UNAUTHORIZED=0

on asking question every time, run

node sample.js  (may throw some warning)  , or

node --experimental-modules sample.js (may throw some warning)

## to run python projects in local
in windows command prompt

raw REST API calls to https://models.github.ai/inference.

python installed

python --version

3.13.3

pip list

it shows all : installed packages

manually downloaded it from python.org

to run:

python python_projects/main.py

python python_projects/multi_turn_chat.py

streamlit run python_projects/chat_ui.py

python python_projects/app.py

python python_projects/hello_world.py

python python_projects/calculator.py

pip install azure-ai-inference  (install it may be future code)

python -m tkinter

.post(,verify='False')
## using Azure's GPT-4.1 via GitHub's AI endpoint
(https://models.github.ai/inference) — not OpenAI's API directly 

not through https://platform.openai.com/

OPENAI_API_KEY -> GITHUB_AI_TOKEN

https://api.openai.com/v1/chat/completions


## Streamlit
web-based chatbot UI using Streamlit. This will let you interact with the GitHub-hosted LLM right from your browser.

pip install streamlit requests

streamlit run python_projects/chat_ui.py

Local URL: http://localhost:8501

Features:

Keeps chat history

Token input box (only shown if env var not set)

Nice browser interface

Uses st.chat_message for a modern look

In Streamlit:

Python is making the API request directly from the server (no browser involved).

All API calls (to https://models.github.ai/inference) are made from the Python backend, not from the browser UI.

## Streamlit App Flow Recap

You type a message in the chat box (st.chat_input()).

Streamlit Python code (server-side) receives that message.

Python sends the request:

response = requests.post(endpoint, headers=headers, json=body)

Streamlit then renders the response HTML back to the browser.

So the browser never touches https://models.github.ai/ directly.

Streamlit always had the token already in Python (in a variable)

## HTML + Flask-based chatbot

👨🎨 Frontend: templates/index.html

🧠 Backend (LLM logic): app.py

This gives you full control and is ideal if you're building a web app beyond just a chatbot.

pip install flask requests

python python_projects/app.py

✅ Accepts a token from the UI

✅ Sends it properly in the request

✅ Prevents the 401 Unauthorized error

✅ Maintains chat history in-memory


Enter a valid GitHub token in the password field and start chatting!


The browser sends a POST to /chat, and Flask receives it.

https://llm-chatbot-md85.onrender.com/

https://movie-recommender-flask-iwcb.onrender.com/

## requirements.txt
pip install -r requirements.txt

TL;DR

requirements.txt → Only dependencies, plain text

package.json → Dependencies + metadata + scripts, in JSON

pyproject.toml (modern Python projects)

It's like the next-gen package.json for Python, used by poetry, pdm, or pip.

## openAI status
https://status.openai.com/

https://platform.openai.com/docs/models

https://community.openai.com/

https://downdetector.in/status/openai/

https://github.com/marketplace?type=models

## vercel.json

vercel.json is a configuration file used to customize your Vercel project. You can use it to:

Define custom routes or rewrites

Set a default file (index.html)

Redirect traffic

Override build settings

Specify regions, env variables, etc.