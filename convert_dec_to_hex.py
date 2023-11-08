def convert_dec_to_hex():
    while True:
        decimal_input_str = input("Entrez un nombre en base 10 que vous voulez convertir en base 16: ")

        if not decimal_input_str:
            print("Veuillez entrer une valeur.")
            continue  # Revenir au début de la boucle

        try:
            decimal_input = int(decimal_input_str)
        except ValueError:
            print("Erreur: Pensez à rentrer un nombre en base 10 que vous souhaitez convertir en base 16.")
        else:
            if decimal_input == 0:
                print("Le nombre '0' en base 10 correspond à 0 en base 16.")
            else:
                hexadecimal_chars = "0123456789ABCDEF"
                hexadecimal = ""

                while decimal_input > 0:
                    remainder = decimal_input % 16  # Calculate the remainder of the division by 16
                    hexadecimal = hexadecimal_chars[remainder] + hexadecimal  # Add the character corresponding to the remainder
                    decimal_input = decimal_input // 16  # Integer division by 16

                print(f"Le nombre {decimal_input_str} en base 10(decimal) correspond à {hexadecimal} en base 16(hexadecimal)")
            break  # Sortir de la boucle après une conversion réussie

convert_dec_to_hex()