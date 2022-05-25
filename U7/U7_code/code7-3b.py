# -*- coding: utf-8 -*-   [   Code 7-3b :  Jieba    ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#
#加入 繁體中文辭庫及自訂詞
import jieba
jieba.set_dictionary('C:/Pyfiles/dictionary/dict.txt')
jieba.load_userdict('C:/Pyfiles/dictionary/user_dict.txt')
sentence='今天跟好友陳太陽去野生動物園玩，心情真好!'
breakword=jieba.cut(sentence, cut_all=False)
print('|'.join(breakword))