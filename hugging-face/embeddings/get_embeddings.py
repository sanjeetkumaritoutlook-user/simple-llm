from transformers import AutoTokenizer, AutoModel
import torch

# 1. Define model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")

# 2. Input text
text = "Hugging Face is awesome!"

# 3. Tokenize and run the model
inputs = tokenizer(text, return_tensors="pt")
with torch.no_grad():
    outputs = model(**inputs)

# 4. Get embeddings (last hidden state)
embeddings = outputs.last_hidden_state

# 5. Print shape and values
print("Shape:", embeddings.shape)
print("Embeddings:", embeddings)
