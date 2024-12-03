import os

os.system("clear") #es para mac
#os.system("cls") #es para windows

##Vamos a realizar una agenda
agenda = {}

while True:
    print("1. Añadir")
    print("2. buscar")
    print("3. borrar")
    print("4. mostrar")
    print("5. salir")

    opcion = int(input("Por favor digite un valor: "))
    if opcion == 1:
        nombre = input("Digite el nombre del contacto: ").upper()
        numero = input("Digite el numero de telefono: ")
        agenda[nombre] = numero
        os.system("clear")
    elif opcion == 2:
         buscar = input("Nombre del contacto a buscar: ").upper()
         if buscar in agenda.keys():
             print(agenda[buscar])
         else:
             print("no lo encontro")
    elif opcion == 3:
        borrar = input("Digite el nombre que desea borrar: ").upper()
        if borrar in agenda.keys():
            del agenda[borrar]
        os.system("clear")
    elif opcion == 4:
        for i,j in agenda.items():
            print(i.title()," El numero es: ", j)
    elif opcion == 5:
        break
    else:
        print("Opcion incorrecta intente de nuevo")

             


