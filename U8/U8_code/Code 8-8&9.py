
# -*- coding: utf-8 -*-   [   Code 8-8 & 8-9 :  FB file Sorting +  Measures   ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#
#
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

G_sn = nx.read_edgelist("C:/Pyfiles/sn_test.txt", create_using = nx.Graph(), nodetype=int)
print(nx.info(G_sn))
pos = nx.spring_layout(G_sn, seed=6589)
betCent = nx.betweenness_centrality(G_sn, normalized=True, endpoints=True)
node_color = [20000.0 * G_sn.degree(v) for v in G_sn]
node_size =  [v * 10000 for v in betCent.values()]
plt.figure(figsize=(12,12))
nx.draw_networkx(G_sn, pos=pos, with_labels=False,
                 node_color=node_color,
                 node_size=node_size )
plt.axis('off')

sna = pd.DataFrame(dict(
    DEGREE = dict(G_sn.degree),
    DEGREE_CENTRALITY = nx.degree_centrality(G_sn),
    EIGENVECTOR = nx.eigenvector_centrality(G_sn),
    CLOSENESS_CENTRALITY = nx.closeness_centrality(G_sn),
    BETWEENNESS_CENTRALITY = nx.betweenness_centrality(G_sn),
    CLUSTCOEF = nx.clustering(G_sn),
 ))
sna_sort = sna.sort_values(by=['DEGREE_CENTRALITY'],ascending=False)
# print(sna)
print(sna_sort)
