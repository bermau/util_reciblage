#!/bin/env/python3
"""Récupère la note de Pylint et la met dans un enregistrement

ce_programme module_ou_fichier
le rapport sera ajouté dans module_ou_fichier.txt avec une date"""

import sys
import re
import datetime
import os
import doctest

TEMPO = "TEMPO_pylint"
GLOBAL_OUTPUT_FILE = "quality_report.qc"
def get_default_report_name(file):
    """Retourne le nom du fichier de rapport par défaut
    >>> get_default_report_name(file="my_file.py")
    'my_file.qc'
    >>> get_default_report_name(file="my_file")
    'my_file.qc'
    >>> get_default_report_name(file="my_file.txt")
    'my_file.qc'
    """
    # Dans un regex python il faut escaper les points et les antislash,
    # pas les partenthèse. On récupère avec \1, dont le \ doit être protégé.
    return re.sub(r"(.*)\..*$", "\\1", file) + ".qc"

def exec_pylint(file):
    """si j'étais plus fort en python j'utiliserais

def report_evaluation(self, sect, stats, previous_stats):
située dans la classe PyLinter du fichier lint.py
"""
    os.system("pylint {} > {}".format(file, TEMPO))

def get_final_mark(ligne):
    """"Retourne la note à l'intérieur de la ligne
    >>> get_final_mark("Your code has been rated at 9.67/10 (previous run: \
    9.67/10, +0.00)")
    '9.67/10'
    >>> get_final_mark("Your code has been rated at 9.67/10 ")
    '9.67/10'
    >>> get_final_mark("Your code has been rated at 9.67/10")
    '9.67/10'
    >>> get_final_mark('Your code has been rated at -35.43/10 (previous run: -35.43/10, +0.00)')
    '-35.43/10'
    """
    # si on utilise r'', inutile de protéger \1
    return re.sub(r".*Your code has been rated at ([-0-9\./]*)($|.*$)", r"\1",
                  ligne)
def get_note():
    """Récupère la note en fin du fichier.
suite de l'horreur précédente
"""
    with open(TEMPO, mode='r') as note_file:
        leslignes = note_file.readlines()
        line = (leslignes[-2])
        note = get_final_mark(line)
        print("line", (line, ))
        note = note.replace("\n","")
        print((note,))
        print("Fin de get_note : {}".format(note))
    return note

if __name__ == '__main__':

    doctest.testmod()
    try:
        INPUT_FILE = sys.argv[1]
    except:
        INPUT_FILE = "reciblage_etude"
    print("fichier d'entrée : {}".format(INPUT_FILE))
    OUTPUT_FILE = get_default_report_name(INPUT_FILE)
    print("Fichier de sortie : {}".format(OUTPUT_FILE))
    exec_pylint(INPUT_FILE)
    note = get_note()
    CUR_DATE = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(OUTPUT_FILE, mode='a', encoding='utf8') as fichier:
        fichier.write(':'.join([CUR_DATE, INPUT_FILE, note]))
    with open(GLOBAL_OUTPUT_FILE, mode='a', encoding='utf8') as fichier:
        fichier.write(':'.join([CUR_DATE, INPUT_FILE, note]))
    print("La note est de : {} *".format(note))
