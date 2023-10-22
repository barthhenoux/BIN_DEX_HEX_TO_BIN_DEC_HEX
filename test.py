def dec_to_bin(dtb):
    
    nombre=int(input("Entrez un nombre decimal que vous sohaitez convertir en binaire: "))
    nombre_decimal=nombre

    if nombre==0:
        print("Le nombre 0 en base 10 équivaut à 0 en base 2")
    else:
        while nombre!=0:
            quotient=nombre/2
            reste=nombre%2
            print(reste)
            nombre=quotient

    print("Le nombre",nombre_decimal,"en base 10 correspond à la suite de 0 et de 1 préceente notée du bas vers le haut")