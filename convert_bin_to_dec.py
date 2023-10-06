def convert_bin_to_dec ():

    # Demandez à l'utilisateur de saisir un nombre binaire
    nombre_binaire = input("Entrez un nombre binaire : ")

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

convert_bin_to_dec()