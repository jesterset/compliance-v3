# app/services/message_service.py
from app.core.elastic import ElasticClient
from app.models.messages import RealTimeMessageRequest
from app.services.compliance_service import ComplianceService

class MessageService:
    @classmethod
    async def process_realtime_message(cls, user_message: RealTimeMessageRequest):
        elastic_results = await ElasticClient.search_terms('regex_rules_index', user_message)
        matched_terms = [hit['_source'] for hit in elastic_results['hits']['hits']]
        rules = await ComplianceService.get_rules()
        return {
            "matches": matched_terms,
            "rules": rules
        }