from ingestion.test_ingestion import test_full_pipeline_with_real_pdf
from ingestion.chunk_loader import *
from embeddings.vector_store import *
from dotenv import load_dotenv
# from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

load_dotenv()

embeddings = OllamaEmbeddings(
    model='nomic-embed-text'
)

# test_full_pipeline_with_real_pdf("NASDAQ_AAPL_2025.pdf", True)
docs = load_chunks_from_json("output.json", True)
client = create_supabase_client()

query = ""
vector_store = get_vector_store(embeddings, client=client)
