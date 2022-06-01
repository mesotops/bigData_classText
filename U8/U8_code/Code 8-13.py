
# -*- coding: utf-8 -*-   [   Code 8-13 :     FB file Sorting +  Measures +  SNA Figure      ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#
# import matplotlib
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# matplotlib.font_manager._rebuild()

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_columns', None)

# For Layout Sytle
# print([x for x in nx.__dir__() if x.endswith('_layout')])

G_sn = nx.read_edgelist("C:/Pyfiles/sn_test.txt", create_using = nx.Graph(), nodetype=int)
print(nx.info(G_sn))

def draw(G, pos, measures, measure_name):
    plt.figure(figsize=(12,12))
    nodes = nx.draw_networkx_nodes(G, pos, node_size=100, cmap=plt.cm.plasma, 
                                   node_color=list(measures.values()),
                                   nodelist=measures.keys())
    nodes.set_norm(mcolors.SymLogNorm(linthresh=0.01, linscale=1, base=10))
    nx.draw_networkx_labels(G, pos,font_color="white")
    nx.draw_networkx_edges(G, pos)
    #edges = nx.draw_networkx_edges(G, pos)

    plt.title(measure_name)
    plt.colorbar(nodes)
    plt.axis('off')
    plt.show()
    
pos = nx.spring_layout(G_sn, seed=6589)
#pos = nx.circular_layout(G_sn)

sna = pd.DataFrame(dict(
    DEGREE = dict(G_sn.degree),
    DEGREE_CENTRALITY = nx.degree_centrality(G_sn),
    EIGENVECTOR = nx.eigenvector_centrality(G_sn),
    CLOSENESS_CENTRALITY = nx.closeness_centrality(G_sn),
    BETWEENNESS_CENTRALITY = nx.betweenness_centrality(G_sn),
    KATZ = nx.katz_centrality(G_sn),
    CLUSTCOEF = nx.clustering(G_sn),
 ))
sna_sort = sna.sort_values(by=['DEGREE_CENTRALITY'],ascending=False)
# print(sna)   
print(sna_sort)


# Draw Figures for Different Measures 
draw(G_sn, pos, nx.degree_centrality(G_sn), 'Degree Centrality')            # Degree Centrality
draw(G_sn, pos, nx.betweenness_centrality(G_sn), 'Betweenness Centrality')  # Betweenness Centrality
draw(G_sn, pos, nx.closeness_centrality(G_sn), 'Closeness Centrality')      # Closeness Centrality
draw(G_sn, pos, nx.eigenvector_centrality(G_sn), 'Eigenvector Centrality')     #Eigenvector Centrality
draw(G_sn, pos, nx.katz_centrality(G_sn, alpha=0.1, beta=1.0), 'Katz Centrality') # Katz Centrality

# draw(DiG, dpos, nx.in_degree_centrality(DiG), 'DiGraph Degree Centrality')
# draw(DiG, dpos, nx.pagerank(DiG, alpha=0.85), 'DiGraph PageRank')
