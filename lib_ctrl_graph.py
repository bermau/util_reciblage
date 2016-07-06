#!/bin/env python3
# Le doctests de ce fichier sont génés par les messages de la sortie
# standard
# v2 : OK sur les 3 tests.

"""Représentation de la moyenne +/- 2 ou 3 SD

Dans l'exemple ci dessous, je lance plusieurs lignes de doctest.

Ce module sert à tracer des qraphes avec matplolib.
Sur l'axe des X, les donnénes sont des qualitatives
Sur l'axe des Y, les données sont quantitatives, avec indication de
la moyenne et des bornes inf et sup.
Le réglage de la zone intéressante est automatique.
On place les points avec placer(moyenne, min, max, colonne, style, label)
On peut placer les étiquettes en haut ou en bas des données.

Exemples:

Ci dessous, les étiquettes sont en dessous des données.
>>> G = GrapheCtrl(output_filename='exemple.png', label_pos='down')
>>> G.placer(3, 1.8, 3.4, 1, style='b--', label='nos données')
>>> G.placer(4, 2.2, 4.4, 2, label='jeux 2')
>>> G.placer(3.5, 3.1, 3.8, 3, style='g-.', label='données 3')
>>> G.affiche()

Les étiquettes seront au dessus, si label_pos vaut 'up'

>>> G = GrapheCtrl(output_filename='exemple.png', label_pos='up')
>>> G.placer(3, 1.8, 3.4, 1, style='b--', label='nos_données')
>>> G.placer(4, 2.2, 4.4, 2, label='jeux 2')
>>> G.placer(3.5, 3.1, 3.8, 3, style='g-.', label='données 3')
>>> G.affiche()

Un essai avec d'autres valeurs et 'up'

>>> G = GrapheCtrl(output_filename='exemple.png', label_pos='up')
>>> G.placer(-3, -4.8, -2.4, 1, style='r--', label='etiquette 1')
>>> G.placer(4, 2.2, 4.4, 2, label='jeux 2')
>>> G.placer(3.5, 3.1, 3.8, 3, style='g-.', label='données 3')
>>> G.placer(3.5, 3.1, 3.8, 4, style='g-.', label='données 3')
>>> G.affiche()
"""
from matplotlib import pyplot as plt

class GrapheCtrl():
    """Un graphique de synthèse des valeurs de CQ"""
    def __init__(self, titre='Synthèse', output_filename='graphe.png',
                 label_pos='down'):
        """Déclarations"""
        self.y_min = 0
        self.y_max = 0
        self.y_min_ax = 0.5
        self.y_max_ax = 10

        self.nb_points = 0
        self.labels = []
        self.label_position = label_pos
        self.ecart_label = 0.10
        self.ecart_cadre = 0.08

        self.output_filename = output_filename

        plt.figure(1)
        plt.title(titre)
        plt.xlabel('Conditions')
        plt.ylabel('Valeurs')


    def placer(self, moy, inf, sup, position, style='r', label=''):
        """Représente 3 points sur une position entière"""
        # print("placer un point", (moy, inf, sup, position))
        dec = 0.1
        plt.plot([position-dec, position+dec], [moy, moy], style)
        plt.plot([position-dec, position+dec], [inf, inf], 'r')
        plt.plot([position-dec, position+dec], [sup, sup], 'r')
        # Retenir les labels, qui seront affichés plus tard.
        self.labels.append((position, label))
        plt.grid(True)
        # Récupérer le minimum, maximum
        if self.nb_points == 0:
            self.y_min = inf
            self.y_max = sup
        else:
            self.y_min = min(self.y_min, inf)
            self.y_max = max(self.y_max, sup)
        self.nb_points += 1
        # print("Ajout d'un point : valeur de y_min, y_max", self.y_min, self.y_max)
        # print("y_min, y_max",(self.y_min, self.y_max))
        # print()
        # return None
    def affiche(self):

        """Placer les commentaires, puis créer le fichier et l'affiche"""
        # print(self.labels)
        y_range = self.y_max - self.y_min
        if self.label_position == 'down':
            # hauteur =  self.y_min )
            hauteur = self.y_min - (self.ecart_label * y_range)
            self.y_min_ax = hauteur
            self.y_max_ax = self.y_max
        else:
            #import pdb
            #pdb.set_trace()
            hauteur = self.y_max  + (self.ecart_label * y_range)
            self.y_max_ax = hauteur
            self.y_min_ax = self.y_min
        print("y_min_ax, y_max_ax", (self.y_min_ax, self.y_max_ax))

        # place les commentaires
        for position, label in self.labels:
            plt.text(position, hauteur, label, horizontalalignment='center')
        # Gérer l'affichage automatique
        x_min, x_max = plt.axis()[0:2]
        print("y_min, y_max", (self.y_min, self.y_max))
        # print("y mix max des axes : ",(self.y_min_ax, self.y_max_ax))
        plt.axis([x_min, x_max, self.y_min_ax - self.ecart_cadre * hauteur,
                  self.y_max_ax + self.ecart_cadre * hauteur])
        # sauver puis afficher
        plt.savefig(self.output_filename)
        plt.show()

def _test():
    "self-test routine"
    # load the doctest module, part of the std Python API
    import doctest
    # invoke the testmod function that will parse
    # the whole content of the file, looking for
    # docstrings and run all tests they contain
    doctest.testmod(verbose=False)
if __name__ == '__main__':
    _test()
    G = GrapheCtrl(output_filename='exemple.png', label_pos='up')
    G.placer(-3, -4.8, -2.4, 1, style='r--', label='etiquette 1')
    G.placer(4, 2.2, 4.4, 2, label='jeux 2')
    G.placer(3.5, 3.1, 3.8, 3, style='g-.', label='données 3')
    G.placer(3.5, 3.1, 3.8, 4, style='g-.', label='données 3')
    G.affiche()


