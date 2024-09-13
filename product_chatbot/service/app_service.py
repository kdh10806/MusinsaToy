

from flask import json
from repo.repository_mysql import find_member_number, find_product, like_count
from service.similar_keyword import search_keyword, register_keyword
from service.contents_base import recom_likebase
from service.chatOpenAi import analyze_bot, shop_chat_bot
from service.tohtml import product_size_zero, recommendhtml, searchhtml  


def chat_bot_service(user_input, user_id):

    # open ai 로 user의 내용 분석. recommendation, search, other로 분류
    response = json.loads(analyze_bot(user_input = user_input))

    filter = response.get('option')

    # other인 경우 쇼핑몰 챗봇과 대화.
    if(filter == "other"):
        return shop_chat_bot(user_input = user_input, user_id=user_id)
    
    # recommendation의 경우 contents_base 로 설정. -> 카테고리별 등은 나중에...
    if(filter == "recommendation"):
        

        # user_id가 없는 경우 member_number를 0으로
        if(user_id is None):
            member_number = 0
        else :
            member_number = find_member_number(user_id = user_id)

        count = like_count(int(member_number))

        # like 개수가 5개 이하라면 1번의 데이터로 추천
        # 현재는 1번의 경우 default 사용자로 정해두기.
        if(count<6):
            member_number = 1
        

        text = recommendhtml(recom_likebase(member_number=member_number), member_number= member_number)

        return text
    
    # search의 경우 openai가 키워드를 추출해내지 못할 경우 사용자에게 정확한 키워드 입력하도록 return
    if(response.get('keyword') == "NoneKeyword"):
        return "해당 내용에 대해 정확히 검색할 수 없습니다. <br> 정확한 키워드로 다시 입력해 주세요.ㅠㅠ"
    
    # openai에서 제공한 keyword로 chromaDB에서 비슷한 키워드 찾기.
    else:
        # 5개의 product_id 반환 후 db에서 해당 product_id의 내용 찾기.

        product_ids = search_keyword(response)
        if(len(product_ids)==0):
            return product_size_zero(response)
        search_list = find_product(product_ids)
       
        return  searchhtml(search_list, response.get('keyword'))

# 상품 등록시 chromadb에 저장. 
def register_chromadb(product):
    register_keyword(product)
    