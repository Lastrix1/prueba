
from .validaciones import *
from .Funciones_parcial import *
def get_int(num:str) -> int | None:
    """convierte un string a un entero

    Args:
        num (str): string a convertir

    Returns:
        int | None: retorna el entero o None si no es un entero
    """
    retorno=None
    if es_numero_entero(num):
        retorno=int(num)
    return retorno
def get_float(num:str)-> float | None:
    """convierte un string a un float

    Args:
        num (str): string a convertir

    Returns:
        int | None: retorna el float o None si no es un float
    """
    retorno=None
    if es_numero_flotante(num):
        retorno=float(num)
    return retorno
def mostrar_dato(indice_i:int,nombres:list,legajos:list,notas:list,generos:list,promedio=0)->None:
    """muestra los datos de la matriz

    Args:
        indice_i (int): fila a mostrar
        nombres (list): lista de nombres
        legajos (list): lista de legajos
        notas (list): lista de notas
        generos (list): lista de generos
        promedio (int, optional): promedio del estudiante es cero si no tiene promedio.
    """
    print("legajo\t nombre\t     nota1\tnota2\tnota3\tnota4\tnota5  genero")
    if promedio == 0:
        if len(nombres[indice_i]) >6:
            print(f"{legajos[indice_i]}\t {nombres[indice_i]}\t{notas[indice_i][0]}\t{notas[indice_i][1]}\t{notas[indice_i][2]}\t{notas[indice_i][3]}\t{notas[indice_i][4]}\t {generos[indice_i]}\t")
        else:
            print(f"{legajos[indice_i]}\t {nombres[indice_i]}\t\t{notas[indice_i][0]}\t{notas[indice_i][1]}\t{notas[indice_i][2]}\t{notas[indice_i][3]}\t{notas[indice_i][4]}\t {generos[indice_i]}\t")
    else:
        if len(nombres[indice_i]) >6:
                print(f"{legajos[indice_i]}\t {nombres[indice_i]}\t{notas[indice_i][0]}\t{notas[indice_i][1]}\t{notas[indice_i][2]}\t{notas[indice_i][3]}\t{notas[indice_i][4]}\t {generos[indice_i]}\t {promedio}\t")
        else:
                print(f"{legajos[indice_i]}\t {nombres[indice_i]}\t\t{notas[indice_i][0]}\t{notas[indice_i][1]}\t{notas[indice_i][2]}\t{notas[indice_i][3]}\t{notas[indice_i][4]}\t {generos[indice_i]}\t {promedio}\t")
def mostrar_datos(nombres:list,legajos:list,notas:list,generos:list,promedio=0)->None:
    """muestra los datos de la matriz

    Args:
        nombres (list): lista de nombres
        legajos (list): lista de legajos
        notas (list): lista de notas
        generos (list): lista de generos
        promedio (int, optional): promedio del estudiante es cero si no tiene promedio.
    """
    
    for i in range(len(nombres)):
        print("---------------------------------------------------------------------------------")
        mostrar_dato(i,nombres,legajos,notas,generos,promedio)


def mostrar_mayores_promedios(indices:list, Promedios_materias:list)->None:
    """Muestra los promedios mayores de la lista de promedios

    Args:
        indices (list): indices de los promedios mayores
        Promedios_materias (list): lista de promedios de las materias
    """
    for i in range(len(Promedios_materias)):
        if indices[i] != None:
            mostrar_mayor_promedio(indices[i], Promedios_materias)


def mostrar_mayor_promedio(indice:int, Promedios_materias:list)->None:
    """Muestra el promedio mayor de la lista de promedios

    Args:
        indice (int): indice del promedio mayor
        Promedios_materias (list): lista de promedios de las materias
    """
    print(f"El mayor promedio es {Promedios_materias[indice]}, le pertenece a la Materia_{indice+1}")
def mostrar_cantidad_de_notas(contador:list,indice_materia:int)->None:
    """Muestra la cantidad de cada nota ingresada en la matriz de notas

    Args:
        contador (list): lista de contador de notas
    """
    for i in range(len(contador)):
        print("---------------------------------------------------------------------------------")
        print(f"La cantidad de {i+1} ingresadas en la materia_{indice_materia} es {contador[i]}")
      