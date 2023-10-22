def convert_hex_to_dec(htd):
    
    
    
def convert_dec_to_hex(dth):
    if dth == 0:
        return "0"  # Gestion du cas où le nombre décimal est 0

    hexadecimal_chars = "0123456789ABCDEF"
    hexadecimal = ""

    while dth > 0:
        remainder = dth % 16  # Calcul du reste de la division par 16
        hexadecimal = hexadecimal_chars[remainder] + hexadecimal  # Ajout du caractère correspondant au reste
        dth = dth // 16  # Division entière par 16

    return hexadecimal

# Demander à l'utilisateur d'entrer un nombre décimal
decimal_input = int(input("Entrez un nombre décimal : "))

# Appeler la fonction de conversion et afficher le résultat
hexadecimal_result = convert_dec_to_hex(decimal_input)
print(f"Le nombre hexadécimal correspondant est : {hexadecimal_result}")

    

def convert_hex_to_bin(htb):

# Demande à l'utilisateur d'entrer un nombre en base hexadécimale
hexadecimal = input("Entrez un nombre en base hexadécimale : ")

# Crée un dictionnaire pour la conversion des chiffres hexadécimaux en binaire
hex_to_binary = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
}

# Initialise une chaîne de caractères pour stocker le résultat binaire
binary = ""

# Convertit chaque chiffre hexadécimal en binaire et l'ajoute au résultat
for digit in hexadecimal:
    binary += hex_to_binary.get(digit, "")

# Affiche le résultat en base binaire
print("Le nombre en base binaire est :", binary)

    
    
def convert_bin_to_hex(bth):
    
    
def convert_dec_to_bin(dtb):
    
    
def convert_bin_to_dec(btd):
    
    
