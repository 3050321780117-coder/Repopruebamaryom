function nota = leer_nota(mensaje)

    while true

        entrada = input(mensaje, 's');
        nota = str2double(entrada);

        if isnan(nota)

            disp('Error: ingrese un numero.');

        elseif nota < 0 || nota > 100

            disp('Error: la nota debe estar entre 0 y 100.');

        else

            break;

        endif

    endwhile

endfunction

