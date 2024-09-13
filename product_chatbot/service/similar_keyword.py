import chromadb
from openai import OpenAI
import openai
from dotenv import load_dotenv
import os
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer

openai.api_key = os.getenv("OPENAI_API_KEY")




client = chromadb.PersistentClient(path="product")


product_collection = client.get_or_create_collection(
    name = "musinsa_product",
    metadata ={"hsnw:space":"cosine"}
)

category_collection = client.get_or_create_collection(
    name = "musinsa_category",
    metadata ={"hsnw:space":"cosine"}
)

brand_collection = client.get_or_create_collection(
    name = "musinsa_brand",
    metadata ={"hsnw:space":"cosine"}
)

# 약 700 차원
model = SentenceTransformer('snunlp/KR-SBERT-V40K-klueNLI-augSTS')

#-------------------------------------------------------------------------------------------------------------------------
# 임베딩 저장.

 # 추후 변경. - pd로 그냥 읽어도 되지만 많이 변할 게 없으니 csv로...
# product_metadata = pd.read_csv('./service/product.csv', dtype=str,encoding='UTF-8')
# product_brand = pd.read_csv('./service/brand.csv', dtype=str,encoding='UTF-8')
# product_category = pd.read_csv('./service/category.csv', dtype=str,encoding='UTF-8')

# for idx in range(len(product_brand)):
#     brand = product_brand.iloc[idx]
#     id = brand['name']
#     document = f"{brand['name']}:{brand['brand_id']}"
#     embedding = embedding = model.encode(document, normalize_embeddings=True).tolist()

#     brand_collection.add(
#         ids = id,
#         documents= document,
#         embeddings=embedding
#     )

# for idx in range(len(product_category)):
#     category = product_category.iloc[idx]
#     id = category['category_id']
#     document = f"{category['category_name']}"

#     embedding = embedding = embedding = model.encode(document, normalize_embeddings=True).tolist()
#     category_collection.add(
#         ids = id,
#         documents= document,
#         embeddings=embedding
#     )


# #처음 모든 상품 등록
# ids =[]
# doc_meta = []
# documents = []
# embeddings =[]
# metadatas = []
# dict = {}
# # Hugging Face 임베딩 모델 / 한국어(KR)

# #metadata 도 생각해보기. -> where과 같이 사용 가능하다고 함.
# for idx in range(len(product_metadata)):
#     #idx번째 행 선택
#     item = product_metadata.iloc[idx]
#     id = item['product_id']
#     document = f"{item['카테고리']}:{item['이름']}:{item['브랜드 영명']}:{item['브랜드 이름']}"
#     embedding = model.encode(document, normalize_embeddings=True).tolist()
#     dict['brand'] = item['브랜드 이름']
#     dict['category'] = item['카테고리']

#     metadata = dict.copy()
    

#     embeddings.append(embedding)
#     ids.append(id)
#     metadatas.append(metadata)
#     documents.append(document)

# product_collection.add(
#     ids = ids,
#     metadatas = metadatas,
#     documents=documents,
#     embeddings = embeddings 
# )

#-------------------------------------------------------------------------------------------------------------------------

# # filter 사용
# collection.similarity_search(
#     "TF IDF 에 대하여 알려줘", filter={"source": "data/nlp-keywords.txt"}, k=2
# )
def search_category(category):

    category = category_collection.query(
        query_embeddings=model.encode(category, normalize_embeddings=True).tolist(),
        n_results=1,
    )

    return category['ids'][0][0]


def search_brand(brand):
    
    brand = brand_collection.query(
        query_embeddings=model.encode(brand, normalize_embeddings=True).tolist(),
        n_results=1,
    )
    return brand['ids'][0][0]



# 생각 보다 검색 성능이 조금. 그렇네요. -> metadate로 filter 해주기.
def search_keyword(search_data):

    query_kwargs = {
        'query_embeddings': model.encode(search_data.get('keyword'), normalize_embeddings=True).tolist(),
        'n_results': 5
    }

    # where 절 조건을 담을 딕셔너리
    where_conditions = []

    # category가 None이 아닐 때, NoneKeyword가 아닐 때 조건 추가
    if (search_data.get('category') is not None )and (search_data.get('category')!="NoneKeyword"):
        category = search_category(search_data.get('category'))
        where_conditions.append({"category": {"$eq": category}})

    # 브랜드 동일.
    if (search_data.get('brand') is not None ) and (search_data.get('brand')!="NoneKeyword"):
        brand=search_brand(search_data.get('brand'))
        where_conditions.append({"brand": {"$eq": brand}})

    # 조건이 하나일 때는 바로 추가, 두 개 이상일 때는 "일단 or로가" - "니트 검색시 카테고리가 신발로 나옴;; "스웨터 니트"라고도 적어놨는데." 
    if len(where_conditions) == 1:
        query_kwargs['where'] = where_conditions[0]  # 1개 일 때{"$or":where_condition} 안됨 ㅜ

    elif len(where_conditions) > 1:
        query_kwargs['where'] = {"$and": where_conditions}

    # collection.query 호출
    
    product_ids = product_collection.query(**query_kwargs)



    # ans=collection.query(
    #     query_embeddings=model.encode(search_data.get('keyword'), normalize_embeddings=True).tolist(),
    #     n_results=5,
    #    # where={"category": None, "brand":None}
    # )

    return product_ids['ids'][0]


def register_keyword(product): 
    id = product['product_id']
    document = product['name']
    embedding = model.encode(document, normalize_embeddings=True).tolist()

    product_collection.add(
    ids = id,
    documents=document,
    embeddings = embedding 
    )