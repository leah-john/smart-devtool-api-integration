from pydantic import BaseModel


class AnalyzeRequest(BaseModel):
    url: str
    use_case: str