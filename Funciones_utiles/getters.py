from .validaciones import *
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
def get_float(num:str)-> int | None:
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
def mostrar_dato(indice_i:int,nombres:list,legajos:list,notas:list,generos:list,indice_j=0)->None:
    """muestra los datos de la matriz

    Args:
        indice_i (int): fila a mostrar
        indice_j (int): columna a mostrar
        nombres (list): lista de nombres
        legajos (list): lista de legajos
        notas (list): lista de notas
        generos (list): lista de generos
    """
    if len(nombres[indice_i]) >6:
        print(f"{legajos[indice_i]}\t {nombres[indice_i]}\t{notas[indice_i][0]}\t{notas[indice_i][1]}\t{notas[indice_i][2]}\t{notas[indice_i][3]}\t{notas[indice_i][4]}\t {generos[indice_i]}\t")
    else:
        print(f"{legajos[indice_i]}\t {nombres[indice_i]}\t\t{notas[indice_i][0]}\t{notas[indice_i][1]}\t{notas[indice_i][2]}\t{notas[indice_i][3]}\t{notas[indice_i][4]}\t {generos[indice_i]}\t")

def mostrar_datos(nombres:list,legajos:list,notas:list,generos:list)->None:
    """muestra los datos de la matriz

    Args:
        nombres (list): lista de nombres
        legajos (list): lista de legajos
        notas (list): lista de notas
        generos (list): lista de generos
    """
    print("legajo\t nombre\t     nota1\tnota2\tnota3\tnota4\tnota5  genero")
    for i in range(len(nombres)):
        print("---------------------------------------------------------------------------------")
        for j in range(len(notas[i])):
            mostrar_dato(i,nombres,legajos,notas,generos,j)


def mostrar_mayores_promedios(indices, Promedios_materias):
    for i in range(len(Promedios_materias)):
        if indices[i] != "null":
            mostrar_mayor_promedio(indices[i], Promedios_materias)


def mostrar_mayor_promedio(indice, Promedios_materias):
    print(f"El mayor promedio es {Promedios_materias[indice]}, le pertenece a la Materia_{indice+1}")

#buscAR Y MOSTRAR DATOS DE UN ESTUDIANTE POR LEGAJO, incluyendo promedio


def buscar_indice_alumno(legajo, legajos):
    indice = None
    for i in range(len(legajos)):
        if legajo == legajos[i]:
            indice = i
            break
    return indice

def mostrar_datos_promedio(indice_i:int,nombres:list,legajos:list,notas:list,generos:list,promedios:list)->None:
    if len(nombres[indice_i]) >6:
        print(f"{legajos[indice_i]}\t {nombres[indice_i]}\t{notas[indice_i][0]}\t{notas[indice_i][1]}\t{notas[indice_i][2]}\t{notas[indice_i][3]}\t{notas[indice_i][4]}\t {generos[indice_i]}\t {promedios[indice_i]}\t")
    else:
        print(f"{legajos[indice_i]}\t {nombres[indice_i]}\t\t{notas[indice_i][0]}\t{notas[indice_i][1]}\t{notas[indice_i][2]}\t{notas[indice_i][3]}\t{notas[indice_i][4]}\t {generos[indice_i]}\t {promedios[indice_i]}\t")

def mostrar_datos_todos(nombres:list,legajos:list,notas:list,generos:list,promedios:list)->None:
    for i in range(len(nombres)):
        mostrar_datos_promedio(i, nombres, legajos, notas, generos, promedios)