def convert_hex_to_bin(htb):

    # Demande à l'utilisateur d'entrer un nombre en base hexadécimale
    hexadecimal = input("Entrez un nombre en base hexadécimale : ")

    # Crée un dictionnaire pour la conversion des chiffres hexadécimaux en binaire
    hex_to_binary = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
        }

    # Initialise une chaîne de caractères pour stocker le résultat binaire
    binary = ""

    # Convertit chaque chiffre hexadécimal en binaire et l'ajoute au résultat
    for digit in hexadecimal:
        binary += hex_to_binary.get(digit, "")

    # Affiche le résultat en base binaire
print("Le nombre en base binaire est :", binary)


