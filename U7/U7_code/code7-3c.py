# -*- coding: utf-8 -*-   [   Code 7-3c :  Jieba    ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#
#加入繁體中文辭庫、自訂詞、及停用詞

import jieba
jieba.set_dictionary('C:/Pyfiles/dictionary/dict.txt')
jieba.load_userdict('C:/Pyfiles/dictionary/user_dict.txt')
with open('C:/Pyfiles/dictionary/stopWord_test.txt','r',encoding='utf-8-sig') as f:
    stops=f.read().split('\n')

sentence='今天跟好友陳太陽去野生動物園玩，心情真好!'
breakword=jieba.cut(sentence, cut_all=False)

words=[]
for word in breakword:
    if word not in stops:
        words.append(word)
print('|'.join(words))