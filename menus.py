# -*- coding: utf-8 -*-
from tkinter import *  # (sur python 3.1 le module s'appèle tkinter)
# import bm_u, bm_u_for_ftp




class MenuBar(Frame):
    # tres important : transmettre boss !!
    """Définition de toute la Barre des menus déroulant"""
    def __init__(self, boss=None):
        Frame.__init__(self, boss, borderwidth =2)  
        # Menu Fichier
        menuFichier=Menubutton(self, text='Fichier', underline=0)
        menuFichier.pack(side=LEFT)
        menu1=Menu(menuFichier)
        menu1.add_command(label='Quitter', underline=0, command=boss.quit)
        menuFichier.configure(menu=menu1)

        # Menu Divers et tests.
        menuTests=Menubutton(self, text='Tests',underline=0)
        menuTests.pack(side=LEFT,padx=5)
        menuitems4=Menu(menuTests)
        menuitems4.add_separator()
        menuitems4.add_command(label='Version', underline=0,command=boss.afficherVersion)
        menuTests.configure(menu=menuitems4)


