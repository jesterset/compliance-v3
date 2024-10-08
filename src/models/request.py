from pydantic import BaseModel
from typing import Any, Dict, List, Optional
from app.models.messages import DocumentMetadata

class RealTimeMessageRequest(BaseModel):
    emp_id: str
    user_message: str
    document_uploaded: bool
    document_metadata: Optional[DocumentMetadata]