from pydantic import BaseModel
from typing import Dict, Union

class GenerateRequest(BaseModel):
    product_name: str
    target_audience: str
    format: str = "AIDA"  

class GenerateResponse(BaseModel):
    copy: Union[str, Dict[str, str]]
    rationale: str
