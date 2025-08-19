import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
model_name = os.getenv("MODEL_NAME")

genai.configure(api_key=api_key)

prompt = """
You are a 5th-grade science teachers assistant. You like to keep a professional setting while still being approchable. You are teaching a class on Astronomy tommorrow, please generate:
1.  Three engaging in-class activities.
2.  Five practice questions with their corresponding answers.
"""

model = genai.GenerativeModel(model_name)
response = model.generate_content([prompt])
print(response.text)