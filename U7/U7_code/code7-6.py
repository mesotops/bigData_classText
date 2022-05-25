# -*- coding: utf-8 -*-   [   Code 7-6 :  TF-IDF  +  LDA    ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, TfidfTransformer   

sentences = [
      '福利 出國 玩 年終 分紅 舉辦活動 樂趣 員工 出國', 
      '員工 機會 轉正職 才能 年度 分紅 福利', 
      '員工 相處融洽 福利 分紅 福利',
      '友善  樂趣 相處融洽 福利 辦公 優良',
      ]

    
##TF-IDF
# 載入使用的套件

print('*'*70)
# 創建詞彙表
tfidf_model = TfidfVectorizer().fit(sentences)      
print(tfidf_model.vocabulary_)                  
print('='*70)


# 計算 TF-IDF
tfidf_model2 = TfidfVectorizer(max_df=0.7).fit(sentences)
print(tfidf_model2.vocabulary_)

df1=tfidf_model2.get_feature_names()
print('TF-IDF:',df1)


#得到tf-idf矩陣
tf = tfidf_model2.fit_transform(df1) 
tf_dense = tf.todense()


from sklearn.decomposition import LatentDirichletAllocation
n_topics = 5   ### 分幾個topics
n_top_words = 5   ### 顯示topic中多少個字(關鍵字)

lda = LatentDirichletAllocation(n_components=n_topics, random_state=0)        
lda.fit(tf)

feature_names = tfidf_model2.get_feature_names()
components = lda.components_
print('='*70)

##LDA匯出
topic_dic = {}
for no in range(n_topics):
          topic = ([feature_names[i] for i in components[no].argsort()[:-n_top_words - 1:-1]])
          topic_dic["topic"+str(no+1)] = topic

topic_df = pd.DataFrame(topic_dic)
print(topic_df)
topic_df.to_excel("C:/Pyfiles/Temp/result.xlsx",index=False)