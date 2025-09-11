import os
import gradio as gr
import requests
from dotenv import load_dotenv

load_dotenv()
PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")

def chat_perplexity(user_message, history=[]):
    if not isinstance(history, list):
        history = []

    url = "https://api.perplexity.ai/chat/completions"
    headers = {
        "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
        "Content-Type": "application/json"
    }

    # Build message history for Perplexity API
    messages = [{"role": "system", "content": "You are a helpful AI assistant."}]
    for user, assistant in history[-10:]:  # Only keep last 10 exchanges
        messages.append({"role": "user", "content": user})
        messages.append({"role": "assistant", "content": assistant})
    messages.append({"role": "user", "content": user_message})

    data = {
        "model": "sonar",
        "messages": messages,
        "max_tokens": 300,
        "temperature": 0.7
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        reply = result["choices"][0]["message"]["content"]
    except Exception as e:
        reply = f"Error: {str(e)}"

    history.append((user_message, reply))
    history = history[-10:]  # Keep only last 10 exchanges
    return history, history

chatbot_ui = gr.Blocks()
with chatbot_ui:
    gr.Markdown("## Perplexity LLM Chatbot")
    chatbot = gr.Chatbot()
    msg_box = gr.Textbox(label="Your message")
    state = gr.State()
    send_btn = gr.Button("Send")
    send_btn.click(chat_perplexity, inputs=[msg_box, state], outputs=[chatbot, state])

chatbot_ui.launch()