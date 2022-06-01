
# -*- coding: utf-8 -*-   [   Code 8-4 :   Edge weight  (1) ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
G.add_weighted_edges_from([('B','E',2.5),('C','E',3)])
print (G.nodes())                                      
print (G.edges())                                       
print (G.number_of_edges())   
print (G.get_edge_data('C','E'))

