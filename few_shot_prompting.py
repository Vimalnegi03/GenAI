from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()
api_key=os.getenv("OPEN_API_KEY")
client=OpenAI(api_key=api_key)

system_prompt="""
You are an AI assistant who is specialized in maths.You should not query anything that is not related to maths
For a given query help user to solve that along with explanation
Example:
Input:2+2
Output:2+2 is 4 which is calculated by adding 2 with 2
Input:3*10
Output:3*10 is 30 which is calculated by multiplying 3 by 10.Funfact you can even multiply 10 by 3 which give same output
Input:Why sky is blue?
Output:Bruh are you alright?Is it maths query
"""

result=client.chat.completions.create(
    model="gpt-4",
    temperature=0.5,
    max_tokens=200,
    messages=[{
        "role":"system","content":system_prompt
    },
    {
        "role":"user","content":"What is 5*45"
    }]
)
print(result.choices[0].message.content)
