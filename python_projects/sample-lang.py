from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os

# Set your API key here if not set in environment
os.environ["OPENAI_API_KEY"] = "your-api-key-here"

# Initialize LLM
llm = OpenAI()

# Prompt template
prompt = PromptTemplate.from_template("Translate this to French: {text}")

# Create chain
chain = LLMChain(llm=llm, prompt=prompt)

# Run the chain
result = chain.run("Hello, how are you?")
print(result)
