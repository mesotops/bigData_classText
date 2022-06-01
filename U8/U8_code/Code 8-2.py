# -*- coding: utf-8 -*-   [   Code 8-3 :   Directed Graph (Asymmetric Networks  Graph)  ]  ~~~~~~~~~~~~~~~~~
#   
# 
import networkx as nx
G = nx.DiGraph()       # Directed Graph (有向圖)                                                                
G.add_edge('A','D')                                    
G.add_edge('A','C')                                    
G.add_edge('B','D') 
G.add_edge('D','B') 
G.add_edge('B','E')
G.add_edge('C','E')
print (G.nodes())                                      
print (G.edges())                                       
print (G.number_of_edges())   

