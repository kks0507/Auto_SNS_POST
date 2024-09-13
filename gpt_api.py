# 1. openai 라이브러리 불러오기
import openai
import os

# 1.1) OpenAI의 API 키 설정
openai.api_key = os.environ["OPENAI_API_KEY"]

# 2. Chat GPT에 요청을 전송하는 함수 정의
def make_autoPost():
    # 2.1) Chat GPT에게 요청할 핵심 명령문 설정
    request = "저는 AI 엔지니어를 꿈꾸는 '루키'입니다. 저의 SNS(X,tweeter)에 포스팅 할 루키의 성장일기를 100자 이내로 작성해주세요. n|n|n 성장일기를 작성할 때 아래의 예문을 참고해 주세요.|n|n"
    
    # 2.2) 예시 문장
    exam1 = "오늘은 자연어 처리 모델을 처음 다뤄봤어요. 조금 어려웠지만, 성장하고 있는 느낌이 들어요!"
    exam2 = "작은 걸음이지만, 매일 배우는 즐거움이 쌓여가고 있어요. AI 엔지니어의 길, 조금씩 나아갑니다."
    
    # 2.3) 핵심 명령문과 예시 문장을 연결해 하나의 명령문으로 만들기
    content = request + exam1 + exam2

    # 2.4) Chat GPT에게 요청보내기
    response = openai.ChatCompletion.create(
        ## 구체적인 Chat GPT API의 매개변수 설정
        model="gpt-3.5-turbo",
        temperature=1,
        messages=[
            ## Chat GPT 시스템의 정체성 설정
            {"role": "system", "content": "너는 매우 적극적인 성격이고, 루키로서 AI 분야에서 실력을 향상시키고자 하는 강한 열망을 가지고 있어."},

            ## Chat GPT에게 할 실질적 지시(명령문)
            {"role": "user", "content": content}
        ]
    )

    # 2.5) Chat GPT가 생성한 게시글 내용 반환
    return response.choices[0]["content"]


