import os
from pinecone import Pinecone, ServerlessSpec
from sentence_transformers import SentenceTransformer

# === Step 1: Load a Hugging Face embedding model , not openai embedding model===  
# https://huggingface.co/models?sort=trending&search=bge-small-en
model = SentenceTransformer("BAAI/bge-small-en")

# === Step 2: Setup Pinecone ===
api_key = "pinecone key"
pc = Pinecone(api_key=api_key)

index_name = "demo-index"
dimension = 384  # dimension of BAAI/bge-small-en

# Only create the index if it doesn't exist
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=dimension,
        metric="cosine",  # or "dotproduct"
        spec=ServerlessSpec(
            cloud="aws",       # or "gcp"
            region="us-east-1" # or your preferred region
        )
    )

# Connect to the index
index = pc.Index(index_name)

# === Step 3: Embed and upsert data ===
texts = ["The Eiffel Tower is in Paris", "The Great Wall is in China"]
embeddings = model.encode(texts).tolist()

print(f"Embedding dimension: {len(embeddings[0])}")


vectors = [
    {"id": f"item-{i}", "values": embeddings[i], "metadata": {"text": texts[i]}}
    for i in range(len(texts))
]

index.upsert(vectors=vectors)

print(f"Upserted {len(vectors)} vectors")


# === Step 4: Query with a new sentence ===
query = "Where is the Eiffel Tower?"
query_embedding = model.encode([query])[0].tolist()

result = index.query(vector=query_embedding, top_k=2, include_metadata=True)

print(result)

print("Query Results:")
for match in result['matches']:
    print(f"{match['score']:.2f} => {match['metadata']['text']}")
