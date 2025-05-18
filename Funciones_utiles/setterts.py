from .setterts import *
from .getters import *
from .validaciones import *
from .Funciones_parcial import *
def cargar_notas(matriz:list[list])->list[list]:
    """carga una matriz de notas

    Args:
        matriz (list[list]): matriz a llenar

    Returns:
        list[list]: devuelve una matriz llena de notas
    """
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            while True:
                nota=get_int(input(f"ingrese la nota de la fila {i} columna {j}: "))
                if vericar_nota(nota):
                    matriz[i][j]=nota
                    break
                else:
                    print("ERROR nota no valida")
    return matriz

def cargar_nombres(lista:list)->list:
    """carga una lista de nombres

    Args:
        lista (list): lista a llenar

    Returns:
        list: devuelve una lista llena de nombres
    """
    for i in range(len(lista)):
        while True:
            nombre=input(f"ingrese el nombre de la fila {i}: ")
            if vericar_nombre(nombre):
                
                lista[i]=nombre
                break
            else:
                print("ERROR nombre no valido")
    return lista

def cargar_legajos(lista:list)->list:
    """carga una lista de legajos

    Args:
        lista (list): lista a llenar

    Returns:
        list: devuelve una lista llena de legajos
    """
    for i in range(len(lista)):
        while True:
            legajo=get_int(input(f"ingrese el legajo de la fila {i}: "))
            if verificar_legajo(legajo):
                lista[i]=legajo
                break
            else:
                print("ERROR legajo no valido")
    return lista

def cargar_generos(lista:list)->list:
    """carga una lista de genero

    Args:
        lista (list): lista a llenar con generos

    Returns:
        list: devuelve una lista llena de generos
    """
    for i in range(len(lista)):
        while True:
            genero=input(f"ingrese el genero de la fila {i}: ")
            if verificar_genero(genero):
                lista[i]=genero
                break
            else:
                print("ERROR genero no valido")
    return lista