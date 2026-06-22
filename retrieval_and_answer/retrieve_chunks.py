def retrieve_chunks(query, db):
    retriever = db.as_retriever(search_kwargs={"k": 3})
    chunks = retriever.invoke(query)

    return chunks


