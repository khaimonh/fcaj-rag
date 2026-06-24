def retrieve_chunks(query, vector_store):
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})

    chunks = retriever.invoke(query)
    return chunks
def retrieve_context_from_chunks(chunks):
    context = ""
    for chunk in chunks:
        # print(chunk)
        context += f"\n--- RETRIEVED CHUNK ---\n" + f"{chunk.page_content}" 

        for table in chunk.metadata.get("tables_html", []):
            context += f"TABLE:{table}"

    message_content = [
        {
            "type": "text",
            "text": context
        }
    ]   

    for chunk in chunks:
        for image in chunk.metadata.get("images_base64", []):
            message_content.append({
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/png;base64,{image}"
                }
            })
    return message_content
    

