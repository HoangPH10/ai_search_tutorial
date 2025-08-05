from config import Config
from services.azure_openai import AzureOpenAIClient
from services.azure_ai_search import AzureAISearch
from helper import read_prompt
from logger import verbose_logger


if __name__ == "__main__":
    # Create config and services
    verbose_logger.debug("Create config and services")
    config = Config()
    azure_openai_client = AzureOpenAIClient(config)
    azure_ai_search = AzureAISearch(config)

    # Vectorized user query
    user_query = "What is the review of the creek hotel in Dubai?"
    verbose_logger.debug(f"Vectorized user query: {user_query}")
    is_success, vectorised_user_query = azure_openai_client.generate_embeddings(
        user_query
    )

    if is_success:
        # Search documents related to user query
        verbose_logger.debug("Search documents related to user query")
        is_success, documents = azure_ai_search.search(vectorised_user_query)
        if is_success:
            context = [
                dict(chunk=doc["chunk"], score=doc["@search.score"])
                for doc in documents
            ]

            # Get message chat template
            system_prompt = read_prompt("./system_prompt.st")
            user_prompt = (
                f"The user query is: {user_query} \n The context is: {context}"
            )
            messages = [
                dict(role="system", content=system_prompt),
                dict(role="user", content=user_prompt),
            ]

            # Get result
            verbose_logger.debug("Chat with OpenAI")
            content = azure_openai_client.chat(messages)
            verbose_logger.debug(f"Response: {content}")
