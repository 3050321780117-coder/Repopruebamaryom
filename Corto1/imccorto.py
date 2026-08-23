import os
import psycopg


# Configuracion PostgreSQL
try:

    conn = psycopg.connect(
        dbname="test",
        host="localhost",
        port="5432",
        user="postgres",
        password="rockyto"
    )

    print("Conexion con PostgreSQL exitosa.")

except Exception:

    print("Error de conexion con PostgreSQL.")
    print("Programa finalizado.")

    exit()

while True:

    # Menu
    print("\n==============================")
    print("       CALCULO DEL IMC")
    print("==============================")
    print("1. Calcular y guardar IMC")
    print("2. Leer informacion")
    print("3. Borrar informacion")
    print("4. Salir")
    print("==============================")


    opcion = input("Ingrese una opcion: ")


    # Validar opcion
    if opcion not in ["1", "2", "3", "4"]:

        print("Opcion no valida.")
        continue

    # ==========================================
    # OPCION 1
    # ==========================================

    if opcion == "1":

        print("\n--- CALCULAR IMC ---")

        nombre = input("Nombre: ")


        # Validar peso
        while True:

            try:

                peso = float(
                    input("Peso en kg: ")
                )

                if peso > 0:
                    break

                print("El peso debe ser mayor que cero.")

            except ValueError:

                print("Ingrese un numero valido.")


        # Validar altura
        while True:

            try:

                altura = float(
                    input("Altura en metros: ")
                )

                if altura > 0:
                    break

                print("La altura debe ser mayor que cero.")

            except ValueError:

                print("Ingrese un numero valido.")


        # Calcular IMC
        imc = peso / (altura ** 2)


        # Clasificar IMC
        if imc < 18.5:

            categoria = "Bajo peso"

        elif imc < 25:

            categoria = "Peso normal"

        else:

            categoria = "Sobrepeso"


        # Mostrar resultado
        print("\n--- RESULTADO ---")

        print(f"Nombre: {nombre}")
        print(f"Peso: {peso:.2f} kg")
        print(f"Altura: {altura:.2f} m")
        print(f"IMC: {imc:.2f}")
        print(f"Categoria: {categoria}")


        # Guardar primero en imc.txt
        with open(
            "imc.txt",
            "a",
            encoding="utf-8"
        ) as archivo:

            archivo.write(
                f"Nombre: {nombre} | "
                f"Peso: {peso:.2f} | "
                f"Altura: {altura:.2f} | "
                f"IMC: {imc:.2f} | "
                f"Categoria: {categoria}\n"
            )


        # Guardar en PostgreSQL
        try:

            with conn.cursor() as cursor:

                cursor.execute(
                    """
                    INSERT INTO imc_registros
                    (nombre, peso, altura, imc, categoria)
                    VALUES (%s, %s, %s, %s, %s);
                    """,
                    (
                        nombre,
                        peso,
                        altura,
                        imc,
                        categoria
                    )
                )

            conn.commit()

            print(
                "Informacion guardada en "
                "imc.txt y PostgreSQL."
            )


        except Exception as error:

            print(
                "Error al guardar en PostgreSQL."
            )

            print(
                "La informacion permanece "
                "guardada en imc.txt."
            )

            print(error)


    # ==========================================
    # OPCION 2
    # ==========================================

    elif opcion == "2":

        print("\n--- INFORMACION GUARDADA ---")


        # Leer archivo de texto
        print("\nARCHIVO imc.txt:")

        if os.path.exists("imc.txt"):

            with open(
                "imc.txt",
                "r",
                encoding="utf-8"
            ) as archivo:

                for linea in archivo:

                    print(
                        linea.strip()
                    )

        else:

            print(
                "No existe informacion "
                "en imc.txt."
            )


        # Leer PostgreSQL
        print("\nPOSTGRESQL:")

        try:

            with conn.cursor() as cursor:

                cursor.execute(
                    """
                    SELECT
                        nombre,
                        peso,
                        altura,
                        imc,
                        categoria
                    FROM imc_registros;
                    """
                )

                registros = cursor.fetchall()


            if not registros:

                print(
                    "No hay registros "
                    "en PostgreSQL."
                )


            else:

                print(
                    f"{'NOMBRE':<20}"
                    f"{'PESO':<10}"
                    f"{'ALTURA':<10}"
                    f"{'IMC':<10}"
                    f"{'CATEGORIA':<20}"
                )

                print("-" * 70)


                for registro in registros:

                    print(
                        f"{registro[0]:<20}"
                        f"{registro[1]:<10.2f}"
                        f"{registro[2]:<10.2f}"
                        f"{registro[3]:<10.2f}"
                        f"{registro[4]:<20}"
                    )


        except Exception as error:

            print(
                "Error al consultar PostgreSQL."
            )

            print(error)

    # ==========================================
    # OPCION 3
    # ==========================================

    elif opcion == "3":

        print("\n--- BORRAR INFORMACION ---")


        # Borrar imc.txt
        if os.path.exists("imc.txt"):

            os.remove("imc.txt")

            print(
                "Archivo imc.txt eliminado."
            )

        else:

            print(
                "No existe imc.txt."
            )


        # Borrar PostgreSQL
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    DELETE FROM imc_registros;
                    """
                )

            conn.commit()
            print(
                "Registros de PostgreSQL "
                "eliminados."
            )

        except Exception as error:

            print(
                "Error al borrar registros "
                "de PostgreSQL."
            )

            print(error)
    # ==========================================
    # OPCION 4
    # ==========================================

    elif opcion == "4":

        print(
            "Gracias por usar el programa."
        )

        break
# Cerrar PostgreSQL
conn.close()

print("Programa finalizado.")
