import numpy as np
import os
import uuid
from chromadb.api.models.Collection import Collection

base_dir = os.path.dirname(os.path.abspath(__file__))

def normalize(vectors):
    norms = np.linalg.norm(vectors, axis=1, keepdims=True)
    return vectors / norms


def add_embedding_to_collection(collection: Collection, embedding, metadata: list, current_id):
    # current_id = str(uuid.uuid4().hex)
    
    collection.add(
        embeddings=embedding.tolist(),  # ChromaDB espera una lista de embeddings
        metadatas=[metadata],           # Los metadatos asociados al embedding
        ids=[current_id]                # Un identificador único para este embedding
    )
    print(f"Embedding agregado al índice. Total de vectores en el índice: {len(collection.get()['ids'])}")
    return current_id


def search_embedding(collection: Collection, query_embedding, n_results=5, threshold=0.5):
    results = collection.query(
        query_embeddings=[query_embedding],  
        n_results=n_results  
    )

    ids = results['ids'][0]
    metadatas = results['metadatas'][0]
    distances = results['distances'][0]

    # Filtrar solo los resultados con distancia menor al umbral
    filtered_results = [
        (id, metadata, dist)
        for id, metadata, dist in zip(ids, metadatas, distances)
        if dist < threshold
    ]

    return filtered_results

