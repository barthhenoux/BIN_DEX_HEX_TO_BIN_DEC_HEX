def dec_to_bin():
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
dec_to_bin()
