clc;
clear;
pkg load database

% Configuracion
dbname = 'test';
host = 'localhost';
port = '5432';
usuario = 'postgres';
password = 'rockyto';
archivo_txt = 'notas.txt';

% Conexion PostgreSQL
try
    conn = pq_connect(setdbopts( ...
        'dbname', dbname, ...
        'host', host, ...
        'port', port, ...
        'user', usuario, ...
        'password', password));

    conexion_activa = true;

catch
    disp('Error de conexion con PostgreSQL.');
    disp('Programa finalizado de manera segura.');
    return;
end_try_catch


while true

    clc;

    disp('==========================================');
    disp('   SISTEMA DE ANALITICA ACADEMICA');
    disp('==========================================');
    disp('1. Ingreso de datos');
    disp('2. Historial');
    disp('3. Analitica visual');
    disp('4. Salir');

    opcion = str2double(input('Opcion: ', 's'));

    % Validar menu
    if isnan(opcion) || opcion < 1 || opcion > 4

        disp('Opcion no valida.');
        pause;
        continue;

    endif


    % Opcion 1
    if opcion == 1

        clc;

        disp('--- INGRESO DE DATOS ---');

        carnet = input('Carne: ', 's');
        nombre = input('Nombre: ', 's');

        tareas = leer_nota('Tareas (0-100): ');
        p1 = leer_nota('Parcial 1 (0-100): ');
        p2 = leer_nota('Parcial 2 (0-100): ');
        p3 = leer_nota('Parcial 3 (0-100): ');
        examen_final = leer_nota('Examen final (0-100): ');

        % Calculo
        nota_exacta = calcular_nota( ...
            tareas, p1, p2, p3, examen_final);

        % Redondeo
        nota_final = redondear_nota(nota_exacta);

        % Estado
        estado = determinar_estado(nota_final);

        % Resultado
        fprintf('\nNota exacta: %.2f\n', nota_exacta);
        fprintf('Nota final: %d\n', nota_final);
        fprintf('Estado: %s\n', estado);

        % Guardar primero en TXT
        guardar_txt( ...
            archivo_txt, carnet, nombre, ...
            tareas, p1, p2, p3, examen_final, ...
            nota_exacta, nota_final, estado);

        % Guardar PostgreSQL
        try

            guardar_postgresql( ...
                conn, carnet, nombre, ...
                tareas, p1, p2, p3, examen_final, ...
                nota_exacta, nota_final, estado);

            disp('Datos guardados correctamente.');

        catch

            disp('Error al guardar en PostgreSQL.');
            disp('Los datos permanecen en notas.txt.');

            pq_close(conn);
            return;

        end_try_catch

        pause;


    % Opcion 2
    elseif opcion == 2

        mostrar_historial(conn, archivo_txt);
        pause;


    % Opcion 3
    elseif opcion == 3

        analitica_visual(conn);
        pause;


    % Opcion 4
    elseif opcion == 4

        disp('Gracias por utilizar el programa.');
        break;

    endif

endwhile


if conexion_activa
    pq_close(conn);
endif

disp('Programa finalizado.');


