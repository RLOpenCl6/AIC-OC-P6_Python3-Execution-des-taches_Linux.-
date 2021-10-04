#! /usr/bin/python3.8
# -*- coding:utf-8 -*-
# Script permettant la création de nouveaux utilisateurs Linux
# Auteur : R. Linares Rubio
# Date : 28 Septembre 2021
# Version : 2.0


# import des modules
from pexpect import pxssh
import getpass
import os


# création de la variable user
user = input('user: ')
# connexion en ssh au client linux
try:
    s = pxssh.pxssh()
    hostname = input('hostname: ') # attribution variable hostname
    username = input('username: ') # attribution variable username
    password = getpass.getpass('password: ') # attribution variable password
    s.login(hostname, username, password)
    s.sendline('sudo su')   # passage en admin
    s.prompt()         # faire coincider le prompt
    print(s.before)    # print tout avant le prompt
    s.sendline('RLRRLR') # mdp admin
    s.prompt()
    print(s.before)
    s.sendline('useradd -m ' + str(user)) # ajout de l'utilisateur    
    s.prompt()
    print(s.before)
    s.sendline('passwd ' + str(user))     # Créer MDP nouveau utilisateur
    s.sendline('RLRRLR') # attribution du pwd
    s.prompt()
    print(s.before)
    s.sendline('RLRRLR') # confirmation du pwd
    s.prompt()
    print(s.before)
    s.sendline('passwd --unlock ' + str(user)) # activation de l'utilisateur
    s.prompt()
    print(s.before)
    #s.logout()

except pxssh.ExceptionPxssh as e:
    print("utilisateur créé.")
    print(e)