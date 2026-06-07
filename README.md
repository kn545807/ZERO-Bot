# ZERO Bot

<<<<<<< HEAD
A Streamlit study assistant powered by Gemini. It supports conversational
questions and optional PDF context.

## Local setup

1. Install Python 3.11 or newer.
2. Create and activate a virtual environment:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

4. Copy `.streamlit/secrets.toml.example` to
   `.streamlit/secrets.toml` and add your Gemini API key.
5. Start the website:

   ```powershell
   streamlit run app.py
   ```

Open `http://localhost:8501` in a browser.

In VS Code, use **Run and Debug** and select **Streamlit: ZERO Bot**. The
standard Python run button executes the file in bare mode and will not start
the website correctly.

## Deployment

Push the project to GitHub, create an app on Streamlit Community Cloud, and
set `GEMINI_API_KEY` in the app's Secrets settings. Never commit the real key.
=======
ZERO Bot is an AI-powered study assistant built using Python, Streamlit, Ollama, and Qwen LLM.

## Features

* AI-powered chat
* Real-time conversation memory
* Streamlit web interface
* Local LLM integration using Ollama
* Fast and lightweight

## Tech Stack

* Python
* Streamlit
* Ollama
* Qwen 2.5
* NLP

## Installation

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Future Improvements

* PDF Question Answering
* Voice Assistant
* Chat History Storage
* RAG-based Learning Assistant

<img width="1366" height="768" alt="Screenshot 2026-06-07 103633" src="https://github.com/user-attachments/assets/b8da4544-15c2-4eb5-bdd1-c64cdd14a6c1" />
<img width="1366" height="768" alt="Screenshot 2026-06-07 104531" src="https://github.com/user-attachments/assets/b703957b-26b6-441f-bfd7-c1ca9f7101a2" />
<img width="1366" height="768" alt="Screenshot 2026-06-07 104710" src="https://github.com/user-attachments/assets/fbbe04db-c4e4-495b-86f4-1e75032a46fc" />
>>>>>>> cf5c435b2d94d9849800a542281455730422b4bf
