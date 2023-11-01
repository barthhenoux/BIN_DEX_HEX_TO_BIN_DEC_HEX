def hex_to_dec(hexadecimal_input):
    try:
        # Vérifier si l'entrée contient des caractères hexadécimaux valides
        if not all(char in "0123456789ABCDEFabcdef" for char in hexadecimal_input):
            raise ValueError("Caractère hexadécimal invalide")

        # Convertir l'entrée hexadécimale en décimal
        decimal_result = int(hexadecimal_input, 16)
        return decimal_result

    except ValueError as e:
        print(f"Erreur : {e}")
        return None

# Demander à l'utilisateur d'entrer un nombre hexadécimal
while True:
    hexadecimal_input = input("Entrez un nombre hexadécimal que vous voulez convertir en base décimale: ")
    decimal_result = hex_to_dec(hexadecimal_input)

    # Vérifier si la conversion a réussi avant d'afficher le résultat
    if decimal_result is not None:
        print(f"Le nombre décimal correspondant est : {decimal_result}")
        break

#chatgptpihvsogbeorghveogjhoeurihbvgfpoeuihpgisdvhgbpvodsurghbzprçeguhveqporbvguhesrbgpvoejshvgpbdsojghvresdpbgiuerhgvbpdroguvhdomvdurbghomdvguveqrvhgomuiebgemqiug