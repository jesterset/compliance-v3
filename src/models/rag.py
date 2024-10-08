from pydantic import BaseModel

class DocumentMetadata(BaseModel):
    path: str = "no-path"
    name: str = "doc"
    workspace: str
    rag_embed_index: str
    rag_raw_index: str