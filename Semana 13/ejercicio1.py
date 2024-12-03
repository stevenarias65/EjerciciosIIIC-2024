ejemploLista = ["Ronald","Michelle","Lisbeth","hellen"]#Lista Arreglo 
ejemploTupla = ("Ronald","Michelle","Lisbeth","hellen")#Tupla


ejemploLista[0] = "Steven" 


print(ejemploLista[0])


#{} diccionario
#[] lista arreglo
#() tupla


ejemploDiccionario = {
    "nombre" : "Ronald",
    "apellidos" : "Arias Fallas",
    "edad" : 31,
    "titulos" : ["bachillerato","licenciatura","maestria"]
  } #diccionario

print(ejemploDiccionario["nombre"])
print(ejemploDiccionario["titulos"][0])

print(ejemploDiccionario.keys())
print(ejemploDiccionario.values())

for i in ejemploDiccionario.keys():
    print(i)

print("------")
for clave,valor in ejemploDiccionario.items():
    print(clave,"--->",valor)
    if type(valor) == list:
        for i in valor:
            print("Tengo el titulo ", i)


