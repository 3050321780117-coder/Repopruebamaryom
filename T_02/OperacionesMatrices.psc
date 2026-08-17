Proceso OperacionesMatrices
	
    Definir i, j, k Como Entero
    Dimension M[2,2]
    Dimension N[2,2]
    Dimension Suma[2,2]
    Dimension Resta[2,2]
    Dimension Producto[2,2]
	
    M[1,1] = 1
    M[1,2] = 2
    M[2,1] = 4
    M[2,2] = 5
	
    N[1,1] = 0
    N[1,2] = 1
    N[2,1] = 8
    N[2,2] = 10
	
    Para i = 1 Hasta 2 Hacer
        Para j = 1 Hasta 2 Hacer
			
            Suma[i,j] = M[i,j] + N[i,j]
            Resta[i,j] = M[i,j] - N[i,j]
			
        FinPara
    FinPara
	
    Para i = 1 Hasta 2 Hacer
        Para j = 1 Hasta 2 Hacer
			
            Producto[i,j] = 0
			
            Para k = 1 Hasta 2 Hacer
                Producto[i,j] = Producto[i,j] + M[i,k] * N[k,j]
            FinPara
			
        FinPara
    FinPara
	
    Escribir "Matriz suma"
	
    Para i = 1 Hasta 2 Hacer
        Escribir Suma[i,1], "  ", Suma[i,2]
    FinPara
	
    Escribir "Matriz resta"
	
    Para i = 1 Hasta 2 Hacer
        Escribir Resta[i,1], "  ", Resta[i,2]
    FinPara
	
    Escribir "Matriz producto"
	
    Para i = 1 Hasta 2 Hacer
        Escribir Producto[i,1], "  ", Producto[i,2]
    FinPara
	
FinProceso

