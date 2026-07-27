# Clarity

>Clarity est un outil de test de pénétration qui offre un ensemble de commandes permettant de cibler des sites web spécifiques et d'effectuer des attaques de force brute ou de dictionnaire sur les mots de passe, en utilisant diverses options de personnalisation.

## Description

Clarity est un p

## Prérequis

Avant d'utiliser le programme Clarity, assurez-vous d'avoir les éléments suivants installés sur votre système :

- **Python 3.7 ou supérieur :** Si Python n'est pas déjà installé, vous pouvez le faire en utilisant les commandes suivantes :

    ```bash
    $ sudo apt update
    $ sudo apt upgrade
    $ sudo apt install python3
    ```

- **Bibliothèque Selenium :** Vous pouvez installer la bibliothèque Selenium via pip (le gestionnaire de paquets Python) avec la commande suivante :

    ```bash
    $ pip install selenium
    ```

- **Chromedriver :** Vous aurez besoin de Chromedriver et donc de Google Chrome pour automatiser Chrome avec Selenium. Vous pouvez l'installer en téléchargeant la version compatible avec votre version de Chrome à partir du site officiel de Chromedriver (https://sites.google.com/a/chromium.org/chromedriver/downloads). Une fois téléchargé, placez-le dans un répertoire inclus dans votre variable d'environnement `PATH` pour qu'il soit accessible.

- **Une interface graphique :** Clarity nécessite une interface graphique, donc assurez-vous d'utiliser un environnement de bureau tel que Ubuntu 20.04.

Ces prérequis sont essentiels pour faire fonctionner Clarity correctement. Assurez-vous de les installer avant de lancer le programme.

## Installation

Pour installer le programme Clarity, suivez ces étapes :

1. Ouvrez un terminal.

2. Déplacez-vous dans le répertoire où vous souhaitez cloner le projet, par exemple :

    ```bash
    $ cd /Clarity
    ```

3. Clonez le dépôt GitHub en utilisant la commande suivante :

    ```bash
    $ git clone https://github.com/GladioGX/Clarity.git
    ```

4. Accédez au répertoire du projet Clarity :

    ```bash
    $ cd Clarity
    ```

5. Exécutez le script d'installation en utilisant Python :

    ```bash
    $ python install.py
    ```

Cela installera les dépendances nécessaires et configurera le projet Clarity sur votre système.

Assurez-vous d'avoir respecté les prérequis mentionnés précédemment avant de lancer le script d'installation.

## Liste des commandes

### Commande `exit`

La commande `exit` permet de quitter le programme Clarity.

### Commande `url <link>`

La commande `url` permet de préciser quel site web le code doit essayer de bruteforcer.

### Commande `mydata <data_file>`

La commande `mydata` permet d'assimiler les données du fichier `.data` contenant des informations sur la cible, afin de créer un ensemble de possibilités qui sera utilisé par la suite dans l'un des deux modes d'attaque.

### Commande `moreuse <100>, <1000>, <10000>, <100000>, <1000000>`

La fonction `moreuse` permet de tester les x mots de passe les plus utilisés.

### Commande `mode <mouse>, <web>`

La fonction `mode` permet de choisir le type d'input à effectuer pour tester les mots de passe. Par défaut, le mode web est sélectionné.

### Commandes `<clear>`, `<cls>`

Permet de vider le terminal.

### Commande `textzonetype <ByID>, <ByName>, <ByPATH>, <ByCSS_Selector> <nametextzonetype>`

Permet de préciser, pour une attaque web, le type de zone de texte et le nom de cette zone.

### Commande `stopzonetype <ByID>, <ByName>, <ByPATH>, <ByCSS_Selector> <nametextzonetype>`

Permet de préciser, pour une attaque web, le type de la zone d'arrêt et le nom de cette zone.

### Commande `--help`

Permet d'afficher toutes les commandes et leurs fonctions.

### Commande `bruteforce <Nombre_de_Caractère (1-8)> <caractère_spéciaux (on / off)>`

Permet d'utiliser un bruteforce classique pour attaquer via l'un des deux modes d'attaque.

### Commande `dictionary <all>, <language>`

Permet d'utiliser un dictionnaire pour bruteforcer via le mode sélectionné. Actuellement, les langues disponibles sont : 

- Française
- Anglaise
- Espagnole
- Allemande
- Danoise
- Néerlandaise
- Finlandaise
- Hongroise
- Italienne
- Latine
- Norvégienne

Ces langues sont toutes utilisées par la fonction "all".

## Contributeurs

Voici la liste des contributeurs actuels de ce projet :

- [GladioGX](https://github.com/GladioGX)
- [MoonlightShitwait](https://github.com/MoonlightShitwait)

Nous accueillons avec gratitude toutes les contributions et les efforts déployés par ces contributeurs pour améliorer ce projet.

## License

Ce projet est publié sous la [Licence MIT](LICENSE.md).

La Licence MIT est une licence open source qui permet aux utilisateurs de librement utiliser, modifier et distribuer ce logiciel. Vous pouvez consulter les détails de la licence dans le fichier [LICENSE.md](LICENSE.md) associé à ce projet.



Clarity est un programme de forçage de mot de passe de la marque Shitwait, non destiné à la vente, mais seulement à l’entraînement.

  

Celui-ci est utilisable sur n’importe quel terminal classique Clarity possédant un terminal intégré avec ses propres fonctions.

  

En effet, Clarity possède de nombreuse fonctions allant du brutforce classique au brutforce orienté (en utilisant des informations sur la victime), c’est la multiplicité des fonctions et l’efficacité de ses dernières qui fait la force et l’essence du projet Clarity. Le programme possède en tout 5 fonctions d’attaques, y fonctions de paramètrage et z fonctions d’aide à l’utilisateur. Avant d’utiliser les fonctions, l’utilisateur devra rentrer des informations tel que le type de mot de passe ou la taille de ce dernier par exemple.

  

Les fonctions d’attaque sont les suivantes :

  

- Brutforce classique avec la fonction `brutforce` sans arguments : essai toutes les combinaisons possible de tous les caractères jusqu’à craquage du mot de passe.

- Brutforce dictionnaire avec la fonction `brutforce : dico` Prend en argument le mot clé dico et affiche les différents dictionnaire disponible dans le programme.

- `brutforce : dico(langue1,langue2,…)` essayera tous les mots des dictionnaires « langue1 » , « langue2 » , « … » rentrés en paramètre d’arguments par l’utilisateur.

- `brutforce : dico(global)` essayera tous les mots de tous les dictionnaires disponibles sur le programme Clarity.

- Brutforce dataliste avec la fonction `brutforce : datalist` prend en argument le mot clé datalist et affiche les différentes listes de donnés disponibles.

- `brutforce : datalist(mostused list)` prend en paramètre d’argument le mot clé mostused suivis d

- Brutforce orienté avec la fonction `brutforce : targeted, mydata` prend en argument le mot clé targeted et le fichier mydata contenant les informations entrée au préalable par l’utilisateur : essai chacune des informations donnés sur l’utilisateur en les modifiant et en les corrélant jusqu’à trouver le mot de passe de la victime.

  

L’utilisateur pourra paramétrer ses fonctions à l’aide des fonctions de paramétrage suivante :

  

- Parametrage du fichier mydata avec la fonction `settings : mydata` qui prend en argument le mot clé mydata : ouvre le fichier mydata en mode édition pour que l’utilisateur puisse ajouter / modifier des informations.

- Parametrage des informations préalable avec la fonctions `settings : data` qui prend en argument le mot clé data : ouvre le menu d’édition d’informations préalable pour que l’utilisateur puisse ajouter / modifier des informations.

  

Enfin, voici les différentes fonctions d’information mises à disposition de l’utilisateur :

  

- Informations sur les fonctions disponibles avec la fonction `help : fonctions` qui prend en argument le mot clé fonctions. Envoie l’utilisateur dans un menu contenant chacune des fonctions disponibles sur le programme Clarity. Ce dernier aura la possibilité d’obtenir d’avantage d’informations sur celle-ci ainsi que sur leur fonctionnement. La fonction appelé sans argument renverra la liste des fonctions disponible sur le programme.

- Informations sur Clarity avec la fonction `help : Clarity`. Envoie l’utilisateur dans un menu détaillant le fonctionnement logique du programme.

- Informations sur

  

Structure de Clarity 🙈:

  

Clarity

├─Main

├─Algorithme

└─Fonction

  

Clarity :

  

- Fonction Start

- Fonction Loop

  

Algorithme :

  

- Algorithme du brute force

- Algorithme de mydata

- Algorithme du dictionnaire

  

Fonction :

  

- _test_passwords :_ Permet d’accéder au site web et à tester tous les mots de passe qui lui sont donnés.

- _loadDictionaryFiles :_ Permet de mettre tous les mots d’un fichier dans une liste avec le path de ce fichier.

- _loadAllDictionaryFiles :_ Permet de mettre tous les mots de chaque dictionaire dans une liste via _loadDataFiles_.

- _Test_MoreUsedWord :_ Nouvelle version de la fonction _Moreuse,_ permet maintenant de choisir n’import quel entier compris entre 1 et 1.000.000 des fichiers _moreUseWord_ pour les mettre dans une liste via _loadDataFiles_ et les tester via _test_passwords._

- _Test_MyData :_ Fonction NON Faite.

- _loadDataFiles :_ Permet de mettre des mots de fichiers dans une liste.

- _format_time :_ Permet de transformer des secondes en Min/Heure/Jours.

- _Test_Dictionnaire :_ Fonction pour simplifier l’utilisation des fonctions _loadDictionaryFiles_ et _loadAllDictionaryFiles._

  

Features à implémenter :

  

Fonction d’attaque

  

- Commande moreuse `<nombre_de_mots_tester> [--help] ou [<web> <url> <textzonetype> <nametextzonetype> <stopzonetype> <namestopzonetype>] ou [<mouse> <with_délai> <délai>]`

- Commande mydata `<data_file> [--help] ou [<web> <url> <textzonetype> <nametextzonetype> <stopzonetype> <namestopzonetype>] ou [<mouse> <with_délai> <délai>]`

- Commande bruteforce `<Nombre_de_Caractère (1-8)> <Enable_caractère_spéciaux> [--help] ou [<web> <url> <textzonetype> <nametextzonetype> <stopzonetype> <namestopzonetype>] ou [<mouse> <with_délai> <délai>]`

- Commande dictionary `<all>, <language> [--help] ou [<web> <url> <textzonetype> <nametextzonetype> <stopzonetype> <namestopzonetype>] ou [<mouse> <with_délai> <délai>]`

  

Fonction de gestion :

  

- Commande snap mydata <data_file> [--help] ou `[<web> <url> <textzonetype> <nametextzonetype> <stopzonetype> <namestopzonetype>] ou [<mouse> <with_délai> <délai>]`

- Commande clear/cls

- Commande exit

  

Option :

  

Pour `<textzonetype>` ou `<stopzonetype>` les options sont les suivantes:

  

- i (pour utiliser ByID)

- n (pour utiliser ByName)

- p (pour utiliser ByPATH)

- css (pour utiliser ByCSS_Selector)

  

Exemple de fonction :

  

moreuse 1830193 `[](http://82.65.183.109:888/)[http://82.65.183.109:888](http://82.65.183.109:888) -i passwordInput -i passwordMessage`

  

To do list Enzo :

  

- Refaire les fonctions avec les nouvelles options (et supprimer celles qui ne sont plus utile) ;

- Faire en sort de ne pas utiliser le chemin complet pour chercher le dossier .Data et .Language, mais chercher le dossier enfant ;

- Mettre a jour la fonction test_passwords() pour utiliser les variables ;

- Recoder la fonction moreuse pour toujours utiliser le fichier 1 000 000, mais ne prendre que les x premier MDP ;

- Finir le code dictionary (variable texte = "language" à modifier)

- Coder la fonction brutforce

- Coder la fonction mouse dans test_passwords()


Nouvelles fonctions : 

Fonction d'attaque:

Commande moreuse <nombre_de_mots_tester> [--help] ou [<web> <url> <textzonetype> <nametextzonetype> <stopzonetype> <namestopzonetype>] ou [<mouse> <with_délai> <délai>]

Commande mydata <data_file> [--help] ou [<web> <url> <textzonetype> <nametextzonetype> <stopzonetype> <namestopzonetype>] ou [<mouse> <with_délai> <délai>]

Commande bruteforce <Nombre_de_Caractère (1-8)> <Enable_caractère_spéciaux> [--help] ou [<web> <url> <textzonetype> <nametextzonetype> <stopzonetype> <namestopzonetype>] ou [<mouse> <with_délai> <délai>]

Commande dictionary <all>, <language> [--help] ou [<web> <url> <textzonetype> <nametextzonetype> <stopzonetype> <namestopzonetype>] ou [<mouse> <with_délai> <délai>]



Fonction de gestion :

Commande snap mydata <data_file> [--help] ou [<web> <url> <textzonetype> <nametextzonetype> <stopzonetype> <namestopzonetype>] ou [<mouse> <with_délai> <délai>]

Commande clear/cls
Commande exit


Option :

Pour <textzonetype> ou <stopzonetype> les options sont les suivantes:
-i (pour utiliser ByID)
-n (pour utiliser ByName)
-p (pour utiliser ByPATH)
-css (pour utiliser ByCSS_Selector)

Exemple de fonction :
moreuse 1830193 http://82.65.183.109:888 -i passwordInput -i passwordMessage 



----------------------------------------------------------------------------------------------------------------------------------------------------------------------

To do list Enzo :

Refaire les fonctions avec les nouvelles options (et supprimer celles qui ne sont plus utile) ;
faire en sort de ne pas utiliser le chemin complet pour chercher le dossier .Data et .Language, mais chercher le dossier enfant ;
Mettre a jour la fonction test_passwords() pour utiliser les variables ;
Recoder la fonction moreuse pour toujours utiliser le fichier 1 000 000, mais ne prendre que les x premier MDP ;
Finir le code dictionary (variable texte = "language" à modifier)
Coder la fonction brutforce
Coder la fonction mouse dans test_passwords()

Structuration du Dossier Clarity

Clarity
└── .Data
    └── 1_000_000words.data
    └── 100_000words.data
    └── 10_000words.data
    └── 1_000words.data
    └── 100words.data
├── chromedriver.exe (indispensable pour l’utilisation de Selenium)
├── Clarity.py (Contient toutes les fonctions de Clarity)
├── textManagement.py (Pour les couleurs)
├── main.py
└── logo.ico



Structuration de code Clarity.py


#Partie 1 :
#Test des 1000 mots de passe les plus utilisés

#Partie 2 :
#Calcule de toutes les possibilités de mots de passes via ces données (avec 2 données) : print('Calcule de mots de passe (xxx/xxxxx)')

#Partie 3 :
#Test des 1 000 000 mots de passe les plus utilisés

#Partie 4 :
#Calcule de toutes les possibilités de mots de passes via un dictionnaire (langue individue) : print('Calcule de mots de passe (xxx/xxxxx) temps restant :  jours HH:MM:SS')

#Partie 5 :
#Calcule de toutes les possibilités de mots de passes via tous les dictionnaires Toutes les langues : print('Calcule de mots de passe (xxx/xxxxx) temps restant :  jours HH:MM:SS')

#Partie 6 :
#Test de mot de passe Random (Brut Force par défaut)

Pour Clarity V1 nous utiliserons python.
Pour Clarity V2 nous utiliserons C++/C#.

