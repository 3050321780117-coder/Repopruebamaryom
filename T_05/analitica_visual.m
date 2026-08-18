function analitica_visual(conn)

    clc;

    disp('==========================================');
    disp('          ANALITICA VISUAL');
    disp('==========================================');

    datos = pq_exec_params(conn, ...
        ["SELECT nombre,tareas,p1,p2,p3,examen_final," ...
         "nota_final,estado " ...
         "FROM notas_estudiantes ORDER BY id;"]);

    if isempty(datos.data)

        disp('No hay datos para generar graficas.');
        return;

    endif

    cantidad = rows(datos.data);

    nombres = cell(cantidad,1);
    tareas = zeros(cantidad,1);
    p1 = zeros(cantidad,1);
    p2 = zeros(cantidad,1);
    p3 = zeros(cantidad,1);
    finales = zeros(cantidad,1);
    notas = zeros(cantidad,1);
    estados = cell(cantidad,1);


    % Obtener datos
    for i = 1:cantidad

        nombres{i} = datos.data{i,1};
        tareas(i) = datos.data{i,2};
        p1(i) = datos.data{i,3};
        p2(i) = datos.data{i,4};
        p3(i) = datos.data{i,5};
        finales(i) = datos.data{i,6};
        notas(i) = datos.data{i,7};
        estados{i} = datos.data{i,8};

    endfor


    % Grafica 1
    figure(1);
    clf;

    bar(notas);

    title('Rendimiento Individual');
    xlabel('Estudiantes');
    ylabel('Nota Final');

    set(gca, ...
        'xtick', 1:cantidad, ...
        'xticklabel', nombres);

    grid on;


    % Grafica 2
    aprobados = sum(strcmp(estados, 'Aprobado'));
    reprobados = sum(strcmp(estados, 'Reprobado'));

    figure(2);
    clf;

    pie([aprobados, reprobados]);

    legend('Aprobados', 'Reprobados');

    title('Indice de Aprobacion');


    % Grafica 3
    promedios = [ ...
        mean(tareas), ...
        mean(p1), ...
        mean(p2), ...
        mean(p3), ...
        mean(finales)];

    figure(3);
    clf;

    bar(promedios);

    title('Desempeno por Rubro');
    ylabel('Promedio');

    set(gca, ...
        'xtick', 1:5, ...
        'xticklabel', ...
        {'Tareas','P1','P2','P3','Final'});

    grid on;

    disp('Graficas generadas correctamente.');

endfunction
