# -*- coding: utf-8 -*-   [   Code 7-3a :   Jieba    ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# 加入 繁體中文辭庫
import jieba
jieba.set_dictionary('C:/Pyfiles/dictionary/dict.txt')
sentence='我今天要到高雄小港機場搭飛機出差'
breakword=jieba.cut(sentence, cut_all=False)
print('|'.join(breakword))
