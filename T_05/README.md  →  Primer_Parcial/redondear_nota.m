function nota_final = redondear_nota(nota_exacta)

    entero = floor(nota_exacta);
    decimal = nota_exacta - entero;

    if decimal >= 0.5

        nota_final = entero + 1;

    else

        nota_final = entero;

    endif

endfunction


