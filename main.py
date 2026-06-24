from ingestion.chunk_loader import *
from pipelines.ingestion import *
from embeddings.vector_store import create_supabase_client, get_vector_store, upload_vector_store
from dotenv import load_dotenv
# from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from retrieval_and_answer.retrieve_chunks import *
from retrieval_and_answer.generate_answer import *

import json

load_dotenv()

embeddings = OllamaEmbeddings(
    model='nomic-embed-text'
)
client = create_supabase_client()

# ingestion_pipeline("NASDAQ_AAPL_2025.pdf", embeddings, client)

# query = "How many full-time equivalent employees did Apple have as of September 27, 2025?"
query2 = "What was the average price paid per share during each monthly repurchase period in Q4 2025?"
vector_store = get_vector_store(embeddings, client=client)
# vector_store = upload_vector_store(docs, embeddings, client=client)

chunks = retrieve_chunks(query2, vector_store)
export_chunks_to_json(chunks)

context = retrieve_context_from_chunks(chunks)

print(generate_final_answer(chunks, query2, json, use_local=True))
# print(context)