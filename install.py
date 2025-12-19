import os
import subprocess

# Obtenir le répertoire du script Python
script_directory = os.path.dirname(os.path.abspath(__file__))

# Chemin à ajouter au PATH
nouveau_chemin = script_directory

# Exécuter la commande setx PATH
commande_path = f'setx PATH "%PATH%;{nouveau_chemin}"'
subprocess.run(commande_path, shell=True)

print(f'Le chemin {nouveau_chemin} a été ajouté au PATH avec succès.')

# Exécuter la commande pour installer le module Selenium
commande_pip = 'pip install selenium'
subprocess.run(commande_pip, shell=True)

print('Le module Selenium a été installé avec succès.')