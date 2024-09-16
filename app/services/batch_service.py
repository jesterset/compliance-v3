from app.core.database import Database
from app.core.elastic import ElasticClient
from app.services.compliance_service import ComplianceService

class BatchService:
    @classmethod
    async def fetch_chat_messages(cls):
        await Database.connect()
        return await Database.fetch_chat_messages()

    @classmethod
    async def process_batch_messages(cls):
        messages = await cls.fetch_chat_messages()
        rules = await ComplianceService.get_rules()
        results = []

        for message in messages:
            # Match input against Elasticsearch sanitization terms
            elastic_results = await ElasticClient.search_terms('regex_rules_index', message['input'])
            matched_terms = [hit['_source'] for hit in elastic_results['hits']['hits']]

            # Format result
            result = {
                "input": message['input'],
                "chat_type": message['chat_type'],
                "match_count": len(matched_terms),
                "matches": matched_terms,
                "rules": rules
            }

            results.append(result)

        return results