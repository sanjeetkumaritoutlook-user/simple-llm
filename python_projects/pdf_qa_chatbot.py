import os
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from dotenv import load_dotenv

# Load OpenAI key
load_dotenv()
openai_key = os.getenv("GITHUB_TOKEN")

if not openai_key:
    raise ValueError("GITHUB_TOKEN not found. Set it in .env or environment.")

# Load PDF
pdf_path = "your-file.pdf"  # Replace with your file
loader = PyPDFLoader(pdf_path)
documents = loader.load()

# Split PDF text
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
docs = text_splitter.split_documents(documents)

# Create embeddings
embeddings = OpenAIEmbeddings(openai_api_key=openai_key)

# Store in FAISS vector DB
db = FAISS.from_documents(docs, embeddings)

# Create retriever
retriever = db.as_retriever()

# Set up LLM
llm = ChatOpenAI(openai_api_key=openai_key, temperature=0)

# Create QA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True
)

# User interaction loop
print("🔍 Ask questions about the PDF (type 'exit' to quit):")
while True:
    query = input("\n❓ Your question: ")
    if query.lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break
    result = qa_chain({"query": query})
    print("\n💬 Answer:", result["result"])
