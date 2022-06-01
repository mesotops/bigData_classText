
# -*- coding: utf-8 -*-   [   Code 8-6 :  In & Out Degree     ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#
import networkx as nx
G = nx.DiGraph()                                        
G.add_edge('A','D')                                    
G.add_edge('A','C')                                    
G.add_edge('B','D') 
G.add_edge('D','B') 
G.add_edge('B','E')
G.add_edge('C','E')
print(nx.info(G))

in_degrees = G.in_degree() # dictionary node:degree
out_degrees = G.out_degree()
print("In Degree = ", in_degrees)
print("Out Degree = ", out_degrees)


