def dec_to_bin():
    nombre = int(input("Entrez un nombre décimal que vous souhaitez convertir en binaire: "))
    decimal_number = nombre
    binaire = []  # Créez une liste pour stocker les bits binaires

    if nombre == 0:
        print("Le nombre 0 en base 10 équivaut à 0 en base 2")
    else:
        while nombre != 0:
            quotient = nombre // 2
            rest = nombre % 2
            binaire.insert(0, str(rest))  # Ajoutez le bit au début de la liste sous forme de chaîne
            nombre = quotient

    binary_str = ''.join(binaire)  # Convertir la liste en une seule chaîne
    print(f"Le nombre {decimal_number} en base 10 correspond à {binary_str} en base 2.")

# Appeler la fonction pour effectuer la conversion
dec_to_bin()
