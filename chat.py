# zero shot prompting
from dotenv import  load_dotenv
from openai import  OpenAI
import os
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client=OpenAI(api_key=api_key)
result=client.chat.completions.create(
    model="gpt-4o",
    messages=[{
        "role":"user",
        "content":"How do I check if a Python object is object" 
    }]
)
print(result.choices[0].message.content)
