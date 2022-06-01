

# -*- coding: utf-8 -*-   [   Code 8-1 :  Undirected Graph  ( Symmetric Networks  Graph) ]  ~~~~~~~~~~~~~~~~

import networkx as nx
G = nx.Graph()       # Undirected Graph (無向圖)                                                              
G.add_node('A')                                       
G.add_edge('A','D')                                    
G.add_edge('A','C')                                    
G.add_edge('B','D') 
G.add_edge('D','B') 
G.add_edge('B','E')
G.add_edge('C','E')
print (G.nodes())                                      
print (G.edges())                                       
print (G.number_of_edges())   