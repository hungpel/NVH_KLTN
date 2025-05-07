from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
from app.models import Document

model = SentenceTransformer("all-MiniLM-L6-v2")

def search_documents(query, top_k=10):
    documents = list(Document.objects.select_related('subject').all())

    # Kết hợp name + subject.name + description
    document_texts = [
        f"{doc.name} {doc.subject.name if doc.subject else ''} {doc.description}"
        for doc in documents
    ]

    embeddings = model.encode(document_texts, show_progress_bar=False)

    index = faiss.IndexFlatL2(embeddings[0].shape[0])
    index.add(np.array(embeddings))

    query_embedding = model.encode([query])
    D, I = index.search(np.array(query_embedding), top_k)

    return [documents[i] for i in I[0] if i < len(documents)]

def get_related_documents(document, top_k=5):
    documents = list(Document.objects.exclude(id=document.id).select_related('subject'))

    document_texts = [
        f"{doc.name} {doc.subject.name if doc.subject else ''} {doc.description}"
        for doc in documents
    ]
    embeddings = model.encode(document_texts, show_progress_bar=False)

    query_text = f"{document.name} {document.subject.name if document.subject else ''} {document.description}"
    query_embedding = model.encode([query_text])

    index = faiss.IndexFlatL2(embeddings[0].shape[0])
    index.add(np.array(embeddings))
    D, I = index.search(np.array(query_embedding), top_k)

    return [documents[i] for i in I[0] if i < len(documents)]
