from fastapi import APIRouter
from pydantic import BaseModel
from typing import Literal, Union, Dict

from src.copymate_ai.prompts import (
    generate_aida_prompt,
    generate_pas_prompt,
    generate_format_prompt,
    parse_ai_response
)

router = APIRouter()

class GenerateRequest(BaseModel):
    product_name: str
    target_audience: str
    format: Literal["AIDA", "PAS", "ad", "email", "social_media"] = "AIDA"


class GenerateResponse(BaseModel):
    copy: Union[str, Dict[str, str]]
    rationale: str

@router.post("/generate", response_model=GenerateResponse, tags=["v1"])
async def generate_copy(request: GenerateRequest):
    """
    Generate marketing copy for multiple formats.
    Uses prompts.py to build prompt templates and simulates AI output.
    """

    fmt = request.format.upper()
    product_details = {
        "productName": request.product_name,
        "targetAudience": request.target_audience
    }

    if fmt == "AIDA":
        prompt = generate_aida_prompt(product_details)
    elif fmt == "PAS":
        prompt = generate_pas_prompt(product_details)
    elif fmt in ["AD", "EMAIL", "SOCIAL", "SOCIAL_MEDIA"]:
        prompt = generate_format_prompt(product_details, fmt.lower())
    else:
        return GenerateResponse(
            copy="Invalid format",
            rationale="Please choose one of: AIDA, PAS, AD, EMAIL, SOCIAL_MEDIA."
        )

    fake_ai_response = """
    {
        "copy": "This is a sample copy demonstrating the {fmt} format.",
        "rationale": "This shows how the copy style adapts to the selected format."
    }
    """.replace("{fmt}", fmt)

    parsed = parse_ai_response(fake_ai_response)

    return GenerateResponse(
        copy=parsed.get("copy", ""),
        rationale=parsed.get("rationale", "")
    )
