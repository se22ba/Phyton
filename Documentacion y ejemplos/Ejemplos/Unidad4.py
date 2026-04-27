# ============================================================
# UNIDAD 4
# CONTROL DE FLUJO EN PYTHON
# ============================================================



# ============================================================
# 1) QUE ES EL FLUJO DE UN PROGRAMA
# ============================================================

# Un programa normalmente se ejecuta de arriba hacia abajo.

print("Inicio del programa")
print("Paso 1")
print("Paso 2")
print("Paso 3")

# Pero muchas veces necesitamos:
# - tomar decisiones
# - repetir acciones

# Para eso existen estructuras como:
# if
# while
# for



# ============================================================
# 2) IF - TOMAR DECISIONES
# ============================================================

# Ejemplo cotidiano:
# decidir si alguien puede entrar a un boliche

edad = 20

if edad >= 18:
    print("Puedes entrar al boliche")

# El programa evalúa la condición:
# edad >= 18

# Si es VERDADERO ejecuta el código
# Si es FALSO lo salta



# ============================================================
# 3) IF / ELSE
# ============================================================

# Ejemplo cotidiano:
# decidir si alguien es menor o mayor de edad

edad = 15

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# else significa:
# "si no se cumple lo anterior"



# ============================================================
# 4) IF / ELIF / ELSE
# ============================================================

# Ejemplo cotidiano:
# calificación de un examen

nota = 85

if nota >= 90:
    print("Nota A")
elif nota >= 80:
    print("Nota B")
elif nota >= 70:
    print("Nota C")
elif nota >= 60:
    print("Nota D")
else:
    print("Nota F")

# elif significa:
# "si lo anterior no se cumplió, probar esta condición"



# ============================================================
# 5) OPERADORES DE COMPARACION
# ============================================================

# Se usan para comparar valores

a = 10
b = 5

print("a == b :", a == b)  # igual
print("a != b :", a != b)  # diferente
print("a > b :", a > b)    # mayor
print("a < b :", a < b)    # menor
print("a >= b :", a >= b)  # mayor o igual
print("a <= b :", a <= b)  # menor o igual



# ============================================================
# 6) OPERADORES LOGICOS
# ============================================================

# permiten combinar condiciones

edad = 25
tiene_entrada = True

if edad >= 18 and tiene_entrada:
    print("Puedes entrar al evento")

# and -> ambas condiciones deben ser verdaderas

if edad >= 18 or tiene_entrada:
    print("Al menos una condición es verdadera")

# or -> al menos una debe cumplirse

if not tiene_entrada:
    print("No tienes entrada")



# ============================================================
# 7) INDENTACION
# ============================================================

# Python usa espacios para definir bloques de código

numero = 15

if numero > 10:
    print("El numero es mayor que 10")

# Todo lo que esté indentado pertenece al IF



# ============================================================
# 8) BUCLE WHILE
# ============================================================

# while significa:
# "mientras esta condición sea verdadera"

contador = 0

while contador < 5:
    print("contador:", contador)
    contador += 1

# contador += 1 significa
# contador = contador + 1



# ============================================================
# 9) EJEMPLO COTIDIANO DE WHILE
# ============================================================

# simular llenar un tanque

litros = 0

while litros < 5:
    litros += 1
    print("Agregamos un litro. Total:", litros)

print("Tanque lleno")



# ============================================================
# 10) WHILE ELSE
# ============================================================

contador = 0

while contador < 3:
    print("Contador:", contador)
    contador += 1
else:
    print("El while terminó correctamente")



# ============================================================
# 11) BREAK
# ============================================================

# break sirve para salir de un bucle

for numero in range(10):

    if numero == 5:
        print("Encontramos el 5, salimos del bucle")
        break

    print(numero)



# ============================================================
# 12) CONTINUE
# ============================================================

# continue salta a la siguiente vuelta del bucle

for numero in range(10):

    if numero % 2 == 0:
        continue

    print("Número impar:", numero)



# ============================================================
# 13) PASS
# ============================================================

# pass no hace nada
# solo sirve como placeholder

for numero in range(5):

    if numero < 3:
        pass
    else:
        print("Número mayor o igual a 3:", numero)



# ============================================================
# 14) BUCLE FOR
# ============================================================

# for se usa para recorrer listas o secuencias

frutas = ["manzana", "banana", "naranja"]

for fruta in frutas:
    print("Fruta:", fruta)



# ============================================================
# 15) FOR CON STRING
# ============================================================

for letra in "Python":
    print(letra)



# ============================================================
# 16) FUNCION RANGE
# ============================================================

# range genera secuencias de numeros

for i in range(5):
    print("Numero:", i)



# ============================================================
# 17) RANGE CON INICIO Y FIN
# ============================================================

for i in range(2,7):
    print(i)



# ============================================================
# 18) RANGE CON PASO
# ============================================================

for i in range(0,10,2):
    print("Numero par:", i)



# ============================================================
# 19) RANGE INVERSO
# ============================================================

for i in range(10,0,-1):
    print("Cuenta regresiva:", i)



# ============================================================
# 20) ENUMERATE
# ============================================================

# enumerate permite obtener indice + valor

frutas = ["manzana", "banana", "pera"]

for indice, fruta in enumerate(frutas):
    print("Indice:", indice, "Fruta:", fruta)



# ============================================================
# 21) MODIFICAR LISTA CON FOR
# ============================================================

numeros = [1,2,3,4,5]

for i in range(len(numeros)):
    numeros[i] = numeros[i] * 2

print("Lista modificada:", numeros)



# ============================================================
# FIN DE LA UNIDAD
# ============================================================

print("Unidad 4 ejecutada correctamente")