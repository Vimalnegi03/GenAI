# 🚀 GenAI Assistant

A powerful, step-by-step AI agent using OpenAI's GPT model!  
GenAI Assistant plans, selects appropriate tools, executes actions, observes results, and solves user queries intelligently.

---

## 🧠 Project Structure

- **Plan:** Understands and breaks down user queries.
- **Action:** Selects the right tool (`get_weather`, `run_command`, etc.) and executes it.
- **Observe:** Waits for the tool output.
- **Resolve:** Based on observations, answers the user intelligently.

---

## 🛠️ Features

- 🤖 **Intelligent Planning**: Follows a structured start ➡ plan ➡ action ➡ observe ➡ output loop.
- 🌦️ **Weather Fetching**: Get real-time weather data using `wttr.in`.
- 💻 **System Command Execution**: Run system-level commands safely (for experimental purposes).
- 🗂️ **Tool Selection**: Chooses tools automatically based on user needs.
- 🔒 **Environment Config**: API keys are managed using `.env`.

---

## 📂 Requirements

- Python 3.8+
- `openai`
- `python-dotenv`
- `requests`

Install dependencies:

```bash
pip install openai python-dotenv requests
```
