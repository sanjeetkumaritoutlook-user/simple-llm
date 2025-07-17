from transformers import pipeline

# Load a sentiment-analysis pipeline
classifier = pipeline("sentiment-analysis")

# Use it
result = classifier("I love Hugging Face!")
print(result)
