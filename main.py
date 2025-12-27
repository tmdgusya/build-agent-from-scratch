from utils import llm_call, prompt_chain_workflow

if __name__ == "__main__":
    test = llm_call("한국의 수도는?")
    print(test)

    prompts = [
        """사용자의 여행 취향을 바탕으로 적합한 여행지 세 곳을 추천해.
        - 사용자가 입력한 내용을 요약해.
        - 추천한 여행지가 왜 적합한지 설명해.
        - 각 여행지의 기후, 주요 관광지를 알려줘.
        """,
        """가장 추천하는 여행지 한 곳을 설명하고, 거기서 할 수 있는 활동을 제안해.
        - 왜 최종 여행지로 선정했는지 설명해.
        - 해당 여행지에서 즐길 수 있는 다섯 가지 활동을 나열해.
        - 자연 탐방, 역사 탐방, 음식 체험 등 다양한 영역의 활동을 골라줘.
        """,
        """추천한 여행지의 하루 일정 계획을 세워줘.
        - 오전, 오후, 저녁으로 나눠 일정을 짜줘.
        - 각 시간대에 어떤 활동을 하면 좋을지 설명해.
        """
    ]

    user_input = input("여행 스타일 입력: \n")
    results = prompt_chain_workflow(prompt_chain=prompts, initial_input=user_input)

    print(results[-1])
