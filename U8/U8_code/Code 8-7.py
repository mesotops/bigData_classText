# -*- coding: utf-8 -*-   [   Code 8-7 :   Centrality  ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# 
import networkx as nx
G = nx.Graph()
G.add_edge('A','D')                                    
G.add_edge('A','C')                                    
G.add_edge('B','D') 
G.add_edge('D','B') 
G.add_edge('B','E')
G.add_edge('C','E')
print("All Conncections = ", G.edges()) 
print("Degree = ",G.degree())
print("Max Distances = ", nx.eccentricity(G) ) 
print("Average Cluster =", nx.average_clustering(G))
print("程度中心性 = ", nx.degree_centrality(G))
print("仲介中心性 = ", nx.betweenness_centrality(G))
print("接近中心性 = ", nx.closeness_centrality(G))
print("特徵向量中心性 = ", nx.eigenvector_centrality(G))


