

def inicializar_matriz(cant_filas:int, cant_columnas:int, valor_inicial:int|str)->list[list]:
    """Inicializa una matriz con valores definidos por parametro

    Args:
        cant_filas (int): cantidad de filas para crear la matriz
        cant_columnas (int): cantidad de columnas para crear la matriz
        valor_inicial (int)|(str): valor que va a tener cada elemento de la matriz

    Returns:
        list: retorna una matriz de la cantidad de filas y columnas definidas
    """
    matriz = []
    for _ in range(cant_filas):
        fila = [valor_inicial] * cant_columnas
        matriz += [fila]

    return matriz
def inicializar_array(cant_filas:int,valor_inicial:int|str)->list:
    """
        crea una lista de n filas con un valor inicial x

    Args:
        cant_filas (int): cantidad de filas
        valor_inicial (int)|(str): valor que va a tener cada elemento de la lista

    Returns:
        list: retorna una lista de N filas
    """
    lista=[valor_inicial]*cant_filas
    return lista
def calcular_promedio(notas_alumnos:list[list],promedio:list)->None:
    """calcula el promedio de una fila de la matriz

    Args:
        notas_alumnos (list[list]): matriz de notas
        promedio (list): lista de promedios a llenar
    Returns:
        None: no retorna nada
    """
    
    for i in range(len(promedio)):
        suma=0
        for j in range(len(notas_alumnos[i])):
           suma+=notas_alumnos[i][j]
        promedio[i]=suma/len(notas_alumnos[i])
    
    
def ordenar_datos(nombres:list,legajos:list,notas:list[list],generos:list,promedios:list,ordenar_por="DESC")->None:
    """Ordena los datos de la matriz por el promedio de cada fila
       y en caso de ser iguales por el legajo

    Args:
        nombres (list): lista de nombres
        legajos (list): lista de legajos
        notas (list[list]): matriz de notas
        generos (list): lista de generos
        promedios (list): lista de promedios
        ordenar_por (str, optional): metodo de ordenamiento "DESC" para descendente y "ASC" para ascendente. por defecto "DESC".
    returns:
        None: no retorna nada
    """
    nombre_aux=""
    legajo_aux=0
    nota_aux=0
    genero_aux=""
    promedio_aux=0
    for i in range(len(nombres)-1):
        for j in range(i+1,len(nombres)):
            if (promedios[i]<promedios[j] and ordenar_por=="DESC") or (promedios[i]>promedios[j] and ordenar_por=="ASC"):
                nombre_aux=nombres[i]
                legajo_aux=legajos[i]
                nota_aux=notas[i]
                genero_aux=generos[i]
                promedio_aux=promedios[i]
                
                nombres[i]=nombres[j]
                legajos[i]=legajos[j]
                notas[i]=notas[j]
                generos[i]=generos[j]
                promedios[i]=promedios[j]
                
                nombres[j]=nombre_aux
                legajos[j]=legajo_aux
                notas[j]=nota_aux
                generos[j]=genero_aux
                promedios[j]=promedio_aux
            elif (promedios[i]==promedios[j]) and ((legajos[i]<legajos[j] and ordenar_por=="DESC") or (legajos[i]>legajos[j] and ordenar_por=="ASC")):
                nombre_aux=nombres[i]
                legajo_aux=legajos[i]
                nota_aux=notas[i]
                genero_aux=generos[i]
                promedio_aux=promedios[i]
                
                nombres[i]=nombres[j]
                legajos[i]=legajos[j]
                notas[i]=notas[j]
                generos[i]=generos[j]
                promedios[i]=promedios[j]
                
                nombres[j]=nombre_aux
                legajos[j]=legajo_aux
                notas[j]=nota_aux
                generos[j]=genero_aux
                promedios[j]=promedio_aux


def promedio_materias(notas:list[list])->None:
    """Calcula el promedio de cada materia en la matriz de notas

    Args:
        notas (list[list]): matriz de notas de los alumnos

    Returns:
        list: lista con los promedios de cada materia
    """
    Promedios_materias=inicializar_array(5,0)
    for i in range(len(notas)):
        for j in range(len(notas[i])):
            Promedios_materias[j] += notas[i][j]
    for i in range(len(Promedios_materias)):
        Promedios_materias[i] = Promedios_materias[i]/len(notas)   
    return Promedios_materias  

    
def buscar_mayor_promedio(Promedios_materias:list)->list:
    """Busca el mayor promedio de la lista de promedios y devuelve los indices de los mismos
       

    Args:
        Promedios_materias (list): lista de promedios de las materias

    Returns:
        list: lista de indices de los promedios mayores
    """
    
    j = 0
    indices = inicializar_array(len(Promedios_materias), None)
    maximo = Promedios_materias[0]
    for i in range(len(Promedios_materias)):
        if Promedios_materias[i] == maximo:
            indices[j] = i
            j += 1
        elif Promedios_materias[i] > maximo:
            indices = inicializar_array(len(Promedios_materias), None)
            j = 0
            maximo = Promedios_materias[i]
            indices[j] = i
            j += 1
    return indices

def buscar_indice_alumno(legajo:int, legajos:list)->int|None:
    """Busca el indice de un alumno en la lista de legajos

    Args:
        legajo (int): numero de legajo a buscar
        legajos (list): lista de legajos

    Returns:
        int|None: retorna el indice del legajo o None si no lo encuentra
    """
    indice = None
    for i in range(len(legajos)):
        if legajo == legajos[i]:
            indice = i
            break
    return indice
def cantidad_de_notas_materia(notas:list[list],indice_materia:int)->list:
    """"Calcula la cantidad de notas por materia

    Args:
        notas (list[list]): matriz de notas de los alumnos
        indice_materia (int): indice de la materia a calcular

    Returns:
        list: lista con la cantidad de notas por materia
    """
    contador=inicializar_array(10,0)
    for i in range(len(notas)):
            contador[notas[i][indice_materia]-1]+=1
    return contador
            
