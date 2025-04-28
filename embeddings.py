from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
print(api_key)
client = OpenAI(api_key=api_key)

text = "Eiffel Tower is a famous landmark, it is 324 meters tall"
response = client.embeddings.create(
    input=text,
    model="text-embedding-3-small"
)

print("Vector Embeddings:", response.data[0].embedding)
