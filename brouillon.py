def convert_base():
    while True:
        print("Choisissez le type de conversion :")
        print("1. Convertir binaire en décimal")
        print("2. Convertir binaire en hexadécimal")
        print("3. Convertir décimal en binaire")
        print("4. Convertir décimal en hexadécimal")
        print("5. Convertir hexadécimal en binaire")
        print("6. Convertir hexadécimal en décimal")

        choix = input("Entrez le numéro de votre choix : ")

        if choix == '1':
            binary_input = input("Entrez un nombre binaire que vous voulez convertir en décimal : ")
            try:
                decimal_result = int(binary_input, 2)
                print(f"Le nombre binaire {binary_input} correspond à {decimal_result} en décimal.")
            except ValueError:
                print("Erreur : Entrée binaire invalide.")
        elif choix == '2':
            binary_input = input("Entrez un nombre binaire que vous voulez convertir en hexadécimal : ")
            try:
                decimal_input = int(binary_input, 2)
                hexadecimal_result = convert_dec_to_hex(decimal_input)
                print(f"Le nombre binaire {binary_input} correspond à {hexadecimal_result} en hexadécimal.")
            except ValueError:
                print("Erreur : Entrée binaire invalide.")
        elif choix == '3':
            decimal_input_str = input("Entrez un nombre en base 10 que vous souhaitez convertir en binaire : ")
            try:
                decimal_input = int(decimal_input_str)
                binary_result = convert_dec_to_bin(decimal_input)
                print(f"Le nombre décimal {decimal_input} correspond à {binary_result} en binaire.")
            except ValueError:
                print("Erreur : Entrée décimale invalide.")
        elif choix == '4':
            decimal_input_str = input("Entrez un nombre en base 10 que vous souhaitez convertir en hexadécimal : ")
            try:
                decimal_input = int(decimal_input_str)
                hexadecimal_result = convert_dec_to_hex(decimal_input)
                print(f"Le nombre décimal {decimal_input} correspond à {hexadecimal_result} en hexadécimal.")
            except ValueError:
                print("Erreur : Entrée décimale invalide.")
        # Ajoutez ici les autres choix
        else:
            print("Choix invalide. Veuillez entrer 1, 2, 3, 4, 5, ou 6 pour choisir une option.")

        choice = input("Voulez-vous convertir un autre nombre ? (oui/non) ")
        if choice.lower() != 'oui':
            print("Fin du programme. Merci d'avoir utilisé ce programme.")
            break