from .validaciones import *
from .getters import *



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
    
    for i in range(len(notas_alumnos)):
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
    Promedios_materias=inicializar_array(5,0)
    for i in range(len(notas)):
        for j in range(len(notas[i])):
            match j:
                case 0:
                    promedio_materias[j]+=notas[i][j]
                case 1:
                    promedio_materias[j]+=notas[i][j]
                case 2:
                    promedio_materias[j]+=notas[i][j]
                case 3:
                    promedio_materias[j]+=notas[i][j]
                case 4:
                    promedio_materias[j]+=notas[i][j]
    for i in range(len(Promedios_materias)):
        Promedios_materias[i]=Promedios_materias[i]/len(notas[0])                    
    return Promedios_materias
    









                
                


            
            