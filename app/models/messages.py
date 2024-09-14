# app/models/messages.py
from pydantic import BaseModel, Field
from typing import List, Optional

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

class RealTimeMessageResponse(BaseModel):
    user_message: str
    document_uploaded: bool
    match_count: int
    matches: List[dict]
    rules: List[dict]