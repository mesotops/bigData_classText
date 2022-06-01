# -*- coding: utf-8 -*-   [   Code 8-12:   One Piece : Short Version  ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)


G = nx.DiGraph()
G.add_edges_from([('魯夫','卡普'), ('魯夫','羅傑'), ('索隆','魯夫'),('索隆','布魯克'), ('香吉士','娜美'), ('魯夫','羅賓'),
                    ('魯夫','喬巴'), ('魯夫','香吉士'), ('娜美','魯夫'), ('魯夫','娜美'),('喬巴','羅賓'),('魯夫','布魯克'), ('魯夫','索隆')])
layout = nx.spring_layout(G, seed=289)
measures =nx.degree_centrality(G)
nodes = nx.draw_networkx_nodes(G, layout, node_size=2000,  
                               node_color=list(measures.values()),
                               nodelist=measures.keys())
nx.draw_networkx_labels(G, layout, font_family='SimHei',font_color="white")
nx.draw_networkx_edges(G, layout)
plt.title('DEGREE_CENTRALITY')
plt.colorbar(nodes)
plt.axis('off')
plt.show()
# https://networkx.org/documentation/stable/reference/generated/networkx.drawing.nx_pylab.draw_networkx_nodes.html

sna = pd.DataFrame(dict(
    DEGREE = dict(G.degree),
    DEGREE_CENTRALITY = nx.degree_centrality(G),
    EIGENVECTOR = nx.eigenvector_centrality(G),
    CLOSENESS_CENTRALITY = nx.closeness_centrality(G),
    BETWEENNESS_CENTRALITY = nx.betweenness_centrality(G),
    CLUSTCOEF = nx.clustering(G),
 ))
sna_sort = sna.sort_values(by=['DEGREE_CENTRALITY'],ascending=False)
# print(sna)
print(sna_sort)

