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

# Initialisation de la variable decimal_input_str
decimal_input_str = ""

# Tant que l'entrée n'est pas un nombre décimal valide, continuez à demander à l'utilisateur
while True:
    decimal_input_str = input("Entrez un nombre décimal que vous voulez convertir en base hexadecimal: ")
    
    # Vérifier si l'entrée est une chaîne de caractères (str)
    if isinstance(decimal_input_str, int):
        print("Veuillez entrer un nombre décimal valide.")
    else:
        try:
            decimal_input = int(decimal_input_str)
            break  # Sortir de la boucle si l'entrée est valide
        except ValueError:
            print("Entrée non valide. Assurez-vous d'entrer un nombre décimal valide.")

# À ce stade, decimal_input contient un nombre décimal valide
# Appeler la fonction de conversion et afficher le résultat
hexadecimal_result = convert_dec_to_hex(decimal_input)
print(f"Le nombre hexadécimal correspondant est : {hexadecimal_result}")

    
# Appeler la fonction de conversion et afficher le résultat
hexadecimal_result = convert_dec_to_hex(decimal_input)
print(f"Le nombre hexadécimal correspondant est : " +str(hexadecimal_result))





 