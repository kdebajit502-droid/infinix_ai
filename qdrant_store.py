from qdrant_client import QdrantClient

QDRANT_PATH = "qdrant_data"

_client = None


def get_qdrant_client():
    global _client

    if _client is None:
        try:
            _client = QdrantClient(path=QDRANT_PATH)
        except RuntimeError as error:
            raise RuntimeError(
                "The Qdrant folder qdrant_data is already in use. "
                "Stop the other running python process (another main.py "
                "or ingest.py), then start the app again."
            ) from error

    return _client
