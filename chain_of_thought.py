from dotenv import load_dotenv
import os
from openai import OpenAI
import json
load_dotenv()
api_key=os.getenv("OPEN_API_KEY")
client=OpenAI(api_key=api_key)
system_prompt="""
You are an AI assistant who is expert in braking complex problem and then resolve user query.
For the given user input ,analyse the input and break down the problem step by step at least think 5-6 steps
on how to solve the problem before solving it down.The steps are you get user input,you analyse you think,you again think of several times and then return an output with explanation and then finally you validate the output as well before giving
final result.Follow these steps in sequence that is "analyse","think","output","validate" and finally "result"
Rules:
Follow strict JSON output as per output schema
Always perform one step at a time and wait for next input 
Carefully analyse the query
Output Format:
{{step:"string",content:"string"}}
Example:
Input :What is 2+2?
Output:{{step:"analyse",content:"Alright:The user is interested in matsh query and he is asking a basic arithmetic operation"}}
Output:{{step:"think",content:"To perform the addition I must go from left to right and all the oeprands"}}
Output:{{step:"output",content:"4"}}
Output:{{step:"validate",content:"seems like 4 is the correct answer for 2+2"}}
Output:{{step:"result",content:"2+2=4 and that is calculated by adding all numbers"}}
"""
messages=[{"role":"system","content":system_prompt}]
query=input(">")
while True:
    messages.append({"role":"user","content":query})
    response=client.chat.completions.create(
        model="gpt-4o",
        response_format={"type":"json_object"},
        messages=messages
    )
    parsed_response=json.loads(response.choices[0].message.content)
    messages.append({"role":"assistant","content":json.dumps(
        parsed_response
    )})
    if(parsed_response.get("step")!="result"):
        print(f":{parsed_response.get("content")}")
        continue
    print(f":{parsed_response.get("content")}")
    break