# =========================================================
# UNIDAD 2 - ESTRUCTURAS DE DATOS EN PYTHON
# Listas, Tuplas, Conjuntos (Sets) y Diccionarios
# =========================================================
#
# En esta unidad aprendemos a guardar MUCHOS datos juntos.
#
# En la vida real casi nunca trabajamos con un solo dato.
#
# Ejemplo cotidiano:
#
# una lista de compras
# una lista de alumnos
# un inventario de productos
#
# Para resolver esto existen estructuras de datos.
#
# En Python las principales son:
#
# LISTAS
# TUPLAS
# CONJUNTOS
# DICCIONARIOS
#
# =========================================================



# =========================================================
# 1. LISTAS
# =========================================================
#
# Una lista es una colección ordenada de elementos.
#
# Se escribe usando corchetes []
#
# Las listas pueden contener:
# números
# texto
# booleanos
# incluso otras listas
#
# Además son MUTABLES → se pueden modificar.
#
# Ejemplo cotidiano:
#
# lista de compras
#

lista_compras = ["pan", "leche", "huevos", "queso"]

print("Lista de compras:", lista_compras)



# =========================================================
# ACCEDER A ELEMENTOS DE UNA LISTA
# =========================================================
#
# Cada elemento tiene una posición llamada índice.
#
# IMPORTANTE:
# los índices empiezan en 0
#

frutas = ["manzana", "banana", "naranja"]

print(frutas[0])  # manzana
print(frutas[1])  # banana
print(frutas[2])  # naranja



# =========================================================
# SLICING (CORTAR LISTAS)
# =========================================================
#
# Permite obtener partes de una lista
#

numeros = [0,1,2,3,4,5,6,7,8,9]

print(numeros[0:5])  # primeros 5
print(numeros[5:])   # desde el 5 hasta el final
print(numeros[2:7])  # subconjunto



# =========================================================
# MODIFICAR LISTAS
# =========================================================

productos = ["pan", "leche", "huevos"]

# agregar elemento al final
productos.append("manteca")

print(productos)

# insertar en posición específica
productos.insert(1, "queso")

print(productos)

# eliminar elemento
productos.remove("pan")

print(productos)



# =========================================================
# EJEMPLO REAL CON LISTAS
# =========================================================
#
# Sistema simple de notas de alumnos
#

notas = [7, 8, 10, 6, 9]

promedio = sum(notas) / len(notas)

print("Notas:", notas)
print("Promedio:", promedio)



# =========================================================
# 2. TUPLAS
# =========================================================
#
# Las tuplas son similares a las listas.
#
# Diferencia principal:
#
# SON INMUTABLES
#
# Es decir:
# NO se pueden modificar.
#
# Se usan cuando los datos no deben cambiar.
#
# Se escriben con paréntesis ()
#

coordenadas = (10, 20)

print("Coordenada X:", coordenadas[0])
print("Coordenada Y:", coordenadas[1])



# =========================================================
# EJEMPLO COTIDIANO DE TUPLAS
# =========================================================
#
# fecha de nacimiento
#

fecha_nacimiento = (25, "mayo", 2000)

print("Fecha:", fecha_nacimiento)



# =========================================================
# DIFERENCIA ENTRE LISTA Y TUPLA
# =========================================================

lista = [1,2,3]
tupla = (1,2,3)

lista.append(4)

print("Lista modificada:", lista)

# tupla.append(4)  # esto daría error



# =========================================================
# 3. CONJUNTOS (SETS)
# =========================================================
#
# Un conjunto es una colección:
#
# NO ordenada
# sin elementos repetidos
#
# Se escribe con llaves {}
#

numeros = {1,2,3,4,5}

print(numeros)



# =========================================================
# LOS CONJUNTOS ELIMINAN DUPLICADOS
# =========================================================

numeros = {1,2,2,3,3,4}

print(numeros)



# =========================================================
# OPERACIONES DE CONJUNTOS
# =========================================================

grupo_a = {1,2,3}
grupo_b = {3,4,5}

# unión
print("Union:", grupo_a | grupo_b)

# intersección
print("Interseccion:", grupo_a & grupo_b)

# diferencia
print("Diferencia:", grupo_a - grupo_b)



# =========================================================
# MÉTODOS DE CONJUNTOS
# =========================================================

numeros = {1,2,3}

numeros.add(4)
print(numeros)

numeros.remove(2)
print(numeros)



# =========================================================
# EJEMPLO REAL DE SET
# =========================================================
#
# lista de emails registrados
#

emails = {"a@mail.com", "b@mail.com"}

emails.add("c@mail.com")
emails.add("a@mail.com")

print(emails)



# =========================================================
# 4. DICCIONARIOS
# =========================================================
#
# Un diccionario guarda datos en pares:
#
# clave : valor
#
# Ejemplo cotidiano:
#
# agenda telefónica
#
# nombre → teléfono
#

persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Buenos Aires"
}

print(persona)



# =========================================================
# ACCEDER A VALORES
# =========================================================

print(persona["nombre"])
print(persona["edad"])



# =========================================================
# MODIFICAR DICCIONARIOS
# =========================================================

persona["edad"] = 31

persona["profesion"] = "programador"

print(persona)



# =========================================================
# ELIMINAR ELEMENTOS
# =========================================================

del persona["ciudad"]

print(persona)



# =========================================================
# MÉTODOS DE DICCIONARIOS
# =========================================================

print(persona.keys())
print(persona.values())
print(persona.items())



# =========================================================
# EJEMPLO COMPLETO
# =========================================================
#
# inventario simple de una tienda
#

inventario = {
    "manzanas": 10,
    "naranjas": 5,
    "peras": 8
}

print("Inventario actual:", inventario)

inventario["manzanas"] += 5

print("Inventario actualizado:", inventario)



# =========================================================
# RESUMEN DE LA UNIDAD
# =========================================================
#
# LISTAS
# colección ordenada y modificable
#
# TUPLAS
# colección ordenada pero NO modificable
#
# SETS
# colección sin duplicados y sin orden
#
# DICCIONARIOS
# pares clave → valor
#
# =========================================================