
import re

from ollama import embed

from qdrant_store import get_qdrant_client


# =====================================
# SETTINGS
# =====================================

MIN_SCORE = 0.60

COLLECTION_NAME = "knowledge"

EMBED_MODEL = "nomic-embed-text"

DEFAULT_LIMIT = 10

DEFAULT_MAX_RESULTS = 3


STOP_WORDS = {
    "what", "is", "are", "the",
    "a", "an", "how", "why",
    "does", "do", "of", "to",
    "in", "on", "for", "and",
    "or", "with", "can", "i",
    "it", "this", "that", "was",
    "were", "be", "been", "being",
    "have", "has", "had", "will",
    "would", "could", "should",
    "my", "your", "their", "from",
    "about", "explain", "tell"
}


# =====================================
# EMBEDDINGS
# =====================================

def get_embedding(text):

    result = embed(
        model=EMBED_MODEL,
        input=text
    )

    embeddings = result.get("embeddings")

    if not embeddings:
        raise ValueError("Embedding generation failed.")

    return embeddings[0]


# =====================================
# KEYWORD EXTRACTION
# =====================================

def get_keywords(text):

    words = re.findall(
        r"\b[a-zA-Z0-9]+\b",
        text.lower()
    )

    return {
        word
        for word in words
        if word not in STOP_WORDS
        and len(word) > 2
    }


# =====================================
# KEYWORD SCORE
# =====================================

def keyword_score(question, text):

    question_keywords = get_keywords(question)

    text_keywords = get_keywords(text)

    if not question_keywords:
        return 0.0

    matches = question_keywords.intersection(
        text_keywords
    )

    return len(matches) / len(question_keywords)


# =====================================
# HYBRID SEARCH
# =====================================

def search_knowledge(
    question,
    limit=DEFAULT_LIMIT,
    max_results=DEFAULT_MAX_RESULTS
):

    question = question.strip()

    if not question:
        return []


    # 1. Generate question embedding

    question_vector = get_embedding(question)


    # 2. Retrieve candidates from Qdrant

    client = get_qdrant_client()

    response = client.query_points(
        collection_name=COLLECTION_NAME,
        query=question_vector,
        limit=limit,
        with_payload=True
    )

    results = response.points


    # 3. Rank candidates

    ranked_results = []

    seen_chunks = set()

    for result in results:

        payload = result.payload or {}

        text = payload.get("text")

        source = payload.get("source")

        if not text or not source:
            continue


        # Avoid duplicate chunks

        if text in seen_chunks:
            continue

        seen_chunks.add(text)


        # Semantic similarity

        semantic_score = result.score


        # Keyword similarity

        keyword_match = keyword_score(
            question,
            text
        )


        # Combined score

        final_score = (
            semantic_score * 0.8
            +
            keyword_match * 0.2
        )


        # Filter weak results

        if final_score < MIN_SCORE:
            continue


        ranked_results.append({

            "text": text,

            "source": source,

            "semantic_score": semantic_score,

            "keyword_score": keyword_match,

            "score": final_score

        })


    # 4. Sort by relevance

    ranked_results.sort(
        key=lambda item: item["score"],
        reverse=True
    )


    # 5. Return best results

    return ranked_results[:max_results]


# =====================================
# TEST
# =====================================

if __name__ == "__main__":

    question = input("Question: ")

    try:

        results = search_knowledge(question)

        print("\nResults:\n")

        if not results:

            print("No relevant knowledge found.")

        for result in results:

            print("Final Score:", round(result["score"], 3))

            print("Semantic Score:", round(result["semantic_score"], 3))

            print("Keyword Score:", round(result["keyword_score"], 3))

            print("Source:", result["source"])

            print("Text:")

            print(result["text"])

            print("-" * 50)


    except Exception as error:

        print("Search failed:", error)
