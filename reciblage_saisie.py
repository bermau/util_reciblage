#!/bin/env python
"""Un frontal graphique pour demander de saisir des valeurs"""
#
##    nous=EvalReciblage(m_theo=0.3106,
##                       cv_theo=5.1,
##                       m_labo=0.297,
##                       cv_labo=3.97,
##                       m_groupe=0.297,
##                       cv_groupe=4.7,
##                       titre="Préalb niveau 2 08/08/2016"
##                       )

CONC = "MPL"

data = [
   [ 'titre','Titre', ],
   [ 'm_theo','Moyenne théorique dans {}'.format(CONC), ],
   [ 'cv_theo','CV théorique dans {}'.format(CONC), ],
   [ 'm_theo','Moyenne obtenue dans le laboratoire', ],
   [ 'm_theo','CV obtenue par le laboratoire', ],
   [ 'm_theo','Moyenne du groupe de pairs', ],
   [ 'm_theo','CV du groupe de pairs', ],
    ]


import tkinter as tk
import menus
import essai_lib_labelled_entry

class Graphe(tk.Frame):
    """Graphe central avec surtout le graphique ; 
    """
    def __init__(self,boss=None):
        tk.Frame.__init__(self,boss)
        self.boss = boss # indispensable ? pour réutiliser boss dans les méthodes de la classe
        self.largeur = boss.largeur
        self.hauteur = boss.hauteur
        self.can = tk.Canvas(self, bg='white', width=boss.largeur,
                             height=boss.hauteur, borderwidth=2)
        self.can.grid(row=0, column=0)
        
class SidePanel(tk.Frame):
    def __init__(self, root):
        self.frame1=tk.Frame.__init__(self,root)
        self.frame2 = tk.Frame(self, root )
        self.frame2.grid(sticky=tk.N)
        self.plotBut = tk.Button(self.frame2, text="Version")
        self.plotBut.grid(sticky=tk.W)
        self.clearButton = tk.Button(self.frame2, text="Clear")
        self.clearButton.grid(sticky=tk.W)

        self.titre
               
class ViewType1(tk.Frame):
    
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        # La fenêtre
        self.largeur, self.hauteur=800,400 # size of the window. 
        self.master.title("Interface général")
        # construction des différentes zones de la fenêtre
        self.leMenu = menus.MenuBar(self) # barre de menu réroulant en haut
        self.leGraphe = Graphe(self) # le graphique
        self.sidepanel = SidePanel(self) # panneau en haut (à déplacer)
        # positionnements des élements déclarés ci-dessus
##        self.leMenu.grid(row=1,column=1, sticky=tk.W, columnspan=10)
##        self.leGraphe.grid(row=2, column=2, columnspan=7,sticky=tk.W)
##        self.sidepanel.grid(row=2,column=3) # pas de méthode grid()

        self.leMenu.grid(row=1, column=3, sticky=tk.W)
        self.leGraphe.grid(row=2, column=3)
        self.sidepanel.grid(row=2,column=2) # pas de méthode grid()
        # placer les objets avant de commencer
        self.grid()



    def afficherVersion(self):
        msg = "Version du programme: 0.10 \nnov 2015"
        s = "Version de Tk :{tk} \nVersion de Tcl :{tcl}".format(tk=tk.TkVersion,tcl=tk.TclVersion)
        msg = msg + "\n" + s
        # msg=self.extraireVersionDuFichier("/home/bertrand/Bureau/ctrl_partiel/gestcqe_31/readme2.txt")
        # msg=self.extraireVersionDuFichier("readme.txt")
        print(msg) # pose problème dans le terminal windows. )
        tk.messagebox.showinfo("Version", msg)

    def quit(self):
        print("Bye...")
        c.tkroot.destroy()

class Controller():
    def __init__(self):
        self.tkroot = tk.Tk()
        # self.model=encours.Encours(filename=DEFAULT_INPUT+"fi59",encoding="latin1")
        self.view = ViewType1(self.tkroot)
        # ici il faut définir les menus.
        self.view.sidepanel.plotBut.bind("<Button>",self.aff_version)
        # Dans la ligne ci-dessous, on indique la podition du menu.
        self.view.leMenu.tool_menu.entryconfig(1, command=self.downloadFi58)
        self.view.leMenu.tool_menu.entryconfig(2, state=tk.DISABLED)

    def aff_version(self,event):
        self.view.afficherVersion() # idem mais en mode graphique.

    def downloadFi58(self):
        bm_u_for_ftp.downloadfiXX(58)

    def run(self):
        self.tkroot.title("Utilitaire pour le reciblage.")
        self.tkroot.deiconify()
        self.tkroot.mainloop()  



if __name__ == '__main__':
    c = Controller()  
    c.run()
    # ou plus simple :
    # Controller().run()  
