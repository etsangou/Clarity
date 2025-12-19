import random

possibilities = "TtNnEe@$"

# Chargement des mots de passe existants
with open("passwords.txt", "r") as file:
    existing_passwords = [line.strip() for line in file]

# Combien de mots de passe sont générer
num_passwords = 10000

# Génération de nouveaux mots de passe
new_passwords = []
while len(new_passwords) < num_passwords: # Générer le nombre de mots de passe demandé
    password = ""
    for i in range(8):
        password += random.choice(possibilities)
    if password not in existing_passwords: # Vérifier si le mot de passe est nouveau
        new_passwords.append(password)
        existing_passwords.append(password)

# Stockage des nouveaux mots de passe dans le fichier
with open("passwords.txt", "a") as file:
    for password in new_passwords:
        file.write(password + "\n")

print("Nouveaux mots de passe générés : ")
print(new_passwords)