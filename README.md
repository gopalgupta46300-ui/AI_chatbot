# AI Chatbot

<p align="center">
  <img src="https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&w=1400&q=80" alt="AI Chatbot Banner" width="100%" />
</p>

<p align="center">
  <a href="#features"><img src="https://img.shields.io/badge/Features-AI%20Assistant-5B8DEF?style=for-the-badge" alt="Features" /></a>
  <a href="#tech-stack"><img src="https://img.shields.io/badge/Tech-Streamlit%20%2B%20Gemini-34D399?style=for-the-badge" alt="Technology" /></a>
  <a href="#setup"><img src="https://img.shields.io/badge/Setup-Quick%20Start-FFB703?style=for-the-badge" alt="Setup" /></a>
</p>

A clean and lightweight AI chatbot project built with Python, Streamlit, and Google Gemini. This repository is designed for quick experimentation, learning, and extending conversational AI with minimal setup.

## Overview

- Simple and beginner-friendly chatbot interface
- Powered by Google Generative AI via LangChain
- Built with Streamlit for a polished web UI
- Easy to modify for custom prompts and workflows
- Suitable for prototyping AI applications

## Features

- Ask questions in a clean chat-like interface
- Real-time responses from Gemini model
- Lightweight single-file app structure
- Environment-variable-based API configuration
- Easy extension for custom logic and workflows

## Tech Stack

- Python
- Streamlit
- LangChain
- Google Generative AI (Gemini)
- Python-dotenv

## Project Structure

```text
AI_chatbot/
├── app.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt (optional, if added later)
```

## Installation

1. Clone the repository

```bash
git clone https://github.com/gopalgupta46300-ui/AI_chatbot.git
cd AI_chatbot
```

2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies

```bash
pip install streamlit python-dotenv langchain-google-genai
```

4. Set environment variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_google_api_key
```

5. Run the app

```bash
streamlit run app.py
```

## How It Works

The app loads environment variables using `python-dotenv`, initializes the Gemini model, and exposes a Streamlit input field for user prompts. When a question is submitted, the model responds and the answer is rendered directly in the app.

## Example

```python
response = llm.invoke(user_input)
st.write(response.content)
```

## Screenshots

<p align="center">
  <img src="https://images.unsplash.com/photo-1531482615713-2afd69097998?auto=format&fit=crop&w=1200&q=80" alt="AI app interface" width="80%" />
</p>

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.

---

Built for learning, experimentation, and building AI-powered experiences.
