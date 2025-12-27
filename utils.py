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

def llm_router_call(user_prompt: str) -> str:
    router_prompt = f"""
    사용자 질문: {user_prompt}

    위 질문에 대해 가장 적절한 유형을 하나 골라.
    - 일상: 일반적인 대화, 일정 짜기, 정보 요청 등
    - 빠른: 계산, 단답형 질문, 간단한 명령 등
    - 코딩: 파이썬, 코드 작성, 오류 디버깅 등

    단답형으로 유형만 출력해.
    """

    response = llm_call(router_prompt)
    return response.strip()

def run_general_agent(user_prompt: str) -> str:
    prompt = f"""
    너는 다재다능한 일상 도우미야.
    여행 일정, 추천, 요약 등 일상적인 질문에 친절하고 유용하게 답변하지.

    [사용자 질문]
    {user_prompt}
    """

    return llm_call(prompt)

def run_quick_agent(user_prompt: str) -> str:
    prompt = f"""
    너는 빠른 답변을 제공하는 도우미야.
    사용자의 질문에 두괄식으로 빠르게 답변을 제공하지.

    [사용자 질문]
    {user_prompt}
    """

    return llm_call(prompt)

def run_coding_agent(user_prompt: str) -> str:
    prompt = f"""
    너는 코딩 도우미야.
    파이썬, 자바 스크립트, API 개발, 오류 디버깅 등에 능숙해.
    질문에 대해 최대한 정확하고 실행 가능한 코드를 제공하지.

    [사용자 질문]
    {user_prompt}
    """

    return llm_call(prompt)

ROUTING_MAP = {
    "일상": run_general_agent,
    "빠른": run_quick_agent,
    "코딩": run_coding_agent,
}
