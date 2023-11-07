def convert_dec_to_bin():
    while True:
        decimal_input_str = input("Entrez un nombre décimal que vous souhaitez convertir en binaire: ")

        if not decimal_input_str:
            print("Veuillez entrer une valeur.")
            continue  # Revenir au début de la boucle

        try:
            nombre_decimal = int(decimal_input_str)
        except ValueError:
            print("Entrée non valide. Veuillez vous assurer d'entrer un nombre décimal valide.")
        else:
            nombre = nombre_decimal
            binaire = []  # Créez une liste pour stocker les bits binaires

            if nombre == 0:
                print(f"Le nombre {nombre_decimal} en base 10 équivaut à 0 en base 2")
            else:
                while nombre != 0:
                    quotient = nombre // 2
                    reste = nombre % 2
                    binaire.insert(0, str(reste))  # Ajoutez le bit au début de la liste sous forme de chaîne
                    nombre = quotient

                binaire_str = ''.join(binaire)  # Convertir la liste en une seule chaîne
                print(f"Le nombre {nombre_decimal} en base 10 correspond à {binaire_str} en base 2.")
            break  # Sortir de la boucle après une conversion réussie

convert_dec_to_bin()