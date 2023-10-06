def convert_dec_to_hex(dth):
    if dth == 0:
        return "0"  # Gestion du cas où le nombre décimal est 0

    hexadecimal_chars = "0123456789ABCDEF"
    hexadecimal = ""

    while dth > 0:
        remainder = dth % 16  # Calcul du reste de la division par 16
        hexadecimal = hexadecimal_chars[remainder] + hexadecimal  # Ajout du caractère correspondant au reste
        dth = dth // 16  # Division entière par 16

    return hexadecimal

# Demander à l'utilisateur d'entrer un nombre décimal
decimal_input = int(input("Entrez un nombre décimal que vous voulez convertir en base hexadecimal: "))

while decimal_input==type(str):
    print("Veuillez entrez un nombre décimal")

    
# Appeler la fonction de conversion et afficher le résultat
hexadecimal_result = convert_dec_to_hex(decimal_input)
print(f"Le nombre hexadécimal correspondant est : " +str(hexadecimal_result))