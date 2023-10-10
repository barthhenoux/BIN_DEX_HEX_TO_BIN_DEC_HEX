def hex_to_bin(hexadecimal):
    # Dictionnaire pour la correspondance hexadécimal -> binaire
    hex_to_bin_dict = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }

    # Convertir le nombre hexadécimal en binaire
    binary = ''.join(hex_to_bin_dict[char] for char in hexadecimal.upper())
    
    return binary

# Exemple d'utilisation
hexadecimal_input = input("Entrez un nombre hexadécimal : ")
binary_output = hex_to_bin(hexadecimal_input)
print(f"Le nombre binaire correspondant est : {binary_output}")

