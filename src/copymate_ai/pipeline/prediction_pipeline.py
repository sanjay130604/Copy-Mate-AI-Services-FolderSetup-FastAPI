from src.copymate_ai.prompts import (
    generate_aida_prompt,
    generate_pas_prompt,
    generate_format_prompt,
    parse_ai_response
)

def generate_copy_pipeline(product_name: str, target_audience: str, copy_format: str = "AIDA") -> dict:
    """
    Simulates the AI pipeline for generating marketing copy.
    In future, replace `fake_ai_response` with real LLM call.
    """

    product_details = {
        "productName": product_name,
        "targetAudience": target_audience
    }

    fmt = copy_format.upper()

    if fmt == "AIDA":
        prompt = generate_aida_prompt(product_details)
    elif fmt == "PAS":
        prompt = generate_pas_prompt(product_details)
    elif fmt in ["AD", "EMAIL", "SOCIAL", "SOCIAL_MEDIA"]:
        prompt = generate_format_prompt(product_details, fmt.lower())
    else:
        return {
            "copy": "Invalid format",
            "rationale": "Choose one of: AIDA, PAS, AD, EMAIL, SOCIAL_MEDIA."
        }

    fake_ai_response = """
    {
        "copy": "This is a sample copy demonstrating the {fmt} format.",
        "rationale": "Shows how the copy style adapts to the requested format."
    }
    """.replace("{fmt}", fmt)

    parsed = parse_ai_response(fake_ai_response)
    return parsed
