# https://wikidocs.net/89215

import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from math import sqrt

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


like=pd.read_csv('./like_product.csv')
product=pd.read_csv('./product.csv')

print(product.head())

new_item_id = pd.DataFrame(columns=['product_id', 'new_product_id'])
new_item_id['product_id'] = like.product_id.unique()
new_item_id['new_product_id'] = range(len(like.product_id.unique()))

# print(new_item_id)

data = like.merge(new_item_id, on='product_id')

# print(data.head())

train = data[:int(len(data)*0.7)]
test = data[:int(len(data)*0.7)]

score = np.zeros((len(train.member_number.unique()), len(data.new_product_id.unique())))
# print(score.shape)

train_item_lst = train.groupby(['member_number']).new_product_id.apply(list)
# print(train_item_lst[:5])

train_item_lst = train_item_lst.tolist()

for ix, item_lst in enumerate(train_item_lst):
    for item in item_lst:
        score[ix, item] = 1.0

# print(score.shape)

score_t = score.T
cosine_sim = cosine_similarity(score_t, score_t)

for i in range(len(data.new_product_id.unique())):
        cosine_sim[i, i] = 1.0

cosine_sim_data = pd.DataFrame(cosine_sim)
num =[]
print(cosine_sim_data.head())

for like in cosine_sim_data[0]:
    if like  >0:
        num.append(like)

print(num)




def recommendations(ids, top, cosine_sim_data=cosine_sim_data):
    rec_lst = list(cosine_sim_data[ids].sort_values(ascending=False)[1:top+1].index)
    return rec_lst

print(recommendations(120, 5, cosine_sim_data))



def evaluation(test, top):
    recall = 0.0
    mrr = 0.0
    count =0
    lst = []
    for idx in range(test.groupby(['member_number']).size().cumsum().values[-2]):
        sess_id = test['member_number'].values[idx]
        id2 = test['new_product_id'].values[idx]
        if sess_id == test['member_number'].values[idx + 1]:
            top_lst = recommendations(id2, top=top)
            answer = test['new_product_id'].values[idx + 1]
            lst += top_lst
            count += 1
            try:
                rank = top_lst.index(answer)
                recall += 1.0
                mrr += 1/(rank + 1)
            except:
                continue
    print('Recall: {:2.2%} MRR: {:2.2%}'.format(recall / count, mrr / count))
    return recall / count, mrr / count





evaluation(test, 20) #Recall: 42.10% MRR: 17.83%