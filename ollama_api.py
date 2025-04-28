from fastapi import FastAPI, Body
from ollama import Client

app = FastAPI()

# NOTE: You had a typo: "locallhost" -> should be "localhost"
client = Client(host="http://localhost:11434")

# Pull the model only once, ideally at startup
client.pull("gemma3:1b")  # "gemma3:lb" seems incorrect, maybe you mean "gemma:2b" or "gemma:7b"

@app.post("/chat")
def chat(message: str = Body(..., description="Chat Message")):
    response = client.chat(
        model="gemma3:1b",
        messages=[   # Typo: you wrote "message" instead of "messages" (must be a list)
            {"role": "user", "content": message},
        ]
    )
    return {"response": response['message']['content']}  # Small fix: Correct accessing the returned response
