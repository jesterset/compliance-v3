# app/services/compliance_service.py
from app.core.database import Database

class ComplianceService:
    @classmethod
    async def get_rules(cls):
        print("there")
        await Database.connect()
        result = await Database.fetch_compliance_rules()
        print("result ", result)
        return result