from app.core.database import Database

class IntentService:
    @classmethod
    async def get_intents(cls):
        await Database.connect()
        return await Database.fetch_compliance_rules()

    @classmethod
    async def get_ml_intent_classification(cls):
        await Database.connect()
        return await Database.fetch_compliance_rules()
    
    @classmethod
    async def get_llm_intent_classification(cls):
        await Database.connect()
        return await Database.fetch_compliance_rules()