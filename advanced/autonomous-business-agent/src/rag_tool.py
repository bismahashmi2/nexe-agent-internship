from retrieve import query_engine

def rag_query(question):

    results = query_engine(question)

    context = "\n\n".join(results)

    return context