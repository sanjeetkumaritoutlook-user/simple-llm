## Github Pages + Vercel
Anyone can see your token in browser dev tools. So, we CANNOT securely use GITHUB_TOKEN (or Azure tokens) in frontend JS directly.

another running app on vercel:

https://space-dashboard-ivory.vercel.app/

Vercel runs your TypeScript API route (api/ask.ts) in a serverless environment, 

and TypeScript doesn’t know about the process object (which is Node-specific) unless you explicitly install the Node types.

npm install --save-dev @types/node

check Vercel project deployment build logs once, as the vercel can still show deployment successful with 500 internal server error

Vercel swallows uncaught exceptions in Serverless Functions and replaces them with a generic 500: FUNCTION_INVOCATION_FAILED,

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



## vercel.json

vercel.json is a configuration file used to customize your Vercel project. You can use it to:

Define custom routes or rewrites

Set a default file (index.html)

Redirect traffic

Override build settings

Specify regions, env variables, etc.