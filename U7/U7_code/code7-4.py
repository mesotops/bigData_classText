# -*- coding: utf-8 -*-   [   Code 7-4 :    TF  ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#
from sklearn.feature_extraction.text import CountVectorizer  

sentences = [
      '福利 出國 玩 年終 分紅 舉辦活動 樂趣 員工 出國', 
      '員工 機會 轉正職 才能 年度 分紅 福利', 
      '員工 相處融洽 福利 分紅 福利 ',
      '友善  樂趣 相處融洽 福利 辦公 優良',
      ]

vectorizer = CountVectorizer()  
X = vectorizer.fit_transform(sentences)  
word = vectorizer.get_feature_names()  
print(word)  
print(X.toarray()) 

