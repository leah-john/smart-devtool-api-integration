from sentence_transformers import SentenceTransformer
import chromadb


model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(
    path="backend/app/rag/chroma_db"
)

collection = client.get_collection(
    name="api_docs"
)


def retrieve_relevant_chunks(query, n_results=2):

    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    return results["documents"][0]