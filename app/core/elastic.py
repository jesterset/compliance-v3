from elasticsearch import AsyncElasticsearch
from app.core.config import Config

class ElasticClient:
    _client = None

    @classmethod
    def get_client(cls):
        """
        Returns the Elasticsearch client instance.

        If the client instance does not exist, it creates a new instance using the Elasticsearch URL
        specified in the Config class.

        Returns:
            AsyncElasticsearch: The Elasticsearch client instance.

        """
        if not cls._client:
            cls._client = AsyncElasticsearch([Config.ELASTICSEARCH_URL])
        return cls._client

    @classmethod
    async def search_terms(cls, index_name, user_message):
        """
        Search for terms in the specified index based on the user's message.

        Args:
            cls (class): The class itself.
            index_name (str): The name of the index to search in.
            user_message (str): The user's message to search for.

        Returns:
            dict: The search results.

        """
        query = {
            "query": {
                "multi_match": {
                    "query": user_message,
                    "fields": [
                        "sanitiztion_term^3",
                        "sanitiztion_term.synonym^2",
                        "sanitiztion_term.stemmed",
                    ],
                    "fuzziness": "AUTO",
                }
            }
        }
        return await cls._client.search(index=index_name, body=query)