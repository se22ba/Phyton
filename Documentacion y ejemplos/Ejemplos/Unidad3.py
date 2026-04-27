# ============================================================
# UNIDAD 3
# MÉTODOS DE COLECCIONES Y OPERADORES BÁSICOS
# ============================================================



# ============================================================
# 1) LISTAS
# ============================================================

# Una LISTA es como una mesa donde apoyas cosas.
# Cada cosa ocupa una posición.

# Ejemplo cotidiano:
# Una lista de compras

lista_compras = ["pan", "leche", "huevos"]

print("Lista inicial:", lista_compras)



# ------------------------------------------------------------
# append()
# agrega un elemento al FINAL de la lista
# ------------------------------------------------------------

lista_compras.append("queso")

print("Agregamos queso:", lista_compras)



# ------------------------------------------------------------
# insert()
# agrega un elemento en una posición específica
# ------------------------------------------------------------

# insertar en posición 1 (segunda posición)

lista_compras.insert(1, "manteca")

print("Insertamos manteca:", lista_compras)



# ------------------------------------------------------------
# remove()
# elimina un elemento por su nombre
# ------------------------------------------------------------

lista_compras.remove("pan")

print("Quitamos pan:", lista_compras)



# ------------------------------------------------------------
# pop()
# elimina un elemento por su posición
# ------------------------------------------------------------

producto = lista_compras.pop(1)

print("Sacamos:", producto)
print("Lista ahora:", lista_compras)



# ------------------------------------------------------------
# count()
# cuenta cuántas veces aparece algo
# ------------------------------------------------------------

numeros = [1,2,3,2,4,2]

print("El numero 2 aparece:", numeros.count(2), "veces")



# ------------------------------------------------------------
# sort()
# ordena una lista
# ------------------------------------------------------------

numeros.sort()

print("Lista ordenada:", numeros)



# ------------------------------------------------------------
# reverse()
# invierte el orden
# ------------------------------------------------------------

numeros.reverse()

print("Lista invertida:", numeros)



# ============================================================
# 2) CONJUNTOS (SETS)
# ============================================================

# Un CONJUNTO es como una bolsa donde NO puede haber duplicados.

# Ejemplo cotidiano:
# personas que entraron a un evento

personas = {"Juan", "Ana", "Pedro"}

print("\nPersonas en el evento:", personas)



# ------------------------------------------------------------
# add()
# agrega un elemento
# ------------------------------------------------------------

personas.add("Maria")

print("Agregamos Maria:", personas)



# ------------------------------------------------------------
# remove()
# elimina un elemento
# ------------------------------------------------------------

personas.remove("Juan")

print("Quitamos Juan:", personas)



# ------------------------------------------------------------
# union()
# une dos conjuntos
# ------------------------------------------------------------

grupo1 = {"Ana", "Pedro"}
grupo2 = {"Pedro", "Maria"}

union = grupo1.union(grupo2)

print("Union de grupos:", union)



# ------------------------------------------------------------
# intersection()
# muestra elementos que se repiten
# ------------------------------------------------------------

interseccion = grupo1.intersection(grupo2)

print("Personas en ambos grupos:", interseccion)



# ------------------------------------------------------------
# difference()
# muestra elementos que están en uno pero no en el otro
# ------------------------------------------------------------

diferencia = grupo1.difference(grupo2)

print("Solo en grupo1:", diferencia)



# ============================================================
# 3) DICCIONARIOS
# ============================================================

# Un DICCIONARIO funciona como una agenda.
# Cada dato tiene una CLAVE y un VALOR.

# Ejemplo cotidiano:
# datos de una persona

persona = {
    "nombre": "Carlos",
    "edad": 30,
    "ciudad": "Buenos Aires"
}

print("\nDatos persona:", persona)



# ------------------------------------------------------------
# acceder a un valor
# ------------------------------------------------------------

print("Nombre:", persona["nombre"])



# ------------------------------------------------------------
# get()
# obtiene un valor sin romper el programa
# ------------------------------------------------------------

print("Edad:", persona.get("edad"))



# ------------------------------------------------------------
# update()
# modifica datos
# ------------------------------------------------------------

persona.update({"edad": 31})

print("Edad actualizada:", persona)



# ------------------------------------------------------------
# keys()
# devuelve las claves
# ------------------------------------------------------------

print("Claves del diccionario:", persona.keys())



# ------------------------------------------------------------
# values()
# devuelve los valores
# ------------------------------------------------------------

print("Valores del diccionario:", persona.values())



# ------------------------------------------------------------
# items()
# devuelve clave + valor
# ------------------------------------------------------------

print("Elementos completos:", persona.items())



# ============================================================
# 4) MÉTODOS DE CADENAS (STRINGS)
# ============================================================

# Una cadena es simplemente texto.

texto = "Hola Mundo"



# ------------------------------------------------------------
# upper()
# convierte a mayúsculas
# ------------------------------------------------------------

print("\nMayúsculas:", texto.upper())



# ------------------------------------------------------------
# lower()
# convierte a minúsculas
# ------------------------------------------------------------

print("Minúsculas:", texto.lower())



# ------------------------------------------------------------
# capitalize()
# primera letra mayúscula
# ------------------------------------------------------------

texto2 = "hola mundo"

print("Capitalizado:", texto2.capitalize())



# ------------------------------------------------------------
# title()
# cada palabra empieza con mayúscula
# ------------------------------------------------------------

print("Titulo:", texto2.title())



# ------------------------------------------------------------
# count()
# cuenta cuántas veces aparece algo
# ------------------------------------------------------------

frase = "hola mundo hola universo"

print("Cantidad de 'hola':", frase.count("hola"))



# ------------------------------------------------------------
# find()
# busca una palabra y devuelve su posición
# ------------------------------------------------------------

print("Posición de 'mundo':", frase.find("mundo"))



# ------------------------------------------------------------
# split()
# separa palabras
# ------------------------------------------------------------

palabras = frase.split()

print("Palabras separadas:", palabras)



# ------------------------------------------------------------
# join()
# une una lista en un texto
# ------------------------------------------------------------

lista_palabras = ["Python", "es", "facil"]

frase_nueva = " ".join(lista_palabras)

print("Frase creada:", frase_nueva)



# ------------------------------------------------------------
# strip()
# elimina espacios al principio y final
# ------------------------------------------------------------

texto_espacios = "   hola mundo   "

print("Texto limpio:", texto_espacios.strip())



# ------------------------------------------------------------
# replace()
# reemplaza texto
# ------------------------------------------------------------

mensaje = "hola mundo"

mensaje = mensaje.replace("mundo", "Python")

print("Mensaje nuevo:", mensaje)



# ============================================================
# FIN DE LA UNIDAD
# ============================================================

print("\nUnidad 3 ejecutada correctamente")