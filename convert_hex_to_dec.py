def convert_hex_to_dec():
    while True:
        # Demander à l'utilisateur d'entrer un nombre hexadécimal
        hexadecimal_input = input("Entrez un nombre en base 16 que vous souhaitez convertir en base 10: ")

        if not hexadecimal_input :
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
                    raise ValueError("Erreur: Pensez à entrez un nombre en base 16 que vous souhaitez convertir en base 10")

            print(f"Le nombre {hexadecimal_input} correspond à {decimal_result}")
            break  # Sortir de la boucle si la conversion est réussie

        except ValueError as e:
            print(f"Erreur : {e}")

# Appeler la fonction pour effectuer la conversion
convert_hex_to_dec()

