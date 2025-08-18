import os
from openai import OpenAI
from flask import current_app

def generate_response(user_message):
    # Create OpenAI client with API key
    client = OpenAI(api_key=current_app.config['OPENAI_API_KEY'])

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Use gpt-4 if you gain access later
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant for teachers. Your tone is professional and friendly."},
                {"role": "user", "content": user_message}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"
