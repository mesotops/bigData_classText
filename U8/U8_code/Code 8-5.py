
# -*- coding: utf-8 -*-   [   Code 8-5 :  MultiGraph   ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#
import networkx as nx
# G = nx.Graph()
G = nx.MultiGraph()
G.add_edge('A','B', relation ='colleague')
G.add_edge('A','B', relation='brother')
G.add_edge('B','C', relation='friend')
G.add_edge('D','C', relation='couple')
print(G.edges())


