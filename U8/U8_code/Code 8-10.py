# -*- coding: utf-8 -*-   [   Code 8-10 :     PageRank   ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

DiG = nx.DiGraph()
DiG.add_edges_from([(2, 5), (4, 7), (3, 1), (4, 2), (5, 3), (1, 4),
                    (5, 6), (6, 2), (6, 5), (7, 4), (7, 6), (8, 2),
                    (8, 5), (9, 2), (8, 9), (10, 5), (11, 5)])
dpos = {1: [0.3, 0.6], 2: [0.5, 0.7], 3: [0.25, 0.9], 4: [0.33, 0.55],
        5: [0.4,  0.5], 6: [0.3,  0.5], 7: [0.2, 0.6], 8: [0.3, 0.8],
        9: [0.8, 0.4], 10: [0.6,  0.3], 11: [0.7, 0.5]}

# plt.figure(figsize=(8,8)) 
measures = nx.pagerank(DiG, alpha=0.85)
nodes = nx.draw_networkx_nodes(DiG, dpos, node_size=500, cmap=plt.cm.plasma, 
                                   node_color=list(measures.values()),
                                   nodelist=measures.keys())
nx.draw_networkx_labels(DiG, dpos, font_color="white", font_size=12)
# nodes.set_norm(mcolors.SymLogNorm(linthresh=0.01, linscale=1, base=10))
# labels = nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(DiG, dpos)
#edges = nx.draw_networkx_edges(G, pos)
plt.title('DiGraph PageRank')
plt.colorbar(nodes)
plt.axis('off')
plt.show()
