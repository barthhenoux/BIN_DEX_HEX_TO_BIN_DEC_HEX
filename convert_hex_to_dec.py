def hex_to_dec(hexadecimal_input):
    # Initialiser la valeur décimale
    decimal_result = 0

    # Définir les caractères valides en hexadécimal
    hexadecimal_chars = "0123456789ABCDEFabcdef"

    # Parcourir chaque caractère hexadécimal de droite à gauche
    for char in hexadecimal_input[::-1]:
        # Assurer que le caractère est valide
        if char not in hexadecimal_chars:
            print("Caractère hexadécimal invalide")
            break
        # Convertir le caractère en décimal
        if '0' <= char <= '9':
            decimal_value = ord(char) - ord('0')
        elif 'A' <= char <= 'F':
            decimal_value = ord(char) - ord('A') + 10
        elif 'a' <= char <= 'f':
            decimal_value = ord(char) - ord('a') + 10
        # Ajouter la valeur décimale au résultat
        decimal_result += decimal_value

    # Retourner le résultat
    return decimal_result

# Demander à l'utilisateur d'entrer un nombre hexadécimal
hexadecimal_input = input("Entrez un nombre hexadécimal que vous voulez convertir en base décimale: ")

# Appeler la fonction hex_to_dec pour effectuer la conversion
decimal_result = hex_to_dec(hexadecimal_input)

# Afficher le résultat
print(f"Le nombre décimal correspondant est : {decimal_result}")