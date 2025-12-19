# Librairies Python
import os
import time


# Mes librairies
from textManagement import color, deleteLastLine


# Librairies Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Mes variables 
msg = f"""
{color(2, "Utilisation : Clarity <commande> [options]")}

{color(3, "Liste des commandes disponibles :")}

{color(4, "Commande `exit` :")}
    La commande `exit` permet de quitter le programme Clarity.

{color(4, "Commande `url` :")}
    La commande `url` permet de préciser quel site web le code doit essayer de bruteforcer.

{color(4, "Commande `mydata <data_file>` :")}
    La commande `mydata` permet d'assimiler les données du fichier .data contenant des informations sur la cible, afin de créer un ensemble de possibilités qui sera utilisé par la suite dans l'un des deux modes d'attaque.

{color(4, "Commande `moreuse <100>, <1000>, <10000>, <100000>, <1000000>` :")}
    La fonction `moreuse` permet de tester les x mots de passe les plus utilisés.

{color(4, "Commande `mode <mouse>, <web>` :")}
    La fonction `mode` permet de choisir le type d'input à effectuer pour tester les mots de passe. Par défaut, le mode web est sélectionné.

{color(4, "Commandes `<clear>`, `<cls>` :")}
    Permet de vider le terminal.

{color(4, "Commande `textzonetype <ByID>, <ByName>, <ByPATH>, <ByCSS_Selector> <nametextzonetype>` :")}
    Permet de préciser, pour une attaque web, le type de zone de texte et le nom de cette zone.

{color(4, "Commande `stopzonetype <ByID>, <ByName>, <ByPATH>, <ByCSS_Selector> <nametextzonetype>` :")}
    Permet de préciser, pour une attaque web, le type de la zone d'arrêt et le nom de cette zone.

{color(4, "Commande `--help` :")}
    Permet d'afficher toutes les commandes et leurs fonctions.

{color(4, "Commande `bruteforce <Nombre_de_Caractère (1-8)> <caractère_spéciaux (on / off)>` :")}
    Permet d'utiliser un bruteforce classique pour attaquer via l'un des deux modes d'attaque.

{color(4, "Commande `dictionary <all>, <french>, <english>, <spanish>, <deutsch>, <danish>, <dutch>, <finnish>, <hungarian>, <italian>, <latin>, <norwegian>` :")}
    Permet d'utiliser un dictionnaire pour bruteforcer via le mode sélectionné. Vous pouvez spécifier la langue parmi les options disponibles.
"""


def Start(msg):
    os.system("cls")

    print("Clarity [version 1.0.0.8]")
    print("(c) Shitwait Entertainment. Tous droits réservés.")
    print("")

    loop(msg)

def loop(msg):
    while True:
        user_input = input("Clarity> ")
        parts = user_input.split()
        if len(parts) > 0:
            if user_input.lower() == 'exit':
                break

            elif parts[0].lower() == 'url':
                if len(parts) > 1:
                    couleur = 2 # Vert
                    texte = parts[1]
                    texte_colore = color(couleur, texte)
                    print(f"URL : {texte_colore}")
                else:
                    print("Commande 'url' nécessite un argument (l'URL).")

            elif parts[0].lower() == 'mydata':
                if len(parts) > 1:
                    fichier_data = parts[1]
                    # Vérifiez si le fichier .data existe
                    if os.path.isfile(fichier_data) and fichier_data.endswith('.data'):
                        couleur = 2  # Vert
                        texte_colore = color(couleur, fichier_data)
                        print(f"Localisation valide : {texte_colore}")
                        mydata = fichier_data
                        # - - - Met ton code ici - - -
                    else:
                        couleur = 1  # rouge
                        texte_colore = color(couleur, fichier_data)
                        print(f"Localisation non valide pour : {texte_colore}")
                else:
                    print("Commande 'mydata' nécessite un argument (la localisation des données).")

            elif parts[0].lower() == 'moreuse':
                if len(parts) > 1:
                    moreuse = parts[1]
                    if parts[1] == "100":
                        Test_100words()
                    elif moreuse == "1000":
                        Test_1000words()
                    elif moreuse == "10000":
                        Test_10000words()
                    elif moreuse == "100000":
                        Test_100000words()
                    elif moreuse == "1000000":
                        Test_1000000words()
                    else:
                        print("L'argument " + moreuse + " n'est pas valide")
                else:
                    print("Commande 'moreuse' nécessite un argument (100, 1000, 10000, 100000, 1000000).")

            elif parts[0].lower() == 'mode':
                a = 0
                if len(parts) > 1:
                    if parts[1] == "mouse":
                        couleur = 2 # Vert
                        texte = parts[1]
                        texte_colore = color(couleur, texte)
                        print(f"Mode {texte_colore} activé")
                        mouse = True
                        web = False
                    elif parts[1] == "web":
                        couleur = 2 # Vert
                        texte = parts[1]
                        texte_colore = color(couleur, texte)
                        print(f"Mode {texte_colore} activé")
                        mouse = False
                        web = True
                    else:
                        couleur = 1 # Rouge
                        texte = parts[1]
                        texte_colore = color(couleur, texte)
                        print(f"L'argument {texte_colore} n'est pas valide")
                        a = 1
                else:
                    if a == 0:
                        print("Commande 'mode' nécessite un argument (mouse ou web).")

            elif user_input.lower() == 'clear' or user_input.lower() == 'cls':
                os.system('cls')

            elif parts[0].lower() == 'textzonetype':
                if len(parts) > 1:
                    if len(parts) > 2:
                        if parts[1] == "ByID":
                            couleur = 2 # Vert
                            texte = parts[2]
                            texte_colore = color(couleur, texte)
                            print(f"La selection ByID est : {texte_colore}")
                            ByID = True
                            ByName = False
                            ByPATH = False
                            ByCSS_Selector = False

                        elif parts[1] == "ByName":
                            couleur = 2 # Vert
                            texte = parts[1]
                            texte_colore = color(couleur, texte)
                            print(f"La selection ByName est : {texte_colore}")
                            ByID = False
                            ByName = True
                            ByPATH = False
                            ByCSS_Selector = False

                        elif parts[1] == "ByPATH":
                            couleur = 2 # Vert
                            texte = parts[1]
                            texte_colore = color(couleur, texte)
                            print(f"La selection ByPATH est : {texte_colore}")
                            ByID = False
                            ByName = False
                            ByPATH = True
                            ByCSS_Selector = False

                        elif parts[1] == "ByCSS_Selector":
                            couleur = 2 # Vert
                            texte = parts[2]
                            texte_colore = color(couleur, texte)
                            print(f"La selection ByCSS_Selector est : {texte_colore}")
                            ByID = False
                            ByName = False
                            ByPATH = False
                            ByCSS_Selector = True

                        else :
                            couleur = 1 # Rouge
                            texte = parts[2]
                            texte_colore = color(couleur, texte)
                            print(f"L'argument {texte_colore} n'est pas valide")
                    else:
                        print("La commande 'textzonetype' nécessite un argument supplémentaire (le nom du type de la zone de texte).")
                else:
                    print("La commande 'textzonetype' nécessite un argument (le type de la zone de texte).")

            elif parts[0].lower() == 'stopzonetype':
                if len(parts) > 1:
                    if len(parts) > 2:
                        if parts[1] == "ByID":
                            couleur = 2 # Vert
                            texte = parts[2]
                            texte_colore = color(couleur, texte)
                            print(f"La selection ByID est : {texte_colore}")
                            stopByID = True
                            stopByName = False
                            stopByPATH = False
                            stopByCSS_Selector = False

                        elif parts[1] == "ByName":
                            couleur = 2 # Vert
                            texte = parts[1]
                            texte_colore = color(couleur, texte)
                            print(f"La selection ByName est : {texte_colore}")
                            stopByID = False
                            stopByName = True
                            stopByPATH = False
                            stopByCSS_Selector = False

                        elif parts[1] == "ByPATH":
                            couleur = 2 # Vert
                            texte = parts[1]
                            texte_colore = color(couleur, texte)
                            print(f"La selection ByPATH est : {texte_colore}")
                            stopByID = False
                            stopByName = False
                            stopByPATH = True
                            stopByCSS_Selector = False

                        elif parts[1] == "ByCSS_Selector":
                            couleur = 2 # Vert
                            texte = parts[2]
                            texte_colore = color(couleur, texte)
                            print(f"La selection ByCSS_Selector est : {texte_colore}")
                            stopByID = False
                            stopByName = False
                            stopByPATH = False
                            stopByCSS_Selector = True

                        else :
                            couleur = 1 # Rouge
                            texte = parts[2]
                            texte_colore = color(couleur, texte)
                            print(f"L'argument {texte_colore} n'est pas valide")
                    else:
                        print("La commande 'stopzonetype' nécessite un argument supplémentaire (le nom du type de la zone de texte).")
                else:
                    print("La commande 'stopzonetype' nécessite un argument (le type de la zone de texte).")

            elif parts[0].lower() == '--help':
                print(msg)

            elif parts[0].lower() == 'brutforce':
                print("Starting")

            elif parts[0].lower() == 'dictionary':
                a = 0
                if len(parts) > 1:
                    if parts[1] == "all":
                        couleur = 2 # Vert
                        texte = "all"
                        texte_colore = color(couleur, texte)
                        print(f"Le dictionaire {texte_colore} est selectioner")
                        Test_Dictionnaire(texte)

                    elif parts[1] == "french":
                        couleur = 2 # Vert
                        texte = "french"
                        texte_colore = color(couleur, texte)
                        print(f"Le dictionaire {texte_colore} est selectioner")
                        Test_Dictionnaire(texte)

                    elif parts[1] == "english":
                        couleur = 2 # Vert
                        texte = "french"
                        texte_colore = color(couleur, texte)
                        print(f"Le dictionaire {texte_colore} est selectioner")

                    elif parts[1] == "spanish":
                        couleur = 2 # Vert
                        texte = "french"
                        texte_colore = color(couleur, texte)
                        print(f"Le dictionaire {texte_colore} est selectioner")

                    elif parts[1] == "deutsch":
                        couleur = 2 # Vert
                        texte = "french"
                        texte_colore = color(couleur, texte)
                        print(f"Le dictionaire {texte_colore} est selectioner")

                    elif parts[1] == "danish":
                        couleur = 2 # Vert
                        texte = "french"
                        texte_colore = color(couleur, texte)
                        print(f"Le dictionaire {texte_colore} est selectioner")

                    elif parts[1] == "dutch":
                        couleur = 2 # Vert
                        texte = "french"
                        texte_colore = color(couleur, texte)
                        print(f"Le dictionaire {texte_colore} est selectioner")

                    elif parts[1] == "finnish":
                        couleur = 2 # Vert
                        texte = "french"
                        texte_colore = color(couleur, texte)
                        print(f"Le dictionaire {texte_colore} est selectioner")

                    elif parts[1] == "hungarian":
                        couleur = 2 # Vert
                        texte = "french"
                        texte_colore = color(couleur, texte)
                        print(f"Le dictionaire {texte_colore} est selectioner")

                    elif parts[1] == "italian":
                        couleur = 2 # Vert
                        texte = "french"
                        texte_colore = color(couleur, texte)
                        print(f"Le dictionaire {texte_colore} est selectioner")

                    elif parts[1] == "latin":
                        couleur = 2 # Vert
                        texte = "french"
                        texte_colore = color(couleur, texte)
                        print(f"Le dictionaire {texte_colore} est selectioner")

                    elif parts[1] == "norwegian":
                        couleur = 2 # Vert
                        texte = "french"
                        texte_colore = color(couleur, texte)
                        print(f"Le dictionaire {texte_colore} est selectioner")

                    else:
                        couleur = 1 # Rouge
                        texte = parts[1]
                        texte_colore = color(couleur, texte)
                        print(f"L'argument {texte_colore} n'est pas valide")
                        a = 1
                else:
                    if a == 0:
                        print("Commande 'dictionary' nécessite un argument (<language> ou all).")

            else:
                print("Erreur : commande inconnue '" + user_input + "'")
            print("")
        else:
            print("")

def test_passwords(password_list):
    a = 0
    nombre_de_mots_de_passe = len(password_list)
    driver = webdriver.Chrome()
    driver.get("http://82.65.183.109:888")
    wait = WebDriverWait(driver, 10)
    password_input = wait.until(EC.presence_of_element_located((By.ID, "passwordInput")))
    start_time = time.time()
    print("")

    try:
        for i, password in enumerate(password_list, 1):
            password_input.clear()
            password_input.send_keys(password)
            password_input.send_keys(Keys.RETURN)
            password_message = wait.until(EC.presence_of_element_located((By.ID, "passwordMessage")))
            if "Mot de passe correct" in password_message.text:
                print(f"Le mot de passe est : {password} ({i}/{nombre_de_mots_de_passe})")
                a = 1
                break 

            elapsed_time = time.time() - start_time
            avg_time_per_password = elapsed_time / i
            remaining_passwords = nombre_de_mots_de_passe - i
            estimated_remaining_time = avg_time_per_password * remaining_passwords

            deleteLastLine()
            print("Estimation du temps restant : " + format_time(estimated_remaining_time))

    except Exception as e:
        couleur = 1  # rouge
        texte = "Le test s'est subitement arrêté"
        texte_colore = color(couleur, texte)
        print(texte_colore)

    if a == 0:
        print("Le mot de passe n'a pas été trouvé")

    end_time = time.time()
    elapsed_time = end_time - start_time 
    print("Le test a pris environ {0:.3f} secondes".format(elapsed_time))
    driver.quit()

def loadDataFiles(filename):
    password_list = []
    try:
        file_path = os.path.join("E://Code//Application//Clarity//.Data", filename)
        with open(file_path, 'r') as file:
            lines = file.readlines()
            password_list = [line.strip() for line in lines]
    except FileNotFoundError:
        print(f"Le fichier {filename} n'existe pas.")
    return password_list

def loadDictionaryFiles(filename):
    password_list = []
    try:
        file_path = os.path.join("E://Code//Application//Clarity//.Language", filename)
        with open(file_path, 'r') as file:
            lines = file.readlines()
            password_list = [line.strip().lower() for line in lines]  # Convertir en minuscules
    except FileNotFoundError:
        print(f"Le fichier {filename} n'existe pas.")
    return password_list

def loadAllDictionaryFiles():
    directory_path = "E://Code//Application//Clarity//.Language"
    password_list = []
    try:
        # Obtenez la liste de fichiers dans le répertoire
        files = os.listdir(directory_path)

        for filename in files:
            file_path = os.path.join(directory_path, filename)
            if os.path.isfile(file_path):
                with open(file_path, 'r', encoding='iso-8859-1') as file:
                    lines = file.readlines()
                    password_list.extend([line.strip().lower() for line in lines])  # Convertir en minuscules
    except FileNotFoundError:
        print(f"Le répertoire {directory_path} n'existe pas.")
    
    return password_list

def Test_100words():
    filename = "100words.data"
    password_list = loadDataFiles(filename)
    test_passwords(password_list)

def Test_1000words():
    filename = "1_000words.data"
    password_list = loadDataFiles(filename)
    test_passwords(password_list)

def Test_10000words():
    filename = "10_000words.data"
    password_list = loadDataFiles(filename)
    test_passwords(password_list)

def Test_100000words():
    filename = "100_000words.data"
    password_list = loadDataFiles(filename)
    test_passwords(password_list)

def Test_1000000words():
    filename = "1_000_000words.data"
    password_list = loadDataFiles(filename)
    test_passwords(password_list)

def Test_MyData(list):
    password_list = loadDataFiles(list)
    test_passwords(password_list)

def format_time(seconds):
    days, seconds = divmod(seconds, 24*60*60)
    hours, seconds = divmod(seconds, 60*60)
    minutes, seconds = divmod(seconds, 60)
    time_parts = []

    if days > 0:
        time_parts.append(f"{int(days)} j")
    if hours > 0:
        time_parts.append(f"{int(hours)} h")
    if minutes > 0:
        time_parts.append(f"{int(minutes)} min")
    if seconds > 0 or not time_parts:
        time_parts.append(f"{int(seconds)} s")

    return ' '.join(time_parts)

def Test_Dictionnaire(language):
    if language == "all":
        test_passwords(loadAllDictionaryFiles())
    else:
        filename = language + ".txt"
        password_list = loadDictionaryFiles(filename)
        test_passwords(password_list)

Start(msg)