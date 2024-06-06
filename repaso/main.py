# Crear una lista de elementos de tipo numérico. 
# Luego, mediante un ciclo for iterar esta lista e imprimir en la consola cada uno de los valores.
list = [1,2,3,4]

for x in list:
    print(x)
# Crear un diccionario con 4 atributos. Debe tener datos de tipo:
# Numérico
# String
# List (array) de números
# bool
# Luego, imprimir cada atributo de éste diccionario por separado, en la consola.
dicc = {
    "id": 1 , 
    "nombre": "a",
    "arr_n": [1,2,3,4],
    "active": True 
    }

for x in dicc:
    print(x)


# Crear una lista de diccionarios. Cada diccionario debe tener los siguientes atributos:
# Nombre --> string
# Apellido --> string
# Edad --> numero
# Lenguajes --> lista de strings
# Luego, mediante un for recorrer cada elemento de la lista e imprimir en la consola sus valores.
dicc = {
    "nombre": "Martha" , 
    "edad": 38,
    "arr_n": ["Python","C#","C"],
    }

for x,y in dicc.items():
    print(y)


# Crear una función llamada obtenerMayor que reciba dos números y devuelva el mayor de los dos.
# Luego, invocar a esta función pasándole dos numeros y mostrar el resultado en la consola.
# Invocarla nuevamente con otros números para probar el otro caso de prueba.
def obtenerMayor(n1,n2):
    if(n1 > n2):
        return n1
    else:
        return n2
    
print("Ejercicio 4:")
print(obtenerMayor(2,4))
print(obtenerMayor(8,4))


# Crear una función llamada eliminarRepetidos que reciba una lista y devuelva 
# los elementos de ésta lista pero sin elementos repetidos.
# Por ejemplo
# eliminarRepetidos([1,2,3,3,4,6,7,4,8])
# Debe devolver
# [1,2,3,4,6,7,8]

def eliminarRepetidos(arr):
    newArr = []
    for x in arr:
        if x in newArr:
            pass
        else:
            newArr.append(x)
    
    return newArr

print("Ejercicio 5:\n",eliminarRepetidos([1,1,1,1,2,3]))

# Crear una función que se llame convertirALista y reciba un string. 
# El string que recibe debe ser una serie de palabras, numeros o frases separadas por una coma (,).
# La función debe devolver una lista de elementos con la información contenida entre cada separador (,). Por ejemplo, si recibe:
# 'hola, hoy es Jueves, 6/6/2024,19hs'

# debe devolver:

# ['hola', ' hoy es Jueves', ' 6/6/2024', '19hs']

def convertirALista(txtInput):
    newArr = []
    newArr = txtInput.split(",")
    return newArr

print("Ejercicio 6:\n",convertirALista('hola, hoy es Jueves, 6/6/2024,19hs'))