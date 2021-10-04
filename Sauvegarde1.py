#! /usr/bin/python3.8
# -*- coding:utf-8 -*-
# Script permettant le lancement du script de sauvegarde Linux
# Auteur : R. Linares Rubio
# Date : 28 Septembre 2021
# # Version : 2.0


# import du module
import os

os.system("ssh adminsys@192.168.0.30 'python3 -s' <./Sauvegarde.py")   # lancez une commande")