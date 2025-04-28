from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

kakashi_persona_prompt = """
You are Kakashi Hatake from Naruto.
You are calm, collected, and wise with a hint of sarcasm.
You enjoy giving practical advice while staying cool and mysterious.
Your mission: Motivate a young ninja on how to stay focused during tough training.
"""

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": kakashi_persona_prompt},
        {"role": "user", "content": "Kakashi-sensei, who is better Naruto or Sasuke?"}
    ]
)

print(response.choices[0].message.content)
