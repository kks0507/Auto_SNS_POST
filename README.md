# Auto_SNS_Post 🚀

## Description
ChatGPT API를 활용하여 X(구 트위터)에 올릴 게시물을 자동으로 작성하고 포스팅해주는 프로그램입니다.

## Installation and Execution

### Requirements
먼저 프로그램을 실행하기 위해 필요한 라이브러리들을 설치하세요. `requirements.txt` 파일에 명시된 라이브러리를 설치합니다:

```bash
pip install -r requirements.txt
```

`requirements.txt` 파일에는 다음 라이브러리들이 포함되어 있습니다:

- openai==1.10.0
- tweepy

### Environment Variables
트위터 API와 OpenAI API를 사용하기 위해 환경 변수를 설정해야 합니다. 다음의 환경 변수를 설정하세요:

```bash
export OPENAI_API_KEY=your_openai_api_key
export TWITTER_CONSUMER_KEY=your_consumer_key
export TWITTER_CONSUMER_SECRET=your_consumer_secret
export TWITTER_ACCESS_TOKEN=your_access_token
export TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret
export TWITTER_BEARER_TOKEN=your_bearer_token
```

### Run the Program
프로그램을 실행하여 ChatGPT로부터 게시물 내용을 생성하고, 트위터에 게시하려면 아래와 같이 실행하세요:

```bash
python tweet.py
```

## Code Explanation

### 주요 함수: `gpt_api.py`
```python
import openai
import os

def make_autoPost():
    request = "저는 AI 엔지니어를 꿈꾸는 '루키'입니다..."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=1,
        messages=[
            {"role": "system", "content": "너는 매우 적극적인 성격이고..."},
            {"role": "user", "content": request}
        ]
    )
    return response.choices[0]["content"]
```
이 함수는 ChatGPT API를 호출하여 X에 올릴 자동 포스팅 내용을 생성합니다.

### 주요 함수: `twitter_api.py`
```python
import tweepy
import os

def post(tweet):
    client = tweepy.Client(
        bearer_token=os.environ["TWITTER_BEARER_TOKEN"],
        consumer_key=os.environ["TWITTER_CONSUMER_KEY"],
        consumer_secret=os.environ["TWITTER_CONSUMER_SECRET"],
        access_token=os.environ["TWITTER_ACCESS_TOKEN"],
        access_token_secret=os.environ["TWITTER_ACCESS_TOKEN_SECRET"]
    )
    client.create_tweet(text=tweet)
```
이 함수는 Tweepy 라이브러리를 사용하여 트위터 API로 게시물을 포스팅합니다.

### 주요 실행 파일: `tweet.py`
```python
import gpt_api
import twitter_api

tweet = gpt_api.make_autoPost()
twitter_api.post(tweet)
```
이 파일은 `gpt_api.py`로부터 게시물 내용을 가져오고, 이를 `twitter_api.py`를 통해 트위터에 게시합니다.

## Contributor
- kks0507

## License
This project is licensed under the MIT License.

## Repository
코드 및 프로젝트의 최신 업데이트는 [여기](https://github.com/kks0507/Auto_SNS_POST-.git)에서 확인할 수 있습니다.

