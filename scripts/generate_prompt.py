def generate_aida_prompt_with_rationale(product_details: dict) -> str:
    """
    Generates an AIDA (Attention, Interest, Desire, Action) prompt string
    that instructs the LLM to return JSON with 'copy' and 'rationale'.
    """
    product_name = product_details.get("productName", "Unknown Product")
    target_audience = product_details.get("targetAudience", "General Audience")

    prompt = f"""
You are an expert marketing copywriter.

Write a marketing copy using the AIDA framework (Attention, Interest, Desire, Action).

Product: {product_name}
Target Audience: {target_audience}

Return your response in JSON format with two keys:
1. "copy" - the generated marketing copy
2. "rationale" - a short explanation of why this copy works
"""
    return prompt.strip()

if __name__ == "__main__":
    example = {
        "productName": "Running Shoes",
        "targetAudience": "Young fitness enthusiasts"
    }

    result = generate_aida_prompt_with_rationale(example)
    print("=== AIDA Prompt with Rationale ===")
    print(result)
