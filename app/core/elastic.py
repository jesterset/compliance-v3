from elasticsearch import AsyncElasticsearch
from app.core.config import get_config

# print("Hello from elastic.py >>>>", config)
class ElasticClient:
    _client: AsyncElasticsearch | None = None

    @classmethod
    async def connect(cls):
        """
        Creates an instance of the Elasticsearch client using the configuration
        details from the loaded environment variables.

        Returns:
            None
        """
        if cls._client is None:
            config = get_config()  # Get the configuration lazily
            print("Hello from elastic.py >>>>", config)
            cls._client = AsyncElasticsearch(
                hosts=[config.elastic.host],
                basic_auth=(config.elastic.username, config.elastic.password)
            )

    @classmethod
    async def close(cls):
        """
        Closes the Elasticsearch client connection if it exists.

        Returns:
            None
        """
        if cls._client:
            await cls._client.close()
            cls._client = None

    @classmethod
    async def search_terms(cls, index_name: str, user_message: str) -> dict:
        """
        Search for terms in the specified index based on the user's message.

        Args:
            index_name (str): The name of the index to search in.
            user_message (str): The user's message to search for.

        Returns:
            dict: The search results.
        """
        await cls.connect()  # Ensure the client is connected
        query = {
            "query": {
                "multi_match": {
                    "query": user_message,
                    "fields": ["sanitization_term"],
                    "operator": "or",
                    "fuzziness": "AUTO"
                }
            }
        }
        return await cls._client.search(index=index_name, body=query)
