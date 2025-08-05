import os
from dotenv import load_dotenv

load_dotenv(".env")


class Config:
    """Base configuration class"""

    # Azure OpenAI settings
    AZURE_OPENAI_ENDPOINT = os.environ.get("AZURE_OPENAI_ENDPOINT", None)
    AZURE_OPENAI_KEY = os.environ.get("AZURE_OPENAI_KEY", None)
    AZURE_OPENAPI_VERSION = os.environ.get("AZURE_OPENAPI_VERSION", None)
    EMBEDDING_ENGINE = os.environ.get("EMBEDDING_ENGINE", None)
    GPT_ENGINE = os.environ.get("GPT_ENGINE", None)

    # Azure AI Search
    AZURE_SEARCH_SERVICE_ENDPOINT = os.environ.get(
        "AZURE_SEARCH_SERVICE_ENDPOINT", None
    )
    AZURE_SEARCH_INDEX_NAME = os.environ.get("AZURE_SEARCH_INDEX_NAME", None)
    AZURE_SEARCH_API_KEY = os.environ.get("AZURE_SEARCH_API_KEY", None)
