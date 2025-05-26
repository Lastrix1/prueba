
from .getters import *
from .validaciones import *
from .Funciones_parcial import *

def cargar_notas(fila:int,columna:int,matriz:list[list])->list[list]:
    """carga una matriz de notas

    Args:
        matriz (list[list]): matriz a llenar

    Returns:
        list[list]: devuelve una matriz llena de notas
    """
    
 
    while True:
        valor=input(f"ingrese la nota de la fila {fila} columna {columna}: ")
        nota=get_int(valor)
        if vericar_nota(nota):
            matriz[fila][columna]=nota
            break
        else:
            print("ERROR nota no valida")
    return matriz

def cargar_nombres(indice:int,lista:list)->list:
    """carga una lista de nombres

    Args:
        lista (list): lista a llenar

    Returns:
        list: devuelve una lista llena de nombres
    """

    while True:
        nombre=input(f"ingrese el nombre de la fila {indice}: ")
        if vericar_nombre(nombre):
                
            lista[indice]=nombre
            break
        else:
            print("ERROR nombre no valido")
    return lista

def cargar_legajo(indice:int,lista:list)->list:
    """carga una lista de legajos

    Args:
        lista (list): lista a llenar

    Returns:
        list: devuelve una lista llena de legajos
    """
   
    while True:
        legajo=get_int(input(f"ingrese el legajo de la fila {indice}: "))
        if verificar_legajo(legajo):
            lista[indice]=legajo
            break
        else:
            print("ERROR legajo no valido")
    return lista

def cargar_genero(indice:int,lista:list)->list:
    """carga una lista de genero

    Args:
        lista (list): lista a llenar con generos

    Returns:
        list: devuelve una lista llena de generos
    """
    while True:
        genero=input(f"ingrese el genero de la fila {indice}: ")
        if verificar_genero(genero):
            lista[indice]=genero
            break
        else:
            print("ERROR genero no valido")
    return lista
def cargar_datos(nombres:list,legajos:list,generos:list,notas_alumnos:list[list])->None:
    """carga los datos de los alumnos

    Args:
        nombres (list): lista de nombres
        legajos (list): lista de legajos
        generos (list): lista de generos
        notas_alumnos (list[list]): matriz de notas
        filas (int): cantidad de filas
        columnas (int): cantidad de columnas
    """
    for i in range(len(nombres)):
        cargar_nombres(i,nombres)
        cargar_legajo(i,legajos)
        cargar_genero(i,generos)
        for j in range(len(notas_alumnos[i])):
            cargar_notas(i,j,notas_alumnos)