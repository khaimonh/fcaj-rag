
from ingestion.chunker_and_summarizer import create_chunks_by_title, summarise_chunks
from ingestion.export_to_json import export_chunks_to_json
from ingestion.loader import partition_document


def test_full_pipeline_with_real_pdf(file_path: str, use_local):
    pdf_path = file_path
    
    elements = partition_document(pdf_path)
    chunks = create_chunks_by_title(elements)
    documents = summarise_chunks(chunks, use_local
    )
    export_chunks_to_json(documents, "output.json")
    
    # Verify output quality
    assert len(documents) > 0
    assert all(len(d.page_content) > 100 for d in documents), "Chunks too short"