import os
import time
from openai import OpenAI


api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)

messages = [] # 메세지들이 담기는 공간 => 챗봇 (채팅 내역 6개월동안 보관 법적으로 필요) / 유럽진출(유로6)
user_thread = {}


def wait_on_run(run, thread):
    # 주어진 실행(run)이 완료될 때까지 대기
    # status 가 "queued" 또는 "in_progress" 인 경우에는 계속 polling 하며 대기합니다.
    while run.status == "queued" or run.status == "in_progress":
        # run.status 를 업데이트
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id,
        )
        # API 요청 사이에 잠깐의 대기 시간을 두어 서버 부하를 줄인다고함.
        time.sleep(0.5)
    return run


def analyze_bot(user_input):
    #생성한 어시스턴트의 id 설정.(open ai의 어떤 assistats사용할 건지)
    assistant =client.beta.assistants.retrieve('asst_dH7HMmoi4cQiUxRACIT6MFBK')

    #요청시마다 thread_id 가 달라짐. 저장 필요.
    # Mysql 에 테이블 하나 만들고, user_id마다 어떤 thread_id 가지고 있는지,
    # redis 사용해보기. 
    thread=client.beta.threads.create()
    message=client.beta.threads.messages.create(thread_id=thread.id
                                        ,role="user"
                                        , content=user_input)
    
    run=client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id
        # instruction = "" # assistant에게 설정.
    )

    #응답 기다림.
    run = wait_on_run(run=run, thread=thread)

    # 해당 thread와의 message 리스트 return
    message=client.beta.threads.messages.list(thread.id)

    #응답의 최상위 가져옴. -> 가장 최신이 맨 위.
    res = message.data[0].content[0].text.value
    
    return res

def shop_chat_bot(user_input, user_id):

    # 쇼핑몰 chat bot의 id
    assistant =client.beta.assistants.retrieve('asst_0jiYLASGkFkGInNDxmhUcaCX')

    # 해당 유저가 thread를 가지고 있을 경우
    if(user_thread.get(user_id) is not None):
        thread = user_thread.get(user_id)
    else :
        thread=client.beta.threads.create()
        if(user_id is not None):
            user_thread[user_id] = thread
    
    
    message=client.beta.threads.messages.create(thread_id=thread.id
                                        ,role="user"
                                        , content=user_input)
    
    run=client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id
    )

    #응답 기다림.
    run = wait_on_run(run=run, thread=thread)

    message=client.beta.threads.messages.list(thread.id)

    
    res = message.data[0].content[0].text.value

    
    return res
