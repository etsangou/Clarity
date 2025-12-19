import sys

def color(color, text, style=None):
    # Définition des codes de couleurs
    colors = {
        1: "\033[91m",  # Rouge
        2: "\033[92m",  # Vert
        3: "\033[93m",  # Jaune
        4: "\033[94m",  # Bleu
        5: "\033[95m",  # Magenta
        6: "\033[96m"   # Cyan
    }

    styles = {
        "reset": "\033[0m",  # Réinitialisation de la couleur
        "underline": "\033[4m",  # Underline
        "inverse": "\033[7m"    # Inverse (swap background and foreground colors)
    }

    colored_text = ""

    if color in colors:
        colored_text += colors[color]

    if style in styles:
        colored_text += styles[style]

    colored_text += text + styles["reset"]
    return colored_text

def deleteLastLine():
    sys.stdout.write("\033[F\033[K")
    sys.stdout.flush()