numeros= [1, 2, 3, 4, 5]
numero_buscado = int(input("Ingresa un número: "))
encontrado = False
if numero_buscado in numeros:
    print("El número", numero_buscado, "sí está en la lista.")
else:
    print("El número", numero_buscado, "no está en la lista.")