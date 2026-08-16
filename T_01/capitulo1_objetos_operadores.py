# ==========================================
# CAPITULO 1 - OBJETOS NUMERICOS Y OPERADORES
# SU CODIGO EN PYTHON
# ==========================================

import numpy as np


# ==========================================
# OBJETOS NUMERICOS
# ==========================================

print(375)
print(3.75e2)
print(3.75E2)
print(0x17)


# ==========================================
# SECUENCIAS
# ==========================================

print(list(range(1, 11)))

secuencia = np.arange(1, 10, 1.6)
print(secuencia)


# ==========================================
# MATRICES
# ==========================================

M = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(M)

M = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

print(M)


# ==========================================
# CADENAS
# ==========================================

print("Cadena de string")
print("A")


# ==========================================
# ESTRUCTURAS
# ==========================================

x = {}

x["secuencia"] = [1, 2, 3, 4, 5]

x["matriz"] = [
    [1, 2],
    [44, 5]
]

x["string"] = "Secuencia"

x["estructura"] = {}

x["estructura"]["numero"] = 0x177
x["estructura"]["letra"] = "A"

print(x)


# ==========================================
# OPERADORES ARITMETICOS
# ==========================================

x = 2
y = 3

print(x + y)
print(x - y)
print(x * y)
print(x / y)

x += 1
print(x)

x -= 1
print(x)


# ==========================================
# OPERADORES RELACIONALES
# ==========================================

x = 2
y = 3

print(x < y)
print(x <= y)
print(x == y)
print(x > y)
print(x >= y)
print(x != y)


# ==========================================
# OPERADORES LOGICOS
# ==========================================

x = True
y = False

print(x and y)
print(x or y)
print(not x)

