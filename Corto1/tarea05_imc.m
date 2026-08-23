# =========================================================
# TAREA 05 - CALCULO DEL IMC
# SIN FUNCIONES
# =========================================================

pkg load database

# Conexion con PostgreSQL
conn = pq_connect(setdbopts( ...
    'dbname','test', ...
    'host','localhost', ...
    'port','5432', ...
    'user','postgres', ...
    'password','rockyto'));

opcion = 0;

while opcion ~= 4

    clc;

    disp('==============================');
    disp('       CALCULO DEL IMC');
    disp('==============================');
    disp('1. Calcular y guardar IMC');
    disp('2. Leer informacion');
    disp('3. Borrar informacion');
    disp('4. Salir');

    opcion = input('Ingrese una opcion: ');

    if opcion < 1 || opcion > 4
        disp('Opcion no valida.');
        pause;
        continue;
    endif


    # =====================================================
    # OPCION 1 - CALCULAR Y GUARDAR
    # =====================================================

    if opcion == 1

        nombre = input('Ingrese su nombre: ', 's');
        peso = input('Ingrese su peso en kg: ');
        altura = input('Ingrese su altura en metros: ');

        # Calculo del IMC
        imc = peso / (altura ^ 2);

        # Clasificacion
        if imc < 18.5
            categoria = 'Bajo peso';

        elseif imc < 25
            categoria = 'Peso normal';

        else
            categoria = 'Sobrepeso';

        endif

        disp(' ');
        disp(['Nombre: ', nombre]);
        disp(['IMC: ', num2str(imc, '%.2f')]);
        disp(['Categoria: ', categoria]);


        # -------------------------------------------------
        # GUARDAR EN ARCHIVO TXT
        # -------------------------------------------------

        archivo = fopen('imc.txt', 'a');

        fprintf(archivo, 'Nombre: %s\n', nombre);
        fprintf(archivo, 'Peso: %.2f kg\n', peso);
        fprintf(archivo, 'Altura: %.2f m\n', altura);
        fprintf(archivo, 'IMC: %.2f\n', imc);
        fprintf(archivo, 'Categoria: %s\n', categoria);
        fprintf(archivo, '-----------------------------\n');

        fclose(archivo);

        disp('Informacion guardada en imc.txt');


        # -------------------------------------------------
        # GUARDAR EN POSTGRESQL
        # -------------------------------------------------

        consulta = sprintf( ...
            "INSERT INTO imc_registros VALUES ('%s', %.2f, %.2f, %.2f, '%s');", ...
            nombre, peso, altura, imc, categoria);

        pq_exec_params(conn, consulta);

        disp('Informacion guardada en PostgreSQL.');

        pause;


    # =====================================================
    # OPCION 2 - LEER
    # =====================================================

    elseif opcion == 2

        disp(' ');
        disp('===== INFORMACION LOCAL =====');

        if exist('imc.txt', 'file')

            archivo = fopen('imc.txt', 'r');

            while ~feof(archivo)
                linea = fgetl(archivo);

                if ischar(linea)
                    disp(linea);
                endif
            endwhile

            fclose(archivo);

        else
            disp('No existe informacion guardada.');
        endif


        disp(' ');
        disp('===== INFORMACION POSTGRESQL =====');

        datos = pq_exec_params(
            conn,
            "SELECT * FROM imc_registros;"
        );

        disp(datos.data);

        pause;


    # =====================================================
    # OPCION 3 - BORRAR
    # =====================================================

    elseif opcion == 3

        # Borrar archivo local
        if exist('imc.txt', 'file')
            delete('imc.txt');
            disp('Archivo imc.txt eliminado.');
        else
            disp('No existe archivo local.');
        endif

        # Borrar datos de PostgreSQL
        pq_exec_params(
            conn,
            "DELETE FROM imc_registros;"
        );

        disp('Registros eliminados de PostgreSQL.');

        pause;


    # =====================================================
    # OPCION 4 - SALIR
    # =====================================================

    elseif opcion == 4

        disp('Gracias por usar el programa.');

    endif

endwhile

pq_close(conn);



