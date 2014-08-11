# -*- coding: utf-8 -*-
"""
Created on Mon Jul 14 23:31:24 2014

@author: Nikhil
"""

import networkx as nx
import matplotlib.pyplot as plt
import csv

def test():
    G=nx.DiGraph()
    G.add_nodes_from([124234,223423,3234234, 1, 2, 3, 3])
    G.add_edges_from([(1,2),(1,3),(2,1)])
    print G.nodes()
    print G.edges()
    nx.draw_networkx(G)
    plt.show()
    
def visualizeGraph(graphFileName):
    with open(graphFileName, 'r') as graph:
        G=nx.DiGraph()
        graphreader = csv.reader(graph, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in graphreader:             
            intRow = []
            for x in row:
                if x.isdigit():
                    intRow.append(int(x))
            G.add_nodes_from(intRow)
            if len(intRow)>1:
                for x in intRow[1:]:
                    G.add_edge(intRow[0], x)
        print G.nodes()
        print G.edges()
        nx.draw_circular(G)
        plt.show()
        nx.draw_spring(G)
        plt.show()
        nx.draw_networkx(G)
        plt.show()
 
visualizeGraph('graph_4.csv')
print 'done'