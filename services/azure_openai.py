from openai import AzureOpenAI
from config import Config
from logger import verbose_logger


class AzureOpenAIClient:
    def __init__(self, conf: Config):
        self.__azure_openai_client = AzureOpenAI(
            api_key=conf.AZURE_OPENAI_KEY,
            api_version=conf.AZURE_OPENAPI_VERSION,
            azure_endpoint=conf.AZURE_OPENAI_ENDPOINT,
        )
        self.__conf = conf

    def generate_embeddings(self, text: str):
        is_success = True
        try:
            response = self.__azure_openai_client.embeddings.create(
                input=text, model=self.__conf.EMBEDDING_ENGINE
            )
            embeddings = response.model_dump()
            verbose_logger.debug("Succesffully generate embeddings")
            return is_success, embeddings["data"][0]["embedding"]
        except Exception as e:
            verbose_logger.error(f"Failed to generate embeddings: {e}")
            is_success = False
            return is_success, None

    def chat(self, messages: list):
        try:
            response = self.__azure_openai_client.chat.completions.create(
                model=self.__conf.GPT_ENGINE, messages=messages, temperature=0.7
            )
            verbose_logger.debug("Succesffully response")
            return response.choices[0].message.content
        except Exception as e:
            verbose_logger.error(f"Failed to response: {e}")
            return ""
