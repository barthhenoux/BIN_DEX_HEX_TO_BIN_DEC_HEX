def convert_bin_to_dec():
    while True:
        # Demandez à l'utilisateur de saisir un nombre binaire
        binary_number = input("Entrez un nombre en base 2(binaire) que vous souhaitez convertir en base 10(decimal): ")

        if not binary_number:
            print("Veuillez entrer une valeur.")
            continue  # Revenir au début de la boucle

        if all(bit in "01" for bit in binary_number):
            # Initialisez la variable pour stocker le résultat en décimal
            decimal_number = 0

            # Parcourez les chiffres binaires de droite à gauche
            for i in range(len(binary_number)):
                # Obtenez le chiffre binaire à la position i (de droite gauch àe)
                number_binary = int(binary_number[-(i + 1)])

                # Ajoutez la contribution du chiffre binaire actuel au résultat en décimal
                decimal_number += number_binary * (2 ** i)

            # Affichez le résultat en décimal
            print(f"Le nombre binaire {binary_number} correspond à {decimal_number} en décimal.")
            break
        else:
            print("Erreur: Pensez à entrez un nombre en base 2 que vous souhaitez convertir en base 10")

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
                    remainder = decimal_input % 16  # calcul du remainder de la division par 16
                    hexadecimal = hexadecimal_chars[remainder] + hexadecimal  # Add the character corresponding to the remainder
                    decimal_input = decimal_input // 16  # Integer division by 16

                print(f"Le nombre {decimal_input_str} en base 10(decimal) correspond à {hexadecimal} en base 16(hexadecimal)")
            break  # Sortir de la boucle après une conversion réussie

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

def convert_bin_to_hex():
    while True:
        # Demandez à l'utilisateur de saisir un nombre binaire
        binary_number = input("Entrez un nombre en base 2 que vous voulez convertir en base 16: ")

        if not binary_number:
            print("Veuillez entrer une valeur.")
            continue  # Revenir au début de la boucle


        if all(bit in "01" for bit in binary_number):
            # Initialisez la variable pour stocker le résultat en décimal
            decimal_number = 0

            # Parcourez les chiffres binaires de droite à gauche
            for i in range(len(binary_number)):
                # Obtenez le chiffre binaire à la position i (de droite à gauche)
                chiffre_binaire = int(binary_number[-(i + 1)])

                # Ajoutez la contribution du chiffre binaire actuel au résultat en décimal
                decimal_number += chiffre_binaire * (2 ** i)


            # Maintenant, convertissez le nombre décimal en base 16
            hexadecimal_chars = "0123456789ABCDEF"
            nombre_hexadecimal = ""

            if decimal_number == 0:
                nombre_hexadecimal = "0"
            else:
                while decimal_number > 0:
                    rest = decimal_number % 16  # Calculez le reste de la division par 16
                    nombre_hexadecimal = hexadecimal_chars[rest] + nombre_hexadecimal  # Ajoutez le caractère correspondant au reste
                    decimal_number = decimal_number // 16  # Division entière par 16

            print(f"Le nombre {binary_number} en base 2(binaire) correspond à {nombre_hexadecimal} en base 16(hexadecimal)")
            break
        else:
            print("Erreur. Pensez à entrer un nombre en base 2 que vous souhaitez convertir en base 16.")


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

def convert_base():
    nchoice = "123456"
    choix = ""
    choice = "oui"  # Initialisez la variable choice ici pour éviter l'erreur
    print("\nBienvenue sur OBM. Ce programme vous permet de convertir une base 2,10 ou 16 en une autre des 3 trois bases citées.\n")

    print("Choisissez le type de conversion:\n")
    print("1. Convertir binaire en décimal")
    print("2. Convertir binaire en hexadécimal")
    print("3. Convertir décimal en binaire")
    print("4. Convertir décimal en hexadécimal")
    print("5. Convertir hexadécimal en binaire")
    print("6. Convertir hexadécimal en décimal\n")
    
    choix = input("Entrez le numéro correspondant à la conversion de votre choix: ")

    while not choix in nchoice:
        print("Erreur:Veuillez entrez un chiffre entre 1 et 6 correspondant à la conversion de votre choix")
        print("Choisissez le type de conversion:\n")
        print("1. Convertir binaire en décimal")
        print("2. Convertir binaire en hexadécimal")
        print("3. Convertir décimal en binaire")
        print("4. Convertir décimal en hexadécimal")
        print("5. Convertir hexadécimal en binaire")
        print("6. Convertir hexadécimal en décimal\n")
        
        choix = input("Entrez le numéro de votre choix : ")

        if choix not in nchoice:
            print("Choix invalide. Veuillez entrer 1, 2, 3, 4, 5, ou 6 pour choisir une option.")

    if choix == '1':
        convert_bin_to_dec()
    elif choix == '2':
        convert_bin_to_hex()
    elif choix == '3':
        convert_dec_to_bin()
    elif choix == '4':
        convert_dec_to_hex()
    elif choix == '5':
        convert_hex_to_bin()
    elif choix == '6':
        convert_hex_to_dec()

    choice = input("\nVoulez-vous convertir un autre nombre? (oui/non):").lower()
    if choice == 'oui':
        convert_base()
    elif choice == 'non':  
        print("\nFin du programme. Merci d'avoir utilisé OBM.\n")
    else: 
        print('\nChoix invalide. Veuillez entrez "oui" ou "non"\n')

# Appeler la fonction principale pour commencer le programme
convert_base()


