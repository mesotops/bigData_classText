# -*- coding: utf-8 -*-   [   Code 8-11 :     One Piece : Simple Version  ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()
G.add_edge('魯夫','卡普')
G.add_edge('魯夫','羅傑')
G.add_edge('索隆','魯夫')
G.add_edge('索隆','布魯克')
G.add_edge('香吉士','娜美')
G.add_edge('魯夫','羅賓')
G.add_edge('魯夫','喬巴')
G.add_edge('魯夫','香吉士')
G.add_edge('魯夫','娜美')
G.add_edge('喬巴','羅賓')
G.add_edge('魯夫','布魯克')
G.add_edge('魯夫','索隆')

plt.figure(figsize=(15,15))
nx.spring_layout(G, seed =1568)
nx.draw_networkx(G, with_labels=True, node_size=5000, font_size=18, font_family='SimHei', font_color="white", font_weight="bold")


