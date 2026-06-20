from ingestion import loader
from ingestion.chunker_and_summarizer import *
from embeddings.vector_store import *

def ingestion_pipeline(file_path):
    partitioned = loader(file_path)

    chunks_by_title = create_chunks_by_title(partitioned)

    summarized = summarise_chunks(chunks_by_title)

    vector_store = create_vector_store(summarized, "dbv2/chroma_db")

    return vector_store
