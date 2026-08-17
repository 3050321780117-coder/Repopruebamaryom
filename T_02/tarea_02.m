# TAREA 02
# PROYECTOS DE COMPUTACION APLICADA A I.E.
# EJEMPLOS EN GNU OCTAVE


# =============================================
# OBJETOS NUMERICOS
# =============================================

375
3.75e2
3.75E2
0x177


# =============================================
# SECUENCIAS
# =============================================

# Secuencia de 1 hasta 10
1:10

# Secuencia iniciando en 1 con salto de 1.6
1:1.6:10


# =============================================
# MATRICES BASICAS
# =============================================

# Matriz de 3 filas y 3 columnas
M = [1,2,3;4,5,6;7,8,9]

# Matriz creada mediante secuencias
M = [1:4;5:8]


# =============================================
# CADENAS
# =============================================

'Cadena de string'
'A'


# =============================================
# ESTRUCTURAS
# =============================================

# Se crea una estructura para guardar
# diferentes tipos de información
x = struct()

# Secuencia dentro de la estructura
x.secuencia = 1:5

# Matriz dentro de la estructura
x.matriz = [1,2;44,5]

# Cadena de texto
x.string = 'Secuencia'

# Estructura interna
x.estructura = struct()

# Numero hexadecimal
x.estructura.numero = 0x177

# Caracter
x.estructura.letra = 'A'

# Mostrar estructura completa
x


# =============================================
# OPERADORES ARITMETICOS
# =============================================

x = 2
y = 3

# Suma
x + y

# Resta
x - y

# Multiplicacion
x * y

# Division
x / y

# Incremento
++x

# Decremento
--x


# =============================================
# OPERADORES RELACIONALES
# =============================================

x = 2
y = 3

# Menor que
x < y

# Menor o igual
x <= y

# Igual
x == y

# Mayor que
x > y

# Mayor o igual
x >= y

# Diferente
x != y


# =============================================
# OPERADORES LOGICOS
# =============================================

x = 1
y = 0

# AND
x & y

# OR
x | y

# NOT
not(x)


# =============================================
# ESTRUCTURA CONDICIONAL IF
# =============================================

x = 1
y = 0

if (x > y)

    disp('x es mayor a y')

elseif (x == y)

    disp('x y y son iguales')

else

    disp('y es mayor a x')

endif


# =============================================
# CONDICION COMPUESTA
# =============================================

x = 1
y = 0
z = -5

if (x > y & z < 0)

    disp('x es mayor a y y z es menor a 0')

elseif (x == y | z < 0)

    disp('x y y son iguales')

else

    disp('y es mayor a x')

endif


# =============================================
# CICLO WHILE
# =============================================

x = 1
y = 0
z = -5

while (z < y)

    disp('Valor de z:')
    z

    ++z

endwhile


# =============================================
# CICLO FOR - FIBONACCI
# =============================================

# Se crea un vector de 10 posiciones
# inicialmente lleno de unos
fib = ones(1,10)

# Desde la tercera posicion se calcula
# cada numero utilizando los dos anteriores
for i = 3:10

    fib(i) = fib(i-1) + fib(i-2);

endfor

# Mostrar sucesion
fib


# =============================================
# MANEJO DE ERRORES
# =============================================

try

    # Estas filas tienen diferente cantidad
    # de elementos y provocan un error
    m = [1:5;10:15]

catch

    disp('NO SE PUDO EJECUTAR, se continua con la ejecucion normal')

end_try_catch


# =============================================
# OPERACIONES CON MATRICES
# =============================================

M = [1,2;4,5]
N = [0,1;8,10]

# Suma
suma = M + N

# Resta
resta = M - N

# Multiplicacion matricial
producto = M * N

# Producto punto
producto_punto = dot(M,N)

# Transpuesta de M
transpuesta = M'



