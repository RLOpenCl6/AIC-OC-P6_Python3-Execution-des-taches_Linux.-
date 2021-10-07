#! /usr/bin/python3.8
# -*- coding:utf-8 -*-
# Script permettant la sauvegarde du dossier Home Linux (format tar.gz)
# Auteur : R. Linares Rubio
# Date : 28 Septembre 2021
# Version : 2.0

import os
from datetime import date



try:
    name = str(input("Nom de la sauvegarde: "))
    userin = str(input("Chemin de dossier pour Sauvegarde : ")) 
    today = date.today()
    os.system('tar -czvf' + str(today) + '-' + name + '.tar.gz ' + userin)
    print("Sauvegarde éfectuée: " )

except EOFError as EOF :    
  print(EOF)







   


