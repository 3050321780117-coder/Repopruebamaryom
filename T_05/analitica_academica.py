import math
import psycopg
import matplotlib.pyplot as plt

ARCHIVO = "notas.txt"

# Conexion
try:
    conn = psycopg.connect(
        dbname="test",
        host="localhost",
        port="5432",
        user="postgres",
        password="rockyto"
    )
except Exception:
    print("Error de conexion con PostgreSQL.")
    exit()


# Validar nota
def leer_nota(mensaje):
    while True:
        try:
            nota = float(input(mensaje))

            if 0 <= nota <= 100:
                return nota

            print("La nota debe estar entre 0 y 100.")

        except ValueError:
            print("Ingrese un numero.")


while True:

    # Menu
    print("\n1. Ingreso de datos")
    print("2. Historial")
    print("3. Analitica visual")
    print("4. Salir")

    opcion = input("Opcion: ")

    # Validar menu
    if opcion not in ["1", "2", "3", "4"]:
        print("Opcion no valida.")
        continue

    # Opcion 1
    if opcion == "1":

        carnet = input("Carne: ")
        nombre = input("Nombre: ")

        tareas = leer_nota("Tareas (0-100): ")
        p1 = leer_nota("Parcial 1 (0-100): ")
        p2 = leer_nota("Parcial 2 (0-100): ")
        p3 = leer_nota("Parcial 3 (0-100): ")
        final = leer_nota("Examen final (0-100): ")

        # Calculo
        nota_exacta = (
            tareas * 0.25 +
            p1 * 0.16 +
            p2 * 0.17 +
            p3 * 0.17 +
            final * 0.25
        )

        # Redondeo
        entero = math.floor(nota_exacta)
        decimal = nota_exacta - entero

        if decimal >= 0.5:
            nota_final = entero + 1
        else:
            nota_final = entero

        # Estado
        if nota_final >= 61:
            estado = "Aprobado"
        else:
            estado = "Reprobado"

        # Resultado
        print(f"\nNota exacta: {nota_exacta:.2f}")
        print(f"Nota final: {nota_final}")
        print(f"Estado: {estado}")

        # Guardar TXT
        with open(ARCHIVO, "a", encoding="utf-8") as archivo:
            archivo.write(
                f"{carnet}|{nombre}|{tareas}|{p1}|{p2}|"
                f"{p3}|{final}|{nota_exacta:.2f}|"
                f"{nota_final}|{estado}\n"
            )

        # Guardar PostgreSQL
        try:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO notas_estudiantes
                    (carnet,nombre,tareas,p1,p2,p3,
                    examen_final,nota_exacta,nota_final,estado)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """,
                    (
                        carnet, nombre, tareas, p1, p2, p3,
                        final, nota_exacta, nota_final, estado
                    )
                )

            conn.commit()
            print("Datos guardados correctamente.")

        except Exception:
            print("Error en PostgreSQL.")
            print("Los datos quedaron en notas.txt.")
            conn.close()
            break

    # Opcion 2
    elif opcion == "2":

        print("\n--- HISTORIAL ---")

        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT carnet,nombre,nota_final,estado
                FROM notas_estudiantes
                ORDER BY id
                """
            )

            datos = cur.fetchall()

        if not datos:
            print("No hay registros.")
        else:
            print(
                f"{'CARNE':<15}"
                f"{'NOMBRE':<25}"
                f"{'NOTA':<10}"
                f"{'ESTADO':<15}"
            )

            for fila in datos:
                print(
                    f"{fila[0]:<15}"
                    f"{fila[1]:<25}"
                    f"{fila[2]:<10}"
                    f"{fila[3]:<15}"
                )

    # Opcion 3
    elif opcion == "3":

        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT nombre,tareas,p1,p2,p3,
                examen_final,nota_final,estado
                FROM notas_estudiantes
                ORDER BY id
                """
            )

            datos = cur.fetchall()

        if not datos:
            print("No hay datos para graficar.")
            continue

        # Extraer datos
        nombres = [x[0] for x in datos]
        tareas = [float(x[1]) for x in datos]
        p1 = [float(x[2]) for x in datos]
        p2 = [float(x[3]) for x in datos]
        p3 = [float(x[4]) for x in datos]
        finales = [float(x[5]) for x in datos]
        notas = [int(x[6]) for x in datos]
        estados = [x[7] for x in datos]

        # Grafica 1
        plt.figure()
        plt.bar(nombres, notas)
        plt.title("Rendimiento individual")
        plt.xlabel("Estudiantes")
        plt.ylabel("Nota final")
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Grafica 2
        aprobados = estados.count("Aprobado")
        reprobados = estados.count("Reprobado")

        plt.figure()
        plt.pie(
            [aprobados, reprobados],
            labels=["Aprobados", "Reprobados"],
            autopct="%1.1f%%"
        )
        plt.title("Indice de aprobacion")

        # Grafica 3
        promedios = [
            sum(tareas) / len(tareas),
            sum(p1) / len(p1),
            sum(p2) / len(p2),
            sum(p3) / len(p3),
            sum(finales) / len(finales)
        ]

        plt.figure()
        plt.bar(
            ["Tareas", "P1", "P2", "P3", "Final"],
            promedios
        )
        plt.title("Desempeno por rubro")
        plt.ylabel("Promedio")
        plt.tight_layout()

        plt.show()

    # Salir
    elif opcion == "4":
        print("Saliendo...")
        break


conn.close()
