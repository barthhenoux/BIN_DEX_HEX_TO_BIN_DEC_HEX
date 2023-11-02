def convert_dec_to_hex(dth):
    if dth == 0:
        return "0"  # Handling the case where the decimal number is 0

    hexadecimal_chars = "0123456789ABCDEF"
    hexadecimal = ""

    while dth > 0:
        remainder = dth % 16  # Calculate the remainder of the division by 16
        hexadecimal = hexadecimal_chars[remainder] + hexadecimal  # Add the character corresponding to the remainder
        dth = dth // 16  # Integer division by 16

    return hexadecimal

# Demander à l'utilisateur d'entrer un nombre décimal 
decimal_input_str = input("Enter a decimal number you want to convert to hexadecimal: ")

# Tant que l'entrée n'est pas un nombre décimal valide, continuez à demander à l'utilisateur
while True:
    if not decimal_input_str:
        print("Veuillez entrer une valeur.")
        decimal_input_str = input("Enter a decimal number you want to convert to hexadecimal: ")
        continue  # Revenir au début de la boucle sans essayer de convertir

    try:
        decimal_input = int(decimal_input_str)
    except ValueError:
        print("Invalid input. Please make sure to enter a valid decimal number.")
        decimal_input_str = ""  # Réinitialiser l'entrée
    else:
        hexadecimal_result = convert_dec_to_hex(decimal_input)
        print(f"The corresponding hexadecimal number is: {hexadecimal_result}")
        break


def convert_dec_to_bin():
    nombre = int(input("Entrez un nombre décimal que vous souhaitez convertir en binaire: "))
    nombre_decimal = nombre
    binaire = []  # Créez une liste pour stocker les bits binaires

    if nombre == 0:
        print("Le nombre 0 en base 10 équivaut à 0 en base 2")
    else:
        while nombre != 0:
            quotient = nombre // 2
            reste = nombre % 2
            binaire.insert(0, str(reste))  # Ajoutez le bit au début de la liste sous forme de chaîne
            nombre = quotient

    binaire_str = ''.join(binaire)  # Convertir la liste en une seule chaîne
    print(f"Le nombre {nombre_decimal} en base 10 correspond à {binaire_str} en base 2.")

# Appeler la fonction pour effectuer la conversion
#convert_dec_to_bin()

def convert_bin_to_dec():

    # Demandez à l'utilisateur de saisir un nombre binaire
    nombre_binaire = input("Entrez un nombre binaire que vous voulez convertir en nombre decimal: ")

    # Initialisez la variable pour stocker le résultat en décimal
    nombre_decimal = 0

    # Parcourez les chiffres binaires de droite à gauche
    for i in range(len(nombre_binaire)):
        # Obtenez le chiffre binaire à la position i (de droite à gauche)
        chiffre_binaire = int(nombre_binaire[-(i + 1)])
        
        # Ajoutez la contribution du chiffre binaire actuel au résultat en décimal
        nombre_decimal += chiffre_binaire * (2 ** i)

    # Affichez le résultat en décimal
    print("Le nombre binaire", nombre_binaire, "correspond à", nombre_decimal, "en décimal.")  

# Appeler la fonction pour effectuer la conversion
#convert_bin_to_dec()

def convert_bin_to_hex():
    nombre= int(input("Entrez un nombre en binaire que vous voulez convertir en nombre hexadecimal: "))
    nombre=convert_bin_to_dec(nombre)
    nombre=convert_dec_to_hex(nombre)
    print(nombre)


def convert_hex_to_bin():
    nombre=int(input("Entrez un nombre en base 16 que vous voulez convertir en un nombre en base 2"))
    nombre=convert_dec_to_bin
