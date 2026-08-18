function estado = determinar_estado(nota_final)

    if nota_final >= 61

        estado = 'Aprobado';

    else

        estado = 'Reprobado';

    endif

endfunction
