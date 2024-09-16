from elasticsearch import AsyncElasticsearch
from app.core.config import Config

class ElasticClient:
    _client = None

    @classmethod
    def get_client(cls):
        if not cls._client:
            cls._client = AsyncElasticsearch([Config.ELASTICSEARCH_URL])
        return cls._client

    @classmethod
    async def search_terms(cls, index_name, user_message):
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