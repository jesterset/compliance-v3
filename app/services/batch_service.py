# app/services/batch_service.py
from app.core.database import Database
from app.core.elastic import ElasticClient
from app.utils.file_utils import save_to_csv
from app.services.compliance_service import ComplianceService

class BatchService:
    @classmethod
    async def fetch_chat_messages(cls):
        query = "SELECT * FROM chat_messages"
        return await Database._connection.fetch(query)

    @classmethod
    async def process_batch(cls):
        messages = await cls.fetch_chat_messages()
        compliance_rules = await ComplianceService.get_rules()
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
                "rules": compliance_rules
            }
            results.append(result)

        # Save results to CSV
        await save_to_csv(results)

        return results