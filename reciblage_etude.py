#!/bin/env python3
# -*- coding: utf-8 -*-
# Evaluer les conséquences d'un reciblage de contrôle de qualité.
"""Reciblage d'un controle interne.

Permet dévaluer les conséquensces d'un reciblage de CQI en fonction de
l'évaluation par rapport à un groupe de pairs."""
import lib_ctrl_graph

class EvalReciblage():
    """Evaluer les conséquences d'un reciblage de contrôle"""

    version = "Programme : " +__file__+" v:1.1 du 11/06/2016"
    def __init__(self, m_theo, cv_theo, m_labo, cv_labo, m_groupe, cv_groupe,
                 titre='Titre'):
        """Initialisation des valeurs.

theo désigne les valeurs cibles,
labo les valeurs mesurées par le laboratoire,
groupe les valeurs du groupe de pair"""

        self.titre = titre
        self.m_theo = m_theo
        self.cv_theo = cv_theo
        self.m_labo = m_labo
        self.cv_labo = cv_labo
        self.m_groupe = m_groupe
        self.cv_groupe = cv_groupe
        self.low_labo = None
        self.high_labo = None
        self.low_groupe = None
        self.high_groupe = None

        self.actualise()

    def actualise(self):
        """Exécute les calculs"""

        self.sd_labo = self.m_labo * self.cv_labo / 100
        self.sd_groupe = self.m_groupe * self.cv_groupe / 100
        self.sd_theo = self.m_theo * self.cv_theo / 100
        self.low_theo = self.m_theo - 2 * self.sd_theo
        self.high_theo = self.m_theo + 2 * self.sd_theo
        self.m_recal = self.m_labo
        self.low_recal = self.m_recal - 2 * self.sd_theo
        self.high_recal = self.m_recal + 2 * self.sd_theo

    def get_recap(self):
        """Revoie un récapitulatif"""

        output = []
        output.append(self.version)
        output.append('-' * 30)
        output.append("M théo = \t{}".format(self.m_theo))
        output.append("CV théo = \t{}".format(self.cv_theo))
        output.append("SD théo = \t{}".format(round(self.sd_theo, 3)))
        output.append('-' * 30)

        output.append("M labo = \t{}".format(self.m_labo))
        output.append("CV labo = \t{}".format(self.cv_labo))
        output.append("SD labo = \t{}".format(round(self.sd_labo, 3)))
        output.append('-' * 30)

        output.append("M groupe = \t{}".format(self.m_groupe))
        output.append("CV groupe = \t{}".format(self.cv_groupe))
        output.append("SD groupe = \t{}".format(round(self.sd_groupe, 3)))
        output.append('-' * 30)

        self.low_labo = self.m_labo - 2 * self.sd_labo
        self.high_labo = self.m_labo + 2 * self.sd_labo
        if self.low_labo < self.low_theo:
            output.append("!  mal ciblé ! : plus de 2,5 % des ctrl sont trop bas")
            output.append("limite basse labo : {} < limite basse théorique : {}"
                          .format(str(self.low_labo), str(self.low_theo)))
        if  self.high_labo > self.high_theo:
            output.append("!  mal ciblé ! : plus de 2,5 % des ctrl sont trop haut")
            output.append("limite haute labo : {} > limite haute théorique : {}"
                          .format(str(self.high_labo), str(self.high_theo)))

        self.low_groupe = self.m_groupe - 3 * self.sd_groupe
        self.high_groupe = self.m_groupe + 3 * self.sd_groupe
        output.extend(["95% des valeurs du labo sont donc entre :" +str(round(self.low_labo, 3))+
                       " et "+ str(round(self.high_labo, 3))])
        output.extend(["99.6% des valeurs des moyennes du groupe sont entre :"
                       +str(round(self.low_groupe, 3))+
                       " et "+ str(round(self.high_groupe, 3))])
        return output

    def illustrate(self):
        """Affiche un graphique de synthèse"""

        gr = lib_ctrl_graph.GrapheCtrl(self.titre, output_filename='output.png')
        gr.placer(self.m_theo, self.low_theo, self.high_theo, 1, style='b',
                  label='Théo')
        gr.placer(self.m_labo, self.low_labo, self.high_labo, 2, style='b',
                  label='Labo')
        gr.placer(self.m_groupe, self.low_groupe, self.high_groupe, 3,
                  style='b', label='Groupe')
        gr.placer(self.m_recal, self.low_recal, self.high_recal, 4,
                  style='b', label='Reciblage')
        x_min, x_max, y_min, y_max = lib_ctrl_graph.plt.axis()
        lib_ctrl_graph.plt.axis([x_min, x_max, y_min * 0.95, y_max])
        gr.affiche()

def create_pdf():
    """Crée un pdf contenant le graphe élaboré par self.illustrate()"""
    import lib_reportlab
    filename = "rapport.pdf"
    print("\nCréation du pdf : {}".format(filename))

    rapport = lib_reportlab.MonRapportReportLab(filename)
    rapport.inserer_graphe('output.png')
    rapport.inserer_texte(ex.get_recap())
    rapport.clore()

if __name__ == '__main__':
    """Exemple d'utilisation.

On saisit les variables ici."""

    ex = EvalReciblage(m_theo=46.63,
                       cv_theo=3.4,
                       m_labo=45.55,
                       cv_labo=2.15,
                       m_groupe=45.168,
                       cv_groupe=3.41,
                       titre="Lipase niveau 1 25/06/2016")
    for line in ex.get_recap():
        print(line)
    ex.illustrate()
    create_pdf()
