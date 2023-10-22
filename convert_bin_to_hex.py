def binary_to_hexadecimal(binary_number):
    # Dictionnaire pour la conversion binaire-hexadécimale
    hex_dict = {
        '0000': '0', '0001': '1', '0010': '2', '0011': '3',
        '0100': '4', '0101': '5', '0110': '6', '0111': '7',
        '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
        '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
    }

    # Assurez-vous que la longueur de la chaîne binaire est un multiple de 4
    while len(binary_number) % 4 != 0:
        binary_number = '0' + binary_number

    # Initialise la chaîne hexadécimale résultante
    hexadecimal_result = ""

    # Parcours la chaîne binaire par groupes de 4 bits
    for i in range(0, len(binary_number), 4):
        group = binary_number[i:i+4]
        hexadecimal_result += hex_dict[group]

    return hexadecimal_result

# Demander à l'utilisateur d'entrer un nombre binaire
binary_input = input("Entrez un nombre binaire : ")

# Appeler la fonction de conversion et afficher le résultat
hexadecimal_result = binary_to_hexadecimal(binary_input)
print(f"Le nombre hexadécimal correspondant est : {hexadecimal_result}")
