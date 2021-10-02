#! /usr/bin/python3.8
# -*- coding:utf-8 -*-
# Script pour gestion de tous les scripts automatisation_administration par fenêtrage.
# Auteur : Ricardo Linares Rubio
# Date : 28 Septembre 2021
# Version : 2.0

# Importation des modules
from tkinter import *
import os
import tkinter


# Création de sous_fenetre "à_propos"
def show_about():
    about_window = tkinter.Toplevel(master)
    about_window.title("A propos")
    lb = tkinter.Label(about_window, text="Ce script automatise l'administration de linux \n\nEtudiant : R. Linares Rubio \n\nP06AIC Openclassrooms ")
    lb.pack()

# Appel des Scripts 'automatisation
def users_list():
    os.system('python3 List_users.py')

def create_users():
    os.system('python3 Créer_users.py') 

def suppr_users():
    os.system('python3 Supprime_user.py') 

def sauv_linux():
    os.system('python3 Sauvegarde.py') 

def nmap_grep():
    os.system('python3 Réseau.py')         




# Creéation de la fen^etre et parametrage
master = Tk()
master.geometry("520x50")
master.title("Script Python Automatisation Linux")


#Widgets
mainmenu = tkinter.Menu(master)

# Menu 1 (Réseau)
Reseau = tkinter.Menu(mainmenu, tearoff=0)
Reseau.add_command(label="Decouverte reseau" ,command=nmap_grep)

# Menu 2 (Liste, Création, Suppresion)
Linux_users = tkinter.Menu(mainmenu, tearoff=0)
Linux_users.add_command(label="Liste utilisateur Linux", command=users_list)
Linux_users.add_command(label="Création utilisateur Linux" , command=create_users)
Linux_users.add_command(label="Suppression utilisateur Linux", command=suppr_users)

# Menu 3 (Sauvegarde)
Sauvegarde = tkinter.Menu(mainmenu, tearoff=0)
Sauvegarde.add_command(label="Sauvegarde Linux dossier home" , command=sauv_linux)

# Menu 4 (Quitter)
Quitter = tkinter.Menu(mainmenu, tearoff=0)
Quitter.add_command(label="Quitter", command=master.quit)

# Menu 5 (A_propos)
A_propos = tkinter.Menu(mainmenu, tearoff=0)
A_propos.add_command(label="A propos", command=show_about)

mainmenu.add_cascade(label="Réseau", menu=Reseau)
mainmenu.add_cascade(label="Linux_users", menu=Linux_users)
mainmenu.add_cascade(label="Sauvegarde", menu=Sauvegarde)
mainmenu.add_cascade(label="Quitter", menu=Quitter)
mainmenu.add_cascade(label="A propos", menu=A_propos)

# Boucle Principale
master.config(menu=mainmenu)
master.mainloop()