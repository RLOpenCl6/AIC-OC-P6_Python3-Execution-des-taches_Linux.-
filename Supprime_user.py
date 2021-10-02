#! /usr/bin/python3.8
# -*- coding:utf-8 -*-
# Script permettant la supression utilisateur Linux
# Auteur : R. Linares Rubio
# Date : 28 Septembre 2021
# Version : 2.0


# import des modules
from pexpect import pxssh
import getpass

# création de la variable user
user = input('user: ')

# connexion en ssh au client linux
try:
    s = pxssh.pxssh()
    hostname = input('hostname: ') # attribution variable hostname
    username = input('username: ') # attribution variable username
    password = getpass.getpass('password: ') # attribution variable password
    s.login(hostname, username, password)
    s.sendline('su')   # passage en admin
    s.sendline('RLRRLR') # mdp admin
    s.sendline('userdel -f -r ' + str(user)) # suppression de l'utilisateur et de ses dossiers
    s.logout()
except pxssh.ExceptionPxssh as e:
    print("utilisateur supprimé.")
    print(e)