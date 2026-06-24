import json

def export_chunks_to_json(chunks, filename="chunks_export.json"):
    export_data = []
    
    for i, doc in enumerate(chunks):
        original_content = json.loads(doc.metadata.get("original_content", "{}"))

        chunk_data = {
            "chunk_id": i + 1,
            "enhanced_content": doc.page_content,
            "metadata": {
                "raw_text": original_content.get("raw_text", ""),
                "tables_html": original_content.get("tables_html", []),
                "images_base64": original_content.get("images_base64", []),
            }
        }
        export_data.append(chunk_data)
    
    # Save to file
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(export_data, f, indent=2, ensure_ascii=False)
    
    print(f"Exported {len(export_data)} chunks to {filename}")
    return export_data