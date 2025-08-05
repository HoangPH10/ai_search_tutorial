from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from config import Config
from logger import verbose_logger


class AzureAISearch:
    def __init__(self, conf: Config):
        self.__search_client = SearchClient(
            endpoint=conf.AZURE_SEARCH_SERVICE_ENDPOINT,
            index_name=conf.AZURE_SEARCH_INDEX_NAME,
            credential=AzureKeyCredential(conf.AZURE_SEARCH_API_KEY),
        )

    def search(self, query_vector):
        is_success = True
        try:
            documents = self.__search_client.search(
                vector_queries=[
                    {
                        "vector": query_vector,
                        "k": 3,
                        "fields": "text_vector",
                        "kind": "vector",
                    }
                ],
                select=["chunk"],
            )
            verbose_logger.debug("Search documents successfully")
        except Exception as e:
            verbose_logger.error(f"Failed to search: {e}")
            is_success, documents = False, []
        return is_success, documents
