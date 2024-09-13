

def recommendhtml(recommend_list, member_number):
    if(member_number==1):
        text = "<br> 기본 상품으로 추천을 해 드릴게요.<br> "
    else:
        text = "<br> 좋아요를 기반으로 상품 추천을 해 드릴게요.<br> "
        
    text = text+'<br>'.join(recommend_list)
    return text


def searchhtml(search_list, keyword):
    text =f"<br>{keyword}라는 키워드로 검색을 진행해 보았습니다.<br>"
    
    for i in range(len(search_list)):
        
        text = text + f"<div sytle=\"display:flex; flex-direction:row; \"><img src='{search_list[i][1]}' style =\"max-width : 150px; max-heigth : 150px\">"
        text = text + f"<a href ='/product/detail/{search_list[i][2]}'>{search_list[i][0]}<a></div>"

    return text

def product_size_zero(response):

    text ="<br>"
    
    if(response.get('brand')!="NoneKeyword" and response.get('brand') is not None):
        text = text + f"{response.get('brand')}의 브랜드에서"

    text =text + f" {response.get('keyword')}라는 키워드로 검색을 진행해 보았지만,<br> 해당 키워드와 연관있는 상품을 찾지 못하였습니다요."
    text =text + f"<br>정말 죄송합니다요."

    return text

    


