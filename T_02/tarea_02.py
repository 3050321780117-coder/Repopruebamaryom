# TAREA 02
# PROYECTOS DE COMPUTACION APLICADA A I.E.
# EQUIVALENTES EN PYTHON

import numpy as np


# =============================================
# OBJETOS NUMERICOS
# =============================================

print(375)
print(3.75e2)
print(3.75E2)
print(0x177)


# =============================================
# SECUENCIAS
# =============================================

# Secuencia desde 1 hasta 10
print(list(range(1, 11)))

# Secuencia con salto decimal
print(np.arange(1, 10, 1.6))


# =============================================
# MATRICES BASICAS
# =============================================

# Matriz de 3 filas y 3 columnas
M = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(M)

# Matriz equivalente a [1:4;5:8] de Octave
M = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

print(M)


# =============================================
# CADENAS
# =============================================

print("Cadena de string")
print("A")


# =============================================
# ESTRUCTURAS
# =============================================

# En Python utilizamos un diccionario
x = {}

# Secuencia
x["secuencia"] = [1, 2, 3, 4, 5]

# Matriz
x["matriz"] = [
    [1, 2],
    [44, 5]
]

# Cadena
x["string"] = "Secuencia"

# Diccionario interno
x["estructura"] = {}

# Numero hexadecimal
x["estructura"]["numero"] = 0x177

# Caracter
x["estructura"]["letra"] = "A"

# Mostrar estructura
print(x)


# =============================================
# OPERADORES ARITMETICOS
# =============================================

x = 2
y = 3

# Suma
print(x + y)

# Resta
print(x - y)

# Multiplicacion
print(x * y)

# Division
print(x / y)

# Incremento
x += 1
print(x)

# Decremento
x -= 1
print(x)


# =============================================
# OPERADORES RELACIONALES
# =============================================

x = 2
y = 3

print(x < y)
print(x <= y)
print(x == y)
print(x > y)
print(x >= y)
print(x != y)


# =============================================
# OPERADORES LOGICOS
# =============================================

x = True
y = False

# AND
print(x and y)

# OR
print(x or y)

# NOT
print(not x)


# =============================================
# ESTRUCTURA CONDICIONAL IF
# =============================================

x = 1
y = 0

if x > y:

    print("x es mayor a y")

elif x == y:

    print("x y y son iguales")

else:

    print("y es mayor a x")


# =============================================
# CONDICION COMPUESTA
# =============================================

x = 1
y = 0
z = -5

if x > y and z < 0:

    print("x es mayor a y y z es menor a 0")

elif x == y or z < 0:

    print("x y y son iguales")

else:

    print("y es mayor a x")


# =============================================
# CICLO WHILE
# =============================================

x = 1
y = 0
z = -5

while z < y:

    print("Valor de z:", z)

    z += 1


# =============================================
# CICLO FOR - FIBONACCI
# =============================================

# Vector de 10 elementos
fib = [1] * 10

# Python comienza los indices desde cero,
# por eso se inicia en la posicion 2
for i in range(2, 10):

    fib[i] = fib[i - 1] + fib[i - 2]

# Mostrar sucesion
print(fib)


# =============================================
# MANEJO DE ERRORES
# =============================================

try:

    fila1 = list(range(1, 6))
    fila2 = list(range(10, 16))

    # Verificar que tengan el mismo tamaño
    if len(fila1) != len(fila2):

        raise ValueError("Las filas tienen dimensiones diferentes")

except ValueError:

    print(
        "NO SE PUDO EJECUTAR, "
        "se continua con la ejecucion normal"
    )


# =============================================
# OPERACIONES CON MATRICES
# =============================================

M = np.array([
    [1, 2],
    [4, 5]
])

N = np.array([
    [0, 1],
    [8, 10]
])


# Suma de matrices
suma = M + N

print("Suma:")
print(suma)


# Resta de matrices
resta = M - N

print("Resta:")
print(resta)


# Multiplicacion matricial
producto = M @ N

print("Multiplicacion:")
print(producto)


# Producto elemento a elemento y suma
producto_punto = np.sum(M * N)

print("Producto punto:")
print(producto_punto)


# Transpuesta
transpuesta = M.T

print("Transpuesta:")
print(transpuesta)
