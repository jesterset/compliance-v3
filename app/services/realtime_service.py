from app.models.messages import RealTimeMessageRequest
from app.services.compliance_service import ComplianceService
from app.utils.elastic_utils import get_matched_terms
from app.core.elastic import ElasticClient

class MessageService:
    @classmethod
    async def process_realtime_message(cls, user_message: RealTimeMessageRequest):
        await ElasticClient.connect()
        matched_terms = await get_matched_terms('regex_rules_index', user_message)

        rules = await ComplianceService.get_rules()
        return {
            "matches": matched_terms,
            "rules": rules
        }