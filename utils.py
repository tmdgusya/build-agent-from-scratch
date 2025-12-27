from ollama import Client, chat

client = Client()

def llm_call(prompt: str, model: str = "qwen3:4b") -> str:
    messages = []
    messages.append({
        "role": "user",
        "content": prompt,
    })
    chat_completion = client.chat(model=model, messages=messages)
    response = chat_completion.message.content

    if not response:
        return ""

    return response
