def convert_bin_to_dec():
    while True:
        # Demandez à l'utilisateur de saisir un nombre binaire
        nombre_binaire = input("Entrez un nombre binaire que vous voulez convertir en nombre décimal: ")

        if all(bit in "01" for bit in nombre_binaire):
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
            break
        else:
            print("Entrée invalide. Assurez-vous de saisir un nombre binaire valide (0 et 1 uniquement).")

# Appeler la fonction pour effectuer la conversion
convert_bin_to_dec()