from datetime import datetime
from pydantic import BaseModel
from typing import Any, Dict, List, Optional

class DocumentMetadata(BaseModel):
    path: str = "no-path"
    name: str = "doc"
    workspace: str
    rag_embed_index: str
    rag_raw_index: str

class RealTimeMessageRequest(BaseModel):
    user_message: str
    document_uploaded: bool
    document_metadata: Optional[DocumentMetadata]

class Rule(BaseModel):
    id: int
    created_at: datetime
    active: bool
    rule: str

    def to_custom_dict(self):
        serialize = lambda v: v.isoformat() if isinstance(v, datetime) else v
        return {key: serialize(value) for key, value in self.model_dump().items()}

class RealTimeMessageResponse(BaseModel):
    user_message: str
    document_uploaded: bool
    match_count: int
    matches: List[dict]
    rules: List[Rule]

    def to_custom_dict(self) -> Dict[str, Any]:
        data = self.model_dump()
        data['rules'] = [rule.to_custom_dict() for rule in self.rules]
        return data

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


class BatchMessageResponse(BaseModel):
    input: str
    chat_type: str
    match_count: int
    matches: List[dict]
    rules: List[Rule]

    def to_custom_dict(self) -> Dict[str, Any]:
        data = self.model_dump()
        data['rules'] = [rule.to_custom_dict() for rule in self.rules]
        return data