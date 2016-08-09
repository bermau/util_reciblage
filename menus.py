# -*- coding: utf-8 -*-
from tkinter import *  # (sur python 3.1 le module s'appèle tkinter)
# import bm_u, bm_u_for_ftp




class MenuBar(Frame):
    # tres important : transmettre boss !!
    """Définition de toute la Barre des menus déroulant"""
    def __init__(self, boss=None):
        Frame.__init__(self, boss, borderwidth=2)  
        # Menu Fichier
        menuFichier = Menubutton(self, text='Fichier', underline=0)
        menuFichier.pack(side=LEFT)
        menu1=Menu(menuFichier)
        menu1.add_command(label='Quitter', underline=0, command=boss.quit)
        menuFichier.configure(menu=menu1)

        # Menu Divers et tests.
        test_menu_button = Menubutton(self, text='Tests',underline=0)
        test_menu_button.pack(side=LEFT, padx=5)
        self.test_menu = Menu(test_menu_button)
        self.test_menu.add_separator()
        self.test_menu.add_command(label='Version', underline=0,command=boss.afficherVersion)
        test_menu_button.configure(menu=self.test_menu)

        # Menu Outils :
        tool_menu_button = Menubutton(self, text='Outils', underline=0)
        tool_menu_button.pack(side=LEFT, padx=5)
        self.tool_menu = Menu(tool_menu_button)
        self.tool_menu.add_command(label='FTP_fi58_(amazilia)', underline=0)
        tool_menu_button.configure(menu=self.tool_menu)

