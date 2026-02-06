def get_campaign_prompt(product, audience, platform):
    return f"""
    Act as a world-class marketing strategist. Create a comprehensive marketing campaign for the following:
    
    Product: {product}
    Target Audience: {audience}
    Platform: {platform}
    
    Provide the output in the following structure:
    1. Campaign Objective: A clear, measurable goal.
    2. Content Ideas: 5 creative content ideas tailored to the platform.
    3. Ad Copy Variations: 3 distinct ad copies (Headline + Body).
    4. CTA Suggestions: 3 compelling calls to action.
    
    Keep the tone professional yet engaging.
    """

def get_sales_pitch_prompt(product, persona):
    return f"""
    Act as a top-tier sales expert. Generate a persuasive sales pitch for:
    
    Product/Service: {product}
    Customer Persona: {persona}
    
    Provide the output in the following structure:
    1. Elevator Pitch (30 seconds): Concise and punchy.
    2. Key Value Proposition: The main benefit.
    3. Key Differentiators: What makes it unique.
    4. Call to Action: A clear next step.
    """

def get_lead_scoring_prompt(lead_name, budget, need, urgency):
    return f"""
    Act as an AI Lead Scoring Agent. Analyze the following lead and assign a score from 0 to 100.
    
    Lead Name: {lead_name}
    Budget: {budget}
    Need: {need}
    Urgency: {urgency}
    
    You MUST return the output in valid JSON format ONLY, with no extra text or markdown code blocks.
    The JSON structure should be:
    {{
        "score": <number 0-100>,
        "reasoning": "<explanation of the score>",
        "conversion_probability": "<percentage>"
    }}
    """
