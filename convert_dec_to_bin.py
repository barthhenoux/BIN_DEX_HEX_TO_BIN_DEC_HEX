def convert_dec_to_bin():
    while True:
        decimal_input_str = input("Entrez un nombre en base 10 que vous souhaitez convertir en base 2: ")

        if not decimal_input_str:
            print("Veuillez entrer une valeur.")
            continue  # Revenir au début de la boucle

        try:
            decimal_number = int(decimal_input_str)
        except ValueError:
            print("Erreur: Pensez à entrez un nombre en base 10 que vous souhaitez convertir en base 2")
        else:
            number = decimal_number
            binary = []  # Créez une liste pour stocker les bits binaires

            if number == 0:
                print(f"Le nombre {decimal_number} en base 10 équivaut à 0 en base 2")
            else:
                while number != 0:
                    quotient = number // 2
                    rest = number % 2
                    binary.insert(0, str(rest))  # Ajoutez le bit au début de la liste sous forme de chaîne
                    number = quotient

                binary_str = ''.join(binary)  # Convertir la liste en une seule chaîne
                print(f"Le nombre {decimal_number} en base 10 correspond à {binary_str} en base 2.")
            break  # Sortir de la boucle après une conversion réussie

convert_dec_to_bin()