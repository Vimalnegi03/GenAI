from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GOOGLE_GEMINI_API_KEY")
print(api_key)
client =genai.Client(api_key=api_key)
resposne=client.models.generate_content(
    model='gemini-2.0-flash-001',
    contents="why the sky is blue"
)
print(resposne.text)