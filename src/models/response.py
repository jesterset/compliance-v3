from datetime import datetime
from pydantic import BaseModel
from typing import Any, Dict, List

from app.models.messages import Rule

class RealTimeMessageResponse(BaseModel):
    emp_id: str
    user_message: str
    document_uploaded: bool
    violation_timestamp: datetime
    match_count: int
    matches: List[dict]
    rules: List[Rule]

    def to_custom_dict(self) -> Dict[str, Any]:
        serialize = lambda v: v.isoformat() if isinstance(v, datetime) else v
        data = self.model_dump()
        data['violation_timestamp'] = serialize(data['violation_timestamp'])
        data['rules'] = [rule.to_custom_dict() for rule in self.rules]
        return data
    
class BatchMessageResponse(BaseModel):
    emp_id: str
    input: str
    chat_type: str
    timestamp: datetime
    match_count: int
    matches: List[dict]
    rules: List[Rule]

    def to_custom_dict(self) -> Dict[str, Any]:
        serialize = lambda v: v.isoformat() if isinstance(v, datetime) else v
        data = self.model_dump()
        data['timestamp'] = serialize(data['timestamp'])
        data['rules'] = [rule.to_custom_dict() for rule in self.rules]
        return data