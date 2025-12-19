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