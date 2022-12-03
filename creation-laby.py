#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#importation des bibliothèques
import networkx as nx
import matplotlib.pyplot as plt
import random

"""
Fonction : creer_labyrinthe()
Format des paramètres : nombre de lignes, nombre de colonnes[, coefficient de dégénération]
Commentaire: le coefficient de dégénération peut ne pas être renseigné.
Entrées : nombre de lignes, nombre de colonnes et coefficient de dégénération sont des entiers.
coefficient de dégénération correspond au pourcentage d’arêtes qui seront détruites.
Sortie : Graphe NetworkX (Représentation du labyrinthe)
Postcondition : Le labyrinthe créé doit être connexe. Sinon, la recherche de sortie va planter!
"""
def creer_labyrinthe(nb_lignes, nb_colonnes, degenerer=30):
    #Création du graphe
    G = nx.grid_2d_graph(nb_lignes, nb_colonnes)
    #Génération des arêtes
    for (u,v) in G.edges():
        G[u][v]['weight'] = random.randint(1,10)
    #Dégénération
    if degenerer > 0:
        for (u,v) in G.edges():
            if random.randint(1,100) <= degenerer:
                G.remove_edge(u,v)
    return G

    
    
if __name__ == "__main__":
    # Lance le test de la fonction creer_labyrinthe()
    Labyrinthe = creer_labyrinthe(5, 6, 30)
    m = nx.adjacency_matrix(Labyrinthe)
    # Affichage du graphe avec matplotlib
    nx.draw(Labyrinthe, with_labels=True)
    plt.show()
    print(m)