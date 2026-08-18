function mostrar_historial(conn, archivo_txt)

    clc;

    disp('==========================================');
    disp('              HISTORIAL');
    disp('==========================================');

    try

        datos = pq_exec_params(conn, ...
            ["SELECT carnet,nombre,nota_final,estado " ...
             "FROM notas_estudiantes ORDER BY id;"]);

        if isempty(datos.data)

            disp('No hay estudiantes registrados.');

        else

            fprintf('\n%-15s %-25s %-10s %-15s\n', ...
                'CARNE', 'NOMBRE', 'NOTA', 'ESTADO');

            disp('--------------------------------------------------------------');

            for i = 1:rows(datos.data)

                fprintf('%-15s %-25s %-10.0f %-15s\n', ...
                    datos.data{i,1}, ...
                    datos.data{i,2}, ...
                    datos.data{i,3}, ...
                    datos.data{i,4});

            endfor

        endif

    catch

        disp('Error al consultar PostgreSQL.');
        disp('Mostrando notas.txt.');

        if exist(archivo_txt, 'file')

            archivo = fopen(archivo_txt, 'r');

            while ~feof(archivo)

                linea = fgetl(archivo);

                if ischar(linea)
                    disp(linea);
                endif

            endwhile

            fclose(archivo);

        else

            disp('No existe notas.txt.');

        endif

    end_try_catch

endfunction

