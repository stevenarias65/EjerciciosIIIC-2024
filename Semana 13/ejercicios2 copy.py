import os

os.system("clear") #es para mac
#os.system("cls") #es para windows

##Vamos a realizar una agenda
agenda = {}

while True:
    try:
        print("1. Añadir / Modificar")
        print("2. buscar")
        print("3. borrar")
        print("4. mostrar")
        print("5. salir")

        opcion = int(input("Por favor digite un valor: "))
        if opcion == 1:

            nombre = input("Digite el nombre del contacto: ").upper()
            if nombre in agenda.keys():
                print(nombre," Ya existe un telefono asociado y es: ",agenda[nombre])
                respuesta = input("Preciosa s si quiere cambiar el numero o otra tecla si no: ")
                if respuesta.upper() == "S":
                    numero = input("Dame el numero numero: ")
                    agenda[nombre] = numero
                    os.system("clear")
                else: 
                    print("Se mantuvo el numero")
                    os.system("clear")
            else:
                numero = input("Digite el numero de telefono: ")
                agenda[nombre] = numero
                os.system("clear")
        elif opcion == 2:
            buscar = input("Nombre del contacto a buscar: ").upper()
            if buscar in agenda.keys():
                print(agenda[buscar])
            else:
                print("no lo encontro")
            for clave,valor in agenda.items():
                if clave.startswith(buscar):
                    print(clave, " tiene el telefono asociado ", valor)
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
    except Exception:
        print("error intente de nuevo")






