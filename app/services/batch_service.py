from app.core.database import Database
from app.services.compliance_service import ComplianceService
from app.utils.message_utils import get_matched_terms

class BatchService:
    @classmethod
    async def fetch_chat_messages(cls):
        await Database.connect()
        return await Database.fetch_chat_messages()

    @classmethod
    async def process_batch_messages(cls):
        chat_messages = await cls.fetch_chat_messages()
        rules = await ComplianceService.get_rules()
        results = []

        for message in chat_messages:
            matched_terms = await get_matched_terms('regex_rules_index', message['input'])
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