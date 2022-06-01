# -*- coding: utf-8 -*-
"""
根據以下資料 :
Edge Data (for Both Directed and Undirected graphs) :
    ([(2, 3), (3, 2), (4, 1), (4, 2), (5, 2), (5, 4),
    (5, 6), (6, 2), (6, 5), (7, 2), (7, 5), (8, 2),
    (8, 5), (9, 2), (9, 5), (10, 5), (11, 5)])
    
Weight Data (for Directed graphs) :
    {1: [0.1, 0.9], 2: [0.4, 0.8], 3: [0.8, 0.9], 4: [0.15, 0.55],
    5: [0.5, 0.5], 6: [0.8, 0.5], 7: [0.22, 0.3], 8: [0.30, 0.27],
    9: [0.38, 0.24], 10: [0.7, 0.3], 11: [0.75, 0.35]}
    
請顯示出所有
1) 無向圖的degree_centrality，eigenvector_centrality，
betweenness_centrality，closeness_centrality，Clustering 
Coefficients 及 katz_centrality等

2) 定向圖的 in_degree, out_degree()， pageRank等 指標評估值及相關圖
形。

"""
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# G = nx.Graph() 
G = nx.Graph() 

edgeData = [(2, 3), (3, 2), (4, 1), (4, 2), (5, 2), (5, 4),
            (5, 6), (6, 2), (6, 5), (7, 2), (7, 5), (8, 2),
            (8, 5), (9, 2), (9, 5), (10, 5), (11, 5)]

weightData = {  1: [0.1, 0.9], 2: [0.4, 0.8], 3: [0.8, 0.9], 4: [0.15, 0.55],
                5: [0.5, 0.5], 6: [0.8, 0.5], 7: [0.22, 0.3], 8: [0.30, 0.27],
                9: [0.38, 0.24], 10: [0.7, 0.3], 11: [0.75, 0.35]  }

G.add_edges_from(edgeData)
                                  
print (G.nodes())                                      
print (G.edges())                                       
print (G.number_of_edges())  
print("All Conncections = ", G.edges()) 

# 1
# print("Degree = ",G.degree())
# print("Max Distances = ", nx.eccentricity(G) ) 
# print("Average Cluster =", nx.average_clustering(G))
# print("程度中心性 = ", nx.degree_centrality(G))
# print("特徵向量中心性 = ", nx.eigenvector_centrality(G))
# print("仲介中心性 = ", nx.betweenness_centrality(G))
# print("接近中心性 = ", nx.closeness_centrality(G))
# print("集群係數 = ", nx.clustering(G))
# print("卡茨中心性 = ", nx.katz_centrality(G))
sna = pd.DataFrame(dict(
    DEGREE = dict(G.degree),
    DEGREE_CENTRALITY = nx.degree_centrality(G),
    EIGENVECTOR = nx.eigenvector_centrality(G),
    CLOSENESS_CENTRALITY = nx.closeness_centrality(G),
    BETWEENNESS_CENTRALITY = nx.betweenness_centrality(G),
    CLUSTCOEF = nx.clustering(G),
    KATZ = nx.katz_centrality(G)
 ))
sna_sort = sna.sort_values(by=['DEGREE_CENTRALITY'],ascending=False)
# print(sna)
print(sna_sort)

#2
in_degrees = G.in_degree()
out_degrees = G.out_degree()
print("In Degree = ", in_degrees)
print("Out Degree = ", out_degrees)
grades = {
    "in_degrees": in_degrees,
    "out_degrees":out_degrees
}
df = pd.DataFrame(grades)
df.columns = ["in_degrees", "out_degrees"]
print(df)

measures = nx.pagerank(G, alpha=0.85)
nodes = nx.draw_networkx_nodes(G, weightData, node_size=500, cmap=plt.cm.plasma, 
                                   node_color=list(measures.values()),
                                   nodelist=measures.keys())
nx.draw_networkx_labels(G, weightData, font_color="white", font_size=12)
# nodes.set_norm(mcolors.SymLogNorm(linthresh=0.01, linscale=1, base=10))
# labels = nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, weightData)
#edges = nx.draw_networkx_edges(G, pos)
plt.title('Graph PageRank')
plt.colorbar(nodes)
plt.axis('off')
plt.show()
