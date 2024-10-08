from datetime import datetime
from pydantic import BaseModel

class ChatMessage(BaseModel):
    id: int
    sess_id: str
    emp_id: str
    message_id: int
    input: str
    timestamp: datetime
    feedback_rating: str
    output: str
    chat_type: str

    def to_custom_dict(self):
        serialize = lambda v: v.isoformat() if isinstance(v, datetime) else v
        return {key: serialize(value) for key, value in self.model_dump().items()}
    
class Rule(BaseModel):
    id: int
    created_at: datetime
    active: bool
    rule: str

    def to_custom_dict(self):
        serialize = lambda v: v.isoformat() if isinstance(v, datetime) else v
        return {key: serialize(value) for key, value in self.model_dump().items()}