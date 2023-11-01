def convert_dec_to_hex(dth):
    if dth == 0:
        return "0"  # Handling the case where the decimal number is 0

    hexadecimal_chars = "0123456789ABCDEF"
    hexadecimal = ""

    while dth > 0:
        remainder = dth % 16  # Calculate the remainder of the division by 16
        hexadecimal = hexadecimal_chars[remainder] + hexadecimal  # Add the character corresponding to the remainder
        dth = dth // 16  # Integer division by 16

    return hexadecimal

# Demander à l'utilisateur d'entrer un nombre décimal 
decimal_input_str = input("Enter a decimal number you want to convert to hexadecimal: ")

# Tant que l'entrée n'est pas un nombre décimal valide, continuez à demander à l'utilisateur
while True:
    if not decimal_input_str:
        print("Veuillez entrer une valeur.")
        decimal_input_str = input("Enter a decimal number you want to convert to hexadecimal: ")
        continue  # Revenir au début de la boucle sans essayer de convertir

    try:
        decimal_input = int(decimal_input_str)
    except ValueError:
        print("Invalid input. Please make sure to enter a valid decimal number.")
        decimal_input_str = ""  # Réinitialiser l'entrée
    else:
        hexadecimal_result = convert_dec_to_hex(decimal_input)
        print(f"The corresponding hexadecimal number is: {hexadecimal_result}")
        break

 