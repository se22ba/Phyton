# =========================================================
# UNIDAD 1 - INTRODUCCIÓN A LA PROGRAMACIÓN CON PYTHON
# =========================================================
#
# Este archivo funciona como:
# 1) Apunte teórico
# 2) Ejemplos ejecutables
#
# Todo lo que empieza con # es un comentario.
# Python ignora esos textos al ejecutar el programa.
#
# Los comentarios sirven para explicar lo que hace el código.
#
# =========================================================



# =========================================================
# 1. ¿QUÉ ES PROGRAMAR?
# =========================================================
#
# Programar es escribir instrucciones que la computadora
# debe seguir paso a paso.
#
# Ejemplo cotidiano:
#
# Si le decís a alguien cómo hacer mate:
#
# 1 calentar agua
# 2 poner yerba
# 3 poner agua
# 4 tomar
#
# Eso es un "programa": una lista de pasos.
#
# En programación hacemos lo mismo, pero con un lenguaje
# que entienda la computadora.
#
# Python es uno de esos lenguajes.
#
# =========================================================



# =========================================================
# 2. PRIMER PROGRAMA
# =========================================================
#
# print() sirve para mostrar información en la pantalla.
#

print("Hola mundo")
print("Este es mi primer programa en Python")



# =========================================================
# 3. VARIABLES
# =========================================================
#
# Una variable es un espacio donde guardamos información.
#
# Pensalo como una caja con una etiqueta.
#
# Etiqueta → nombre de variable
# Caja → dato guardado
#
# Ejemplo:
#

nombre = "Juan"
edad = 25

print("Nombre:", nombre)
print("Edad:", edad)


# Ejemplo cotidiano: sistema de una heladería

producto = "Helado"
precio = 1200
stock = 15

print("Producto:", producto)
print("Precio:", precio)
print("Stock disponible:", stock)



# =========================================================
# 4. TIPOS DE DATOS
# =========================================================
#
# En Python existen distintos tipos de datos.
#

# TEXTO (string)
nombre_cliente = "Carlos"

# ENTERO (int) → número sin decimales
edad_cliente = 33

# DECIMAL (float) → número con decimales
temperatura_freezer = -18.5

# BOOLEANO → verdadero o falso
puerta_abierta = False

print(nombre_cliente)
print(edad_cliente)
print(temperatura_freezer)
print(puerta_abierta)



# =========================================================
# 5. OPERACIONES MATEMÁTICAS
# =========================================================
#
# Python puede hacer cálculos como una calculadora.
#

a = 10
b = 3

# suma
print("Suma:", a + b)

# resta
print("Resta:", a - b)

# multiplicación
print("Multiplicación:", a * b)

# división
print("División:", a / b)

# división entera (solo el número entero)
print("División entera:", a // b)

# módulo → resto de una división
print("Módulo:", a % b)

# potencia
print("Potencia:", a ** b)



# =========================================================
# 6. ORDEN DE OPERACIONES
# =========================================================
#
# Python respeta el orden matemático:
#
# 1 paréntesis
# 2 potencias
# 3 multiplicación / división
# 4 suma / resta
#

resultado = (4 + 8) / 2 * 5 ** 2 - (9 + 3) / 2

print("Resultado de operación compleja:", resultado)



# =========================================================
# 7. INPUT (PEDIR DATOS AL USUARIO)
# =========================================================
#
# input() permite que el usuario escriba algo.
#

nombre_usuario = input("Ingrese su nombre: ")

print("Hola", nombre_usuario)



# =========================================================
# 8. CONVERSIÓN DE TIPOS
# =========================================================
#
# input() siempre devuelve TEXTO.
#
# Si queremos números debemos convertirlos.
#

numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese otro número: "))

suma = numero1 + numero2

print("La suma es:", suma)



# =========================================================
# 9. CADENAS DE TEXTO (STRINGS)
# =========================================================
#
# Un string es una secuencia de caracteres.
#
# Se escribe entre comillas.
#

cadena1 = "Hola"
cadena2 = "Mundo"

# concatenación = unir textos

frase = cadena1 + " " + cadena2

print(frase)



# =========================================================
# 10. LONGITUD DE TEXTO
# =========================================================
#
# len() cuenta cuántos caracteres tiene un texto
#

palabra = "Python"

print("Cantidad de letras:", len(palabra))



# =========================================================
# 11. INDEXACIÓN
# =========================================================
#
# Cada letra tiene una posición.
#
# Las posiciones empiezan en 0
#

print(palabra[0])  # primera letra
print(palabra[1])  # segunda letra
print(palabra[-1]) # última letra



# =========================================================
# 12. SLICING (CORTAR TEXTO)
# =========================================================
#
# Permite extraer partes de una cadena.
#

texto = "Programacion con Python"

print(texto[0:12])   # Programacion
print(texto[18:])    # Python
print(texto[:12])    # desde inicio
print(texto[::2])    # salta caracteres



# =========================================================
# 13. MÉTODOS DE TEXTO
# =========================================================
#
# Los métodos son funciones que actúan sobre textos.
#

frase = "Python es divertido"

# convertir a mayúsculas
print(frase.upper())

# convertir a minúsculas
print(frase.lower())

# reemplazar texto
print(frase.replace("divertido", "facil"))

# buscar posición de palabra
print(frase.find("es"))



# =========================================================
# 14. EJEMPLO COMPLETO
# =========================================================
#
# Programa simple de venta.
#

print("\n--- SISTEMA DE VENTA SIMPLE ---")

producto = input("Producto: ")
precio = float(input("Precio: "))
cantidad = int(input("Cantidad: "))

total = precio * cantidad

print("Producto:", producto)
print("Total a pagar:", total)



# =========================================================
# FIN DEL ARCHIVO
# =========================================================