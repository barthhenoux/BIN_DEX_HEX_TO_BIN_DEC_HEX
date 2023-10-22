# Demander à l'utilisateur d'entrer un nombre décimal
decimal_input = int(input("Entrez un nombre décimal que vous voulez convertir en base binaire: "))

# Vérifier si le nombre est négatif
is_negative = False
if decimal_input < 0:
    is_negative = True
    decimal_input = abs(decimal_input)

# Gérer le cas où le nombre décimal est 0
if decimal_input == 0:
    binary_result = "0"
else:
    binary_result = ""

# Effectuer la conversion en base binaire
while decimal_input > 0:
    remainder = decimal_input % 2  # Calcul du reste de la division par 2
    binary_result = str(remainder) + binary_result  # Ajout du bit correspondant au reste
    decimal_input = decimal_input // 2  # Division entière par 2

# Ajouter un signe négatif si nécessaire
if is_negative:
    binary_result = "-" + binary_result

# Afficher le résultat
print(f"Le nombre binaire correspondant est : {binary_result}")
