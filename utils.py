from typing import List
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


def prompt_chain_workflow(initial_input: str, prompt_chain: List[str]) -> List[str]:
    response_chain: List[str] = []
    response = initial_input

    for i, prompt in enumerate(prompt_chain, 1):
        print(f"\n[{i} 단계]\n")

        final_prompt = f"""{prompt}

        처음에 사용자가 입력한 내용은 아래와 같아. 항상 이 내용을 참고해
        userInput: {initial_input}

        응답시 아래 내용을 참고해.
        {response}
        """

        print(f"프롬프트: {final_prompt}")

        response = llm_call(final_prompt)
        print(f"중간 답변: {response}")
        response_chain.append(response)

    return response_chain
