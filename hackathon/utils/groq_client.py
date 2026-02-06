import os
import json
from groq import Groq

def get_groq_client():
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        # Fallback for hackathon demo purposes if env var is missing, though prompt says "No hardcoded API keys"
        # We will assume the user has set it or will set it. 
        # Raising specific error to be handled by app.py
        raise ValueError("GROQ_API_KEY environment variable not set")
    return Groq(api_key=api_key)

def generate_completion(prompt, model="llama-3.3-70b-versatile", json_mode=False):
    """
    Generates completion from Groq API.
    If json_mode is True, attempts to parse the response as JSON.
    """
    try:
        client = get_groq_client()
        
        response_format = {"type": "json_object"} if json_mode else None
        
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model=model,
            response_format=response_format
        )
        
        content = chat_completion.choices[0].message.content
        
        if json_mode:
            try:
                return json.loads(content)
            except json.JSONDecodeError:
                # Fallback if model didn't return perfect JSON
                return {"error": "Failed to parse JSON response from AI", "raw_content": content}
                
        return content
        
    except Exception as e:
        raise e
