from pydantic import BaseModel

class ParserMessage(BaseModel):
    message_id: str
    label: str
    parser_model_name: str

class ValuedMessage(BaseModel):
    message_id: str
    value_CAD: float | None
    time_saved_seconds: float | None
    valuation_nodel: str
