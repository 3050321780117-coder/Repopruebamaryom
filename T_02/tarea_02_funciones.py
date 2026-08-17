# =========================================================
# TAREA 02 - FUNCIONES Y GRAFICAS
# PYTHON
# =========================================================

import numpy as np
import matplotlib.pyplot as plt


# =========================================================
# 1. FUNCION HIPOTENUSA
# =========================================================

def hipotenusa(a, b):

    hipo = np.sqrt(a**2 + b**2)

    return hipo


a = 3
b = 4

resultado = hipotenusa(a, b)

print("Hipotenusa:")
print(resultado)


# =========================================================
# 2. FUNCION CON DOS VALORES DE SALIDA
# =========================================================

def hipotenusa_doble(a, b):

    hipo = np.sqrt(a**2 + b**2)

    a_cuadrada = a**2

    return hipo, a_cuadrada


hipo, a_cuadrada = hipotenusa_doble(a, b)

print("Hipotenusa:")
print(hipo)

print("a al cuadrado:")
print(a_cuadrada)


# =========================================================
# 3. FUNCION POLINOMICA
# =========================================================

def funcion(x):

    return 4*x**3 + 10*x**2 + 6


x = np.arange(-3, 1.1, 0.1)

y = funcion(x)

plt.figure()

plt.plot(x, y)

plt.title("Funcion")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

plt.show()


# =========================================================
# 4. USO DE LINSPACE
# =========================================================

x = np.linspace(-3, 1, 50)

y = funcion(x)

plt.figure()

plt.plot(x, y)

plt.title("Funcion con linspace")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

plt.show()


# =========================================================
# 5. GRAFICA COLOR ROJO
# =========================================================

plt.figure()

plt.plot(
    x,
    funcion(x),
    color="red"
)

plt.title("Funcion color rojo")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

plt.show()


# =========================================================
# 6. GRAFICA COLOR VERDE
# =========================================================

plt.figure()

plt.plot(
    x,
    funcion(x),
    color="green"
)

plt.title("Funcion color verde")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

plt.show()


# =========================================================
# 7. LINEA CONTINUA
# =========================================================

plt.figure()

plt.plot(
    x,
    funcion(x),
    linestyle="-"
)

plt.title("Linea continua")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

plt.show()


# =========================================================
# 8. LINEA DISCONTINUA
# =========================================================

plt.figure()

plt.plot(
    x,
    funcion(x),
    linestyle="--"
)

plt.title("Linea discontinua")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

plt.show()


# =========================================================
# 9. LINEA DE PUNTOS
# =========================================================

plt.figure()

plt.plot(
    x,
    funcion(x),
    linestyle=":"
)

plt.title("Linea de puntos")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

plt.show()


# =========================================================
# 10. LINEA PUNTO-GUION
# =========================================================

plt.figure()

plt.plot(
    x,
    funcion(x),
    linestyle="-."
)

plt.title("Linea punto-guion")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

plt.show()


# =============================================
# GRAFICA STEM
# =============================================

x = np.linspace(-3, 1, 50)

y = funcion(x)

plt.figure()

plt.stem(x, y)

plt.title("Titulo")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

plt.show()


# =========================================================
# 11. TITULO, EJES Y LEYENDA
# =========================================================

plt.figure()

plt.plot(
    x,
    funcion(x),
    linestyle=":",
    label="Funcion"
)

plt.title("Titulo")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

plt.legend()

plt.show()


# =========================================================
# 12. SENO Y COSENO
# =========================================================

x = np.arange(
    0,
    4 * np.pi,
    0.1
)

y1 = np.sin(x)
y2 = np.cos(x)

plt.figure()

plt.plot(
    x,
    y1,
    color="red",
    linewidth=2,
    label="Seno"
)

plt.plot(
    x,
    y2,
    color="blue",
    linewidth=1,
    label="Coseno"
)

plt.xlabel("Eje X")
plt.ylabel("EJE Y")

plt.title("Seno y Coseno")

plt.legend()

plt.show()
