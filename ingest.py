
from pathlib import Path

from ollama import embed
from qdrant_client.models import (
    PointStruct,
    VectorParams,
    Distance
)

from qdrant_store import get_qdrant_client


# -------------------------
# Settings
# -------------------------

KNOWLEDGE_DIR = Path("knowledge")

COLLECTION_NAME = "knowledge"

EMBED_MODEL = "nomic-embed-text"

CHUNK_SIZE = 800
CHUNK_OVERLAP = 100

BATCH_SIZE = 50


# -------------------------
# Read knowledge files
# -------------------------

def load_documents():

    if not KNOWLEDGE_DIR.exists():
        raise FileNotFoundError(
            f"Knowledge directory not found: {KNOWLEDGE_DIR}"
        )

    documents = []

    for file in KNOWLEDGE_DIR.rglob("*.md"):

        text = file.read_text(encoding="utf-8")

        if text.strip():

            documents.append({
                "source": str(file),
                "text": text
            })

    return documents


# -------------------------
# Split text into chunks
# -------------------------

def chunk_text(text):

    text = text.strip()

    if not text:
        return []

    chunks = []

    start = 0

    while start < len(text):

        end = start + CHUNK_SIZE

        # Avoid cutting words when possible
        if end < len(text):

            split_position = text.rfind(" ", start, end)

            if split_position > start:
                end = split_position

        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        # Move forward while maintaining overlap
        start = end - CHUNK_OVERLAP

        if start <= 0:
            start = end

    return chunks


# -------------------------
# Create collection
# -------------------------

def create_collection():

    client = get_qdrant_client()

    if client.collection_exists(COLLECTION_NAME):

        print("Collection already exists.")

        return

    # Detect actual embedding dimension
    test_embedding = get_embedding("test")

    vector_size = len(test_embedding)

    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=vector_size,
            distance=Distance.COSINE
        )
    )

    print(
        f"Collection created with vector size: {vector_size}"
    )


# -------------------------
# Create embeddings
# -------------------------

def get_embedding(text):

    result = embed(
        model=EMBED_MODEL,
        input=text
    )

    return result["embeddings"][0]


# -------------------------
# Index knowledge
# -------------------------

def index_knowledge():

    documents = load_documents()

    print("Documents found:", len(documents))

    client = get_qdrant_client()

    point_id = 1
    batch = []

    for document in documents:

        chunks = chunk_text(document["text"])

        print(
            f"{document['source']} -> "
            f"{len(chunks)} chunks"
        )

        for chunk_index, chunk in enumerate(chunks):

            vector = get_embedding(chunk)

            batch.append(
                PointStruct(
                    id=point_id,
                    vector=vector,
                    payload={
                        "text": chunk,
                        "source": document["source"],
                        "chunk_index": chunk_index
                    }
                )
            )

            point_id += 1

            # Upload in batches
            if len(batch) >= BATCH_SIZE:

                client.upsert(
                    collection_name=COLLECTION_NAME,
                    points=batch
                )

                print(f"Uploaded {len(batch)} points")

                batch.clear()

    # Upload remaining points
    if batch:

        client.upsert(
            collection_name=COLLECTION_NAME,
            points=batch
        )

        print(f"Uploaded {len(batch)} remaining points")

    print("Knowledge indexing complete.")


# -------------------------
# Run
# -------------------------

if __name__ == "__main__":

    create_collection()

    index_knowledge()
