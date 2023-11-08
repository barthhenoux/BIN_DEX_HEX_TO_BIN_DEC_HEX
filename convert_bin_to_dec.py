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

# Appeler la fonction pour effectuer la conversion
convert_bin_to_dec()