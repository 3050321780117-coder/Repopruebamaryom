# =========================================================
# TAREA 02 - FUNCIONES Y GRAFICAS
# =========================================================


# =========================================================
# 1. FUNCION HIPOTENUSA
# =========================================================

# Para esta funcion se recomienda crear otro archivo
# llamado hipotenusa.m

# Ejemplo de uso:
a = 3;
b = 4;

hipo = hipotenusa(a, b);

disp("Hipotenusa:")
disp(hipo)


# =========================================================
# 2. FUNCION CON DOS VALORES DE SALIDA
# =========================================================

# Esta variante devuelve la hipotenusa y el cuadrado de a

[hipo, a_cuadrada] = hipotenusa_doble(a, b);

disp("Hipotenusa:")
disp(hipo)

disp("a al cuadrado:")
disp(a_cuadrada)


# =========================================================
# 3. FUNCION POLINOMICA
# =========================================================

# Crear varios valores de x
x = -3:0.1:1;

# Evaluar y graficar la funcion
y = funcion(x);

figure;
plot(x, y);

title("Funcion");
xlabel("Eje X");
ylabel("Eje Y");


# =========================================================
# 4. USO DE LINSPACE
# =========================================================

# Genera 50 valores entre -3 y 1
x = linspace(-3, 1, 50);

y = funcion(x);

figure;
plot(x, y);

title("Funcion con linspace");
xlabel("Eje X");
ylabel("Eje Y");


# =========================================================
# 5. GRAFICA COLOR ROJO
# =========================================================

x = linspace(-3, 1, 50);

figure;
plot(x, funcion(x), "Color", "red");

title("Funcion color rojo");
xlabel("Eje X");
ylabel("Eje Y");


# =========================================================
# 6. GRAFICA COLOR VERDE
# =========================================================

figure;
plot(x, funcion(x), "Color", "green");

title("Funcion color verde");
xlabel("Eje X");
ylabel("Eje Y");


# =========================================================
# 7. LINEA CONTINUA
# =========================================================

figure;
plot(x, funcion(x), "LineStyle", "-");

title("Linea continua");
xlabel("Eje X");
ylabel("Eje Y");


# =========================================================
# 8. LINEA DISCONTINUA
# =========================================================

figure;
plot(x, funcion(x), "LineStyle", "--");

title("Linea discontinua");
xlabel("Eje X");
ylabel("Eje Y");


# =========================================================
# 9. LINEA DE PUNTOS
# =========================================================

figure;
plot(x, funcion(x), "LineStyle", ":");

title("Linea de puntos");
xlabel("Eje X");
ylabel("Eje Y");


# =========================================================
# 10. LINEA PUNTO-GUION
# =========================================================

figure;
plot(x, funcion(x), "LineStyle", "-.");

title("Linea punto-guion");
xlabel("Eje X");
ylabel("Eje Y");


# =============================================
# 11. GRAFICA STEM
# =============================================

x = linspace(-3, 1, 50);

y = funcion(x);

figure;

stem(x, y);

title("Titulo");
xlabel("Eje X");
ylabel("Eje Y");


# =========================================================
# 12. GRAFICA CON TITULO, EJES Y LEYENDA
# =========================================================

figure;

plot(
    x,
    funcion(x),
    "LineStyle", ":"
);

title("Titulo");
ylabel("Eje Y");
xlabel("Eje X");
legend("Funcion");


# =========================================================
# 13. GRAFICA SENO Y COSENO
# =========================================================

x = 0:0.1:4*pi;

y1 = sin(x);
y2 = cos(x);

figure;

hold on;

p1 = plot(x, y1);
p2 = plot(x, y2);

set(
    p1,
    "Color", "red",
    "LineWidth", 2
);

set(
    p2,
    "Color", "blue",
    "LineWidth", 1
);

ylabel("EJE Y");
xlabel("Eje X");

title("Seno y Coseno");

legend("Seno", "Coseno");

hold off;


