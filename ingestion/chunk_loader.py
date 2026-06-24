import json
from langchain_core.documents import Document

def load_chunks_from_json(json_path: str, use_local=False):
    with open(json_path, "r", encoding="utf-8") as f:
        rows = json.load(f)

    docs = []
    for row in rows:
        text = (row.get("enhanced_content") or "").strip()
        if not text:
            continue

        md = row.get("metadata") or {}
        original = md.get("original_content") or {}

        docs.append(
            Document(
                page_content=text,
                metadata={
                    "chunk_id": row.get("chunk_id"),
                    "raw_text": original.get("raw_text"),
                    "tables_html": original.get("tables_html", []),
                    "images_base64": original.get("images_base64", [])
                }
            )
        )
    return docs