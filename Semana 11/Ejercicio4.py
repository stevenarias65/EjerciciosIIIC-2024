
n = 1

while n<10:
    print("estoy dentro del mientras",n)
    n = n + 1

#opcion = "si"
#while opcion.lower() == "si":
#    print("desea continuar")
#    opcion = input()


contador = 1
while contador < 10:
    print(contador)
    if contador == 2:
        break
    contador = contador + 1


contador = 1
while contador < 10:
    print(contador)
    if contador == 2:
        contador = 7
        continue

    contador = contador + 1

