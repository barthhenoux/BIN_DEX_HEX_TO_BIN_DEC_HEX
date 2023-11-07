def convert_bin_to_dec():
    while True:
        # Demandez à l'utilisateur de saisir un nombre binaire
        nombre_binaire = input("Entrez un nombre en base 2 que vous souhaitez convertir en base 10: ")

        if all(bit in "01" for bit in nombre_binaire):
            # Initialisez la variable pour stocker le résultat en décimal
            nombre_decimal = 0

            # Parcourez les chiffres binaires de droite à gauche
            for i in range(len(nombre_binaire)):
                # Obtenez le chiffre binaire à la position i (de droite gauch àe)
                chiffre_binaire = int(nombre_binaire[-(i + 1)])

                # Ajoutez la contribution du chiffre binaire actuel au résultat en décimal
                nombre_decimal += chiffre_binaire * (2 ** i)

            # Affichez le résultat en décimal
            print("Le nombre binaire", nombre_binaire, "correspond à", nombre_decimal, "en décimal.")
            break
        else:
            print("Erreur: Pensez à entrez un nombre en base 2 (0 et 1 uniquement) que vous souhaitez convertir en base 10")

def convert_dec_to_bin():
    while True:
        decimal_input_str = input("Entrez un nombre décimal que vous souhaitez convertir en binaire: ")

        if not decimal_input_str:
            print("Veuillez entrer une valeur.")
            continue  # Revenir au début de la boucle

        try:
            nombre_decimal = int(decimal_input_str)
        except ValueError:
            print("Erreur: Pensez à entrez un nombre en base 10 que vous souhaitez convertir en base 2")
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

                print(f"Le nombre hexadecimal correspondant est {hexadecimal}")
            break  # Sortir de la boucle après une conversion réussie

def convert_hex_to_dec():
    while True:
        # Demander à l'utilisateur d'entrer un nombre hexadécimal
        hexadecimal_input = input("Entrez un nombre en base 16 que vous souhaitez convertir en base 10: ")

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

            print(f"Le nombre décimal correspondant est : {decimal_result}")
            break  # Sortir de la boucle si la conversion est réussie

        except ValueError as e:
            print(f"Erreur : {e}")

def convert_bin_to_hex():
    nombre= int(input("Entrez un nombre en base 10 que vous souhaitez convertir en base 16: "))
    nombre=convert_bin_to_dec(nombre)
    nombre=convert_dec_to_hex(nombre)
    print(nombre)


def convert_hex_to_bin():
    nombre=int(input("Entrez un nombre en base 16 que vous souhaitez convertir en base 2"))
    nombre = convert_hex_to_dec(nombre)
    nombre=convert_dec_to_bin(nombre)
    print(nombre)

def convert_base():
    nchoix = "123456"
    choix = ""
    choice = "oui"  # Initialisez la variable choice ici pour éviter l'erreur

    print("Choisissez le type de conversion:")
    print("1. Convertir binaire en décimal")
    print("2. Convertir binaire en hexadécimal")
    print("3. Convertir décimal en binaire")
    print("4. Convertir décimal en hexadécimal")
    print("5. Convertir hexadécimal en binaire")
    print("6. Convertir hexadécimal en décimal")
    
    choix = input("Entrez le numéro correspondant à la conversion de votre choix : ")

    while not choix in nchoix:
        print("Erreur:Veuillez entrez un chiffre entre 1 et 6 correspondant à la conversion de votre choix")
        print("Choisissez le type de conversion :")
        print("1. Convertir binaire en décimal")
        print("2. Convertir binaire en hexadécimal")
        print("3. Convertir décimal en binaire")
        print("4. Convertir décimal en hexadécimal")
        print("5. Convertir hexadécimal en binaire")
        print("6. Convertir hexadécimal en décimal")
        
        choix = input("Entrez le numéro de votre choix : ")

        if choix not in nchoix:
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

    choice = input("Voulez-vous convertir un autre nombre? (oui/non):")
    if choice == 'oui':
        convert_base()
    elif choice == 'non':  
        print("Fin du programme, merci d'avoir utilisé ce programme.")
    else: 
        print('Choix invalide. Veuillez entrez "oui" ou "non"')

# Appeler la fonction principale pour commencer le programme
convert_base()


