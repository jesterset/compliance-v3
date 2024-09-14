# app/services/compliance_service.py
from app.core.database import Database

class ComplianceService:
    @classmethod
    async def get_rules(cls):
        return await Database.fetch_compliance_rules()