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

convert_bin_to_hex()