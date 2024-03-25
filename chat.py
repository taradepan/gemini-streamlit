import google.generativeai as genai
import os
import dotenv

dotenv.load_dotenv()

google_api_key = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=google_api_key)

model = genai.GenerativeModel('gemini-pro')
messages = []
def generate_response(prompt):
    messages.append({"role": "user", "parts": prompt})
    response = model.generate_content(messages)
    messages.append({"role": "model", "parts": [response.text]})
    return response.text
