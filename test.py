import os

def loadDataFiles(filename):
    password_list = []
    try:
        file_path = os.path.join("C://Users//enzot//Documents//Clarity//.Data", filename)
        with open(file_path, 'r') as file:
            lines = file.readlines()
            password_list = [line.strip() for line in lines]
    except FileNotFoundError:
        print(f"Le fichier {filename} n'existe pas.")
    return password_list

filename = "1_000_000words.data"
a = loadDataFiles(filename)
print(len(a))
