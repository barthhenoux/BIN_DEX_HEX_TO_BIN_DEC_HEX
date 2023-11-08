def convert_hex_to_bin():
    while True:
        # Demander à l'utilisateur d'entrer un nombre hexadécimal
        hexadecimal_input = input("Entrez un nombre en base 16 que vous voulez convertir en base 2: ")

        if not hexadecimal_input:
            print("Veuillez entrer une valeur.")
            continue  # Revenir au début de la boucle

        decimal_result = 0
        hexadecimal_input = hexadecimal_input.upper()  # Assurez-vous que les lettres hexadécimales sont en majuscules

        try:
            for char in hexadecimal_input:
                if char in "0123456789":
                    decimal_result = decimal_result * 16 + int(char)
                elif 'A' <= char <= 'F':
                    decimal_result = decimal_result * 16 + ord(char) - ord('A') + 10
                else:
                    raise ValueError("Assurez-vous d'entrer un nombre en base 16 que vous voulez convertir en base 2")

            # Maintenant, convertissez le nombre décimal en base 2
            decimal_number = decimal_result
            binaire = []

            if decimal_number == 0:
                print(f"Le nombre {decimal_number} en base 10 équivaut à 0 en base 2.")
            else:
                while decimal_number != 0:
                    quotient = decimal_number // 2
                    rest = decimal_number % 2
                    binaire.insert(0, str(rest))  # Ajoutez le bit au début de la liste sous forme de chaîne
                    decimal_number = quotient

                binary_str = ''.join(binaire)  # Convertir la liste en une seule chaîne
                print(f"Le nombre {decimal_result} en base 10(decimal) correspond à {binary_str} en base 2(binaire).")
            break
        except ValueError as e:
            print(f"Erreur : {e}")

convert_hex_to_bin()