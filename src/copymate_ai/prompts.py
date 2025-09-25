import json

def generate_aida_prompt(product_details: dict) -> str:
    """
    Generates an AIDA prompt instructing LLM to return JSON with copy + rationale.
    """
    product_name = product_details.get("productName", "Unknown Product")
    target_audience = product_details.get("targetAudience", "General Audience")

    return f"""
You are an expert marketing copywriter.

Write a marketing copy using the AIDA framework (Attention, Interest, Desire, Action).

Product: {product_name}
Target Audience: {target_audience}

Return the result as a JSON object with keys:
- "copy": The AIDA copy.
- "rationale": Short explanation of why it works.
""".strip()


def generate_pas_prompt(product_details: dict) -> str:
    """
    Generates a PAS prompt instructing LLM to return JSON with copy + rationale.
    """
    product_name = product_details.get("productName", "Unknown Product")
    target_audience = product_details.get("targetAudience", "General Audience")

    return f"""
You are an expert marketing copywriter.

Write a marketing copy using the PAS framework (Problem, Agitation, Solution).

Product: {product_name}
Target Audience: {target_audience}

Return the result as a JSON object with keys:
- "copy": The PAS copy.
- "rationale": Short explanation of why it works.
""".strip()


def generate_format_prompt(product_details: dict, copy_format: str) -> str:
    """
    Generates a prompt for ad, email, or social media copy.
    """
    product_name = product_details.get("productName", "Unknown Product")
    target_audience = product_details.get("targetAudience", "General Audience")

    format_instructions = {
        "ad": "Generate a short, punchy, attention-grabbing ad copy.",
        "email": "Generate a professional, persuasive email for the target audience.",
        "social_media": "Generate a concise, engaging, and shareable social media post."
    }

    instruction = format_instructions.get(copy_format.lower(), "Generate a marketing copy.")

    return f"""
You are an expert marketing copywriter.

Product: {product_name}
Target Audience: {target_audience}

{instruction}

Return the result as a JSON object with keys:
- "copy": The generated copy.
- "rationale": Short explanation of why it works.
""".strip()


def parse_ai_response(response_text: str) -> dict:
    """
    Safely parse JSON returned from AI.
    """
    try:
        return json.loads(response_text)
    except json.JSONDecodeError:
        return {"error": "Invalid JSON returned by AI", "raw": response_text}
