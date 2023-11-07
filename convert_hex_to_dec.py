def hex_to_dec():
    while True:
        # Demander à l'utilisateur d'entrer un nombre hexadécimal
        hexadecimal_input = input("Entrez un nombre hexadécimal que vous voulez convertir en base décimale: ")

        decimal_result = 0
        hexadecimal_input = hexadecimal_input.upper()  # Assurez-vous que les lettres hexadécimales sont en majuscules

        try:
            for char in hexadecimal_input:
                if char in "0123456789":
                    decimal_result = decimal_result * 16 + int(char)
                elif 'A' <= char <= 'F':
                    decimal_result = decimal_result * 16 + ord(char) - ord('A') + 10
                else:
                    raise ValueError("Pensez à entrez un nombre en base 16 que vous voulez convertir en base 10")

            print(f"Le nombre décimal correspondant est : {decimal_result}")
            break  # Sortir de la boucle si la conversion est réussie

        except ValueError as e:
            print(f"Erreur : {e}")

# Appeler la fonction pour effectuer la conversion
hex_to_dec()

#chatgptpihvsogbeorghveogjhoeurihbvgfpoeuihpgisdvhgbpvodsurghbzprçeguhveqporbvguhesrbgpvoejshvgpbdsojghvresdpbgiuerhgvbpdroguvhdomvdurbghomdvguveqrvhgomuiebgemqiug