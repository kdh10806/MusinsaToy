import pandas as pd
import numpy as np
from repo.repository_mysql import recommend
import pymysql
from sklearn.metrics.pairwise import cosine_similarity
conn = pymysql.connect(host='127.0.0.1',port=3306, user='root', password='Wjdfyddn2015!', db='web_ex', charset='utf8')

# db에서 불러오든 바꿔줘도 상관없음.
product=pd.read_csv('./product.csv')


# print(item_similarity)
def recom_likebase(member_number):
    global like_matrix_t
    global item_similarity
    
    

    like = recommend() # 해당 사용자의 like 개수 확인
    
    #like의 컬럼을 만들고 1로 만들어줌 - like 명시.
    like['like'] = 1

    # print(product.loc[product['product_id']=='1023790']['name'])

    x = like.copy()
    y = like['member_number']

    #25%는 y,x_test로 분류 -> trainset 하지말고 그냥 모든 상품에 대해서로 바꾸기.
    # x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25,stratify=y,random_state=12)
    # print(x_train)

    ratings_df_mean = like.groupby('product_id')['like'].mean()
    ratings_df_count = like['product_id'].value_counts()

    mc_df = pd.merge(ratings_df_mean,ratings_df_count,on='product_id')

    #그냥 pivot 하면 product_id 중복 때문에 안됨. pivot_table 해야함. 
    like_matrix_t = like.pivot_table(values='like', index='product_id',columns='member_number')

    matrix_dummy = like_matrix_t.copy().fillna(0)

    # print(matrix_dummy)

    # 이거 그냥 벡터 내적이던데.
    item_similarity = cosine_similarity(matrix_dummy, matrix_dummy)
    item_similarity = pd.DataFrame(item_similarity, index=like_matrix_t.index, columns=like_matrix_t.index)


    

    data = recommender(member_number = member_number)

    names = [item.iloc[0] for item in data]

    return names



# product_id는 현재 memeber_number 가 해당 product_id에 좋아요를 누르지 않은 상태. -> 해당 사용자가 좋아요를 누르지 않은 상품에 대해서만 예상.
def ibcf(member_number, product_id, K=0):
    if member_number in like_matrix_t:          # 사용자가 있는지 확인.
        if product_id in item_similarity:     # 현재 의류가 있는지 확인

            # 현재 사용자가 좋아요 하지 않은 의류와 다른 의류의  similarity 값 가져오기
            sim_scores = item_similarity[product_id]

            # 현 사용자 다른 사용자가 좋아요한 모든 product_id 값 가져오기 -> 현재 사용자가 like = 1, 다른 사용자가 like =Nan
            user_like = like_matrix_t[member_number]

            # 현 사용자가 좋아요 하지 않은 의류 index 가져오기
            non_rating_idx = user_like[user_like.isnull()].index

            # 현 사용자가 좋아요 하지않은 않은 의류 제거
            user_like = user_like.dropna()

            # 현 사용자가 좋아요 하지 않은 similarity 값 제거
            sim_scores = sim_scores.drop(non_rating_idx)
            # print(sim_scores)

            # 현 product_id(사용자가 좋아요 하지 않은)에 대한 사용자의 예상 rating 계산, 가중치는 현 의류와 사용자가 평가한 의류의 유사도
            # 현재 의류와 userid가 누른 좋아요 유사도* 의류 좋아요 > 현재 의류의 좋아요할 확률? 예측 (좋아요=1)
            mean_rating = np.dot(sim_scores, user_like) / sim_scores.sum()
            # print(sim_scores.sum(),"\n")
            # print(product_id," : ",mean_rating)
            # print("simscores\n",sim_scores,"\n",len(sim_scores))
            # print("user_like\n",user_like, "\n", len(user_like))
            

    # 현재 사용자가 좋아요한 상품이 없거나, 아무에게도 좋아요(상품id가 없음) 되지 않았다면 0.3... 상품 id 없는거는  그냥 모든 상품 불러와야하나.          
        else:
            
            mean_rating = 0.3
    else:
        mean_rating = 0.3
    return mean_rating



def recommender(member_number, n_items=5):
    # 현재 사용자의 모든 의류에 대한 예상 좋아요 계산
    predictions = []
    recommended_items =[]
    rated_index = like_matrix_t[member_number][like_matrix_t[member_number] > 0].index     # 이미 평가한 좋아요 확인
    items = like_matrix_t[member_number].drop(rated_index) # 현재 사용자가 좋아요 하지 않은 product_id 모음.
    
    for item in items.index:
        predictions.append(ibcf(member_number, item))
        # print(item)   
    # print(predictions)                              
    # 예상
    recommendations = pd.Series(data=predictions, index=items.index, dtype=float)
    # print(recommendations)
    recommendations = recommendations.sort_values(ascending=False)[:n_items] # 좋아요 확률?이 가장 높은 의류 선택 -> 다른 사람이 고른것 들 중에서.
    # print(recommendations)
    # print(recommendations.index)
    for product_id in recommendations.index:
        recommended_items.append(product.loc[product['product_id'] == product_id]['name'])

    return recommended_items


