# gpt_api.py와 twitter_api.py를 호출하는 프로그램  
import gpt_api
import twitter_api

# 1. 챗GPT에서 트윗 내용 가져오기
tweet = gpt_api.make_autoPost()

# 2. 트위터에 트윗을 올리기
twitter_api.post(tweet)