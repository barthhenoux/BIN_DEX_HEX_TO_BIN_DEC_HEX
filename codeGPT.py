def decimal_to_binary(decimal):
    binary = ""
    if decimal == 0:
        binary = "0"
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary

def binary_to_decimal(binary):
    decimal = 0
    binary = binary[::-1]  # Inverser la chaîne binaire
    for i in range(len(binary)):
        if binary[i] == '1':
            decimal += 2 ** i
    return decimal

def decimal_to_hexadecimal(decimal):
    hexadecimal_chars = "0123456789ABCDEF"
    hexadecimal = ""
    if decimal == 0:
        hexadecimal = "0"
    while decimal > 0:
        remainder = decimal % 16
        hexadecimal = hexadecimal_chars[remainder] + hexadecimal
        decimal = decimal // 16
    return hexadecimal

def hexadecimal_to_decimal(hexadecimal):
    hexadecimal_chars = "0123456789ABCDEF"
    decimal = 0
    hexadecimal = hexadecimal[::-1]  # Inverser la chaîne hexadécimale
    for i in range(len(hexadecimal)):
        decimal += hexadecimal_chars.index(hexadecimal[i]) * (16 ** i)
    return decimal

def binary_to_hexadecimal(binary):
    decimal = binary_to_decimal(binary)
    hexadecimal = decimal_to_hexadecimal(decimal)
    return hexadecimal

def hexadecimal_to_binary(hexadecimal):
    decimal = hexadecimal_to_decimal(hexadecimal)
    binary = decimal_to_binary(decimal)
    return binary

# Exemples d'utilisation
decimal_value = 42
binary_value = "101010"
hexadecimal_value = "2A"

print(f"Decimal to Binary: {decimal_to_binary(decimal_value)}")
print(f"Binary to Decimal: {binary_to_decimal(binary_value)}")
print(f"Decimal to Hexadecimal: {decimal_to_hexadecimal(decimal_value)}")
print(f"Hexadecimal to Decimal: {hexadecimal_to_decimal(hexadecimal_value)}")
print(f"Binary to Hexadecimal: {binary_to_hexadecimal(binary_value)}")
print(f"Hexadecimal to Binary: {hexadecimal_to_binary(hexadecimal_value)}")