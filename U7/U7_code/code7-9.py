#-*- coding: utf-8 -*-   [   Code 7-9 :   Text Cluster   ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#
#
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, TfidfTransformer   
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_columns', None)

sentences = [
      '福利 出國 玩 年終 分紅 舉辦活動 樂趣 員工 出國', 
      '員工 機會 轉正職 才能 年度 分紅 福利', 
      '員工 相處融洽 福利 分紅 福利',
      '友善  樂趣 相處融洽 福利 辦公 優良',
      ]
   

vectorizer = CountVectorizer()  
X = vectorizer.fit_transform(sentences)  



print(X)
from sklearn.cluster import KMeans
num_clusters = 2
km = KMeans(n_clusters=num_clusters)
km.fit(X)
clusters = km.labels_.tolist()
print(len(clusters))
print(clusters)


Result =open("C:/Pyfiles/Temp/title_clusters.txt", 'w+',encoding='GB2312',errors='ignore')
for i in clusters:
  Result.write(str(i))
  Result.write("\n")
Result.close()