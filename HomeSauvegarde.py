# Importer les modules suivants
import shutil
from datetime import date
import os
import sys

 
# Si besoin, changer le dossier
os.chdir(sys.path[0])


# Fonction pour réaliser la sauvegarde des fichiers et dossiers
def take_backup(src_file_name,
				dst_file_name=None,
				src_dir='',
				dst_dir=''):
	try:

		# Obtention de la date d'aujourd'hui
		# Extract the today's date
		today = date.today()
		date_format = today.strftime("%d_%b_%Y_")

		
		
		# Déclarer le directory source à l'endroit de sauvegarde
		src_dir = src_dir+src_file_name

		
		# Si l'utilisteur ne declare la source alors: message d'erreur...
		if not src_file_name:
			print("Please give atleast the Source File Name")
			exit()

		try:
			
			
			# Si l'utilisateur fournit tous les inputs
			if src_file_name and dst_file_name and src_dir and dst_dir:
				src_dir = src_dir+src_file_name
				dst_dir = dst_dir+dst_file_name
				
			# Quand l'utilisateur fournit soit 
			# 'None' ou String ('') vide
			elif dst_file_name is None or not dst_file_name:
				dst_file_name = src_file_name
				dst_dir = dst_dir+date_format+dst_file_name
				
			# Quand l'utilisateur fournit un string vide avec un ou plus d'éspaces ('  ')			
			elif dst_file_name.isspace():
				dst_file_name = src_file_name
				dst_dir = dst_dir+date_format+dst_file_name
				
			#Quand l'utilisateur fournit un
			#nom pour le fichier de sauvegarde
			else:
				dst_dir = dst_dir+date_format+dst_file_name			
			
			# Maintenant, copier le fichiers de la sourde
			# à la destination
			shutil.copy2(src_dir, dst_dir)

			print("Backup Successful!")
		except FileNotFoundError:
			print("File does not exists!,\
			please give the complete path")
	
	
	# Quand on a besoin de sauvegarder dossiers seulement...
	except PermissionError:
		dst_dir = dst_dir+date_format+dst_file_name	
		
		
		# Copier le dossier complet de la source 
		# à la detination
		shutil.copytree(src_file_name, dst_dir)

# Appel de la fonction
take_backup("HomeSauvegarde.py")
