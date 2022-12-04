#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#VERSION SANS LES AMELIORATIONS

import networkx as nx

class Pile:
    def __init__(self):
        self.p = []
    def empile(self,e):
        self.p.append(e)
    def depile(self):
        return self.p.pop()
    def vide(self):
        return len(self.p) == 0

def chercher_dfs(laby:nx.Graph, source:int = None, destination:int = None)->list:
    """ Cherche le chemin le plus court entre les sommets source et destination
        selon le parcours en profondeur.
    """
    nodes = list(laby.nodes())
    edges = list(laby.edges())

    if source == None:
        source = nodes[0]
    if destination == None:   
        destination = nodes[-1]
    
    node = source
    
    visited = []
    p = Pile()
    p.empile(node)

    while not p.vide() and node != destination:
        node = p.depile()
        if node not in visited:
            visited.append(node)
            unvisited = [n for n in laby[node] if n not in visited]
            for i in unvisited:
                p.empile(i)
            

    return visited
