#!/bin/env python3
"""Un exemple avec un peu de tout

https://www.reportlab.com/docs/reportlab-userguide.pdf

Le but est de créer un pdf avec un graphe en haut et une
explication textuelle en bas.
Le texte est très basique. Je suis obligé de le filtrer
avec une fonction (très limitée) pour éliminer les \n et les \t.
"""

from reportlab.pdfgen import canvas

def clean_line(line):
    """return a line or a list of lines"""
    # piège : replace() ne remplace pas l'instance mais renvoye
    # une chaîne modifiée
    s=line.replace("\n","").replace("\t","")
    return s
 
def clean_strings(lst_strings):
    """return a string without \n \t and other
    # Dans le doctest ci dessous, les tabulation et retour lignes
    # sont notés avec un avec un double antislash
    >>> clean_strings(["ceci \\test ", "une \\nligne"])
    ['ceci est ', 'une ligne']
    
"""
    buf = [ clean_line(line) for line in lst_strings ]
    return buf
 


class MonRapportReportLab():

    def __init__(self, filename):
        self.can=canvas.Canvas(filename)
        
    def inserer_texte(self,input_lst_lines=[]):
        """Ecrire plusieurs lignes de suite après avoir supprimé
        les retours lignes et tabulations"""
        lst_lines=clean_strings(input_lst_lines)
        textobject = self.can.beginText(20,450)
        for line in lst_lines:
            textobject.textLine(line)
        self.can.drawText(textobject)

    def inserer_graphe(self, filename):

        # attention : données en pixels
        self.can.drawImage(filename, 20, 400, width=500, height=503,
                           preserveAspectRatio=True)

    def clore(self):
        # self.can.showPage()
        self.can.save()


if __name__=='__main__':
    import doctest
    doctest.testmod()
    
    rapport = MonRapportReportLab("exemple_lib_myreportlab.pdf")
    rapport.inserer_graphe(r'example.png')
    
    t=[]
    t.append("ceci est une \n ligne, initialement avec des tabulations.")
    t.append("une \n autre avec un retour ligne")
    t.append("encore une autre.")

    rapport.inserer_texte(t)
    rapport.clore()

