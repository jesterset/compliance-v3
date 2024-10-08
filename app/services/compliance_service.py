from app.core.database import Database

class ComplianceService:
    @classmethod
    async def get_rules(cls):
        await Database.connect()
        return await Database.fetch_compliance_rules()
    
    @classmethod
    async def get_ml_violation_classification(cls):
        await Database.connect()
        return await Database.fetch_compliance_rules()
    
    @classmethod
    async def get_llm_violation_classification(cls):
        await Database.connect()
        return await Database.fetch_compliance_rules()