# Demander à l'utilisateur d'entrer un nombre binaire
binary_input = input("Entrez un nombre binaire que vous voulez convertir en base hexadécimale: ")

# Vérifier si le nombre est négatif (s'il commence par un signe moins '-')
is_negative = False
if binary_input.startswith('-'):
    is_negative = True
    binary_input = binary_input[1:]  # Supprimer le signe moins

# Vérifier si l'entrée est vide ou ne contient que des zéros
if not binary_input or all(bit == '0' for bit in binary_input):
    hex_result = "0"
else:
    # Ajouter des zéros à gauche pour que la longueur soit un multiple de 4
    while len(binary_input) % 4 != 0:
        binary_input = '0' + binary_input

    # Définir un dictionnaire pour la correspondance entre les groupes de 4 bits et les chiffres hexadécimaux
    hex_mapping = {
        '0000': '0',
        '0001': '1',
        '0010': '2',
        '0011': '3',
        '0100': '4',
        '0101': '5',
        '0110': '6',
        '0111': '7',
        '1000': '8',
        '1001': '9',
        '1010': 'A',
        '1011': 'B',
        '1100': 'C',
        '1101': 'D',
        '1110': 'E',
        '1111': 'F'
    }

    # Diviser l'entrée en groupes de 4 bits et convertir en hexadécimal
    hex_result = ''
    for i in range(0, len(binary_input), 4):
        hex_group = binary_input[i:i + 4]
        hex_digit = hex_mapping[hex_group]
        hex_result += hex_digit

# Ajouter un signe moins si nécessaire
if is_negative:
    hex_result = "-" + hex_result

# Afficher le résultat
print(f"Le nombre hexadécimal correspondant est : {hex_result}")
