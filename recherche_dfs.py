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

def recursive_dfs(graph, node,destination):
    def rec(graph, node,destination, visited=None):

        if visited is None:
            visited = []

        if node not in visited :
            visited.append(node)

        if node == destination:
            return visited

        unvisited = [n for n in graph[node] if n not in visited]

        for node in unvisited:
            rec(graph, node, destination, visited)

        return visited
    solution_nodes = rec(graph, node,destination)

    solution_edges = []

    for i in range(len(solution_nodes)-1):
        solution_edges.append((solution_nodes[i],solution_nodes[i+1]))
            

    return solution_edges

    
def chercher_dfs(laby:nx.Graph, source:int = None, destination:int = None)->list:
    """ Cherche le chemin le plus court entre les sommets source et destination
        selon le parcours en profondeur.
    """
    # Initialisation des sommets source et destination s'ils ne sont pas renseignés
    # Récupère la liste des sommets
    nodes = list(laby.nodes())
    # Si source n'est pas renseigné, alors on impose source = 0
    if source == None:
        source = nodes[0]
    # Si destination n'est pas renseigné, alors on impose destination = dernier sommet
    if destination == None:   
        destination = nodes[-1]
    
    node = source
    
    visited = []
    solution_nodes = []
    solution_edges = []
    p = Pile()
    p.empile(node)
    
    while not p.vide():
        node = p.depile()
        
        if node not in visited:
            visited.append(node)
            unvisited = [n for n in laby[node] if n not in visited]
            for i in unvisited:
                p.empile(i)
        if node == destination:
            solution_nodes = visited.copy()


    for i in range(len(solution_nodes)-1):
        solution_edges.append((solution_nodes[i],solution_nodes[i+1]))
            

    return solution_edges

if __name__ == "__main__":
    # Création du labyrinthe de test
    aretes = [(0, 1), (0, 4), (1, 0), (1, 5), (2, 6), (3, 7), (4, 0), (4, 5), (5, 1) , \
     (5, 4), (5, 6), (5, 9), (6, 2), (6, 5), (6, 7), (6, 10), (7, 3), (7, 6), (8, 9),\
     (9, 5), (9, 8), (9, 10), (10, 6), (10, 9), (10, 11), (11, 10)]
    colonnes = 4
    lignes = 3
    nb_sommets = colonnes * lignes
    noeuds = list(range(nb_sommets))
    Labyrinthe = nx.Graph()
    Labyrinthe.add_nodes_from(noeuds)
    Labyrinthe.add_edges_from(aretes)
    # Lance le test de la fonction afficher_labyrinthe()
    #afficher_labyrinthe(Labyrinthe, colonnes, lignes)
    chemin_dfs =chercher_dfs(Labyrinthe)
    print(chemin_dfs,recursive_dfs(Labyrinthe,noeuds[0],noeuds[-1]))
