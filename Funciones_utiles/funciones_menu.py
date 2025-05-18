from .setterts import *
from .getters import *
from .validaciones import *
from .Funciones_parcial import *
def opcion1(notas_estudiantes:list[list], nombres_estudiantes:list, genero_estudiantes:list, legajo_estudiantes:list,notas_existe:bool)->bool:
    """Carga los datos de los estudiantes

    Args:
        notas_estudiantes (list[list]): matriz de notas de los estudiantes
        nombres_estudiantes (list): lista de nombres de los estudiantes
        genero_estudiantes (list):  lista de generos de los estudiantes
        legajo_estudiantes (list):  lista de legajos de los estudiantes
        notas_existe (bool): booleano que indica si existen notas

    Returns:
        bool: devuelve True cunado cargas las notas
    """
    cargar_notas(notas_estudiantes)
    cargar_nombres(nombres_estudiantes)
    cargar_generos(genero_estudiantes)
    cargar_legajos(legajo_estudiantes)
    notas_existe=True
    return notas_existe

def opcion2(notas_existe:bool,legajos:list,estudiantes:list,generos:list,notas_alumnos:list)->None:
    if notas_existe:
        mostrar_datos(estudiantes,legajos,notas_alumnos,generos)
    else:
        print("No hay datos para mostrar")


def opcion3(notas_existe:bool,notas_alumnos:list[list],promedios:list)->bool:
    if notas_existe:
        calcular_promedio(notas_alumnos,promedios)
        promedios_existe = True
    else:
        print("No hay datos para calcular promedios")
        promedios_existe = False
    return promedios_existe
def opcion4(notas_existe:bool,estudiantes,legajos,notas_alumnos,generos,promedios)->None:
    if notas_existe:
        ordenar_datos(estudiantes,legajos,notas_alumnos,generos,promedios)
        print(promedios)
    else:
        print("No hay datos para mostrar")
def opcion5(notas_existe:bool,notas_alumnos:list)->None:
    """Muestra las materias con mayor promedio

    Args:
        notas_existe (bool): True si existen notas, False si no
        notas_alumnos (list): matriz de notas de los alumnos
    """
    if notas_existe:
                promedio_materias = promedio_materias(notas_alumnos)
                indices = buscar_mayor_promedio(promedio_materias)
                contador_indices = 0
                for i in range(len(indices)):
                    if indices[i] != "null":
                        contador_indices += 1
                if contador_indices > 1:
                    mostrar_mayores_promedios(indices, promedio_materias)
                else:
                    mostrar_mayor_promedio(indices[0], promedio_materias)

def opcion6(promedios_existe:bool,notas_existe:bool,estudiantes:list,legajos:list,notas_alumnos:list[list],generos:list,promedios:list)->None:
    """Muestra los datos de un alumno o todos los alumnos

    Args:
        promedios_existe (bool): booleano que indica si existen promedios
        notas_existe (bool): booleano que indica si existen notas
        estudiantes (list): lista de nombres de los estudiantes
        legajos (list): lista de legajos de los estudiantes
        notas_alumnos (list[list]): matriz de notas de los estudiantes
        generos (list): lista de generos de los estudiantes
        promedios (list): lista de promedios de los estudiantes
    """
    if promedios_existe and notas_existe:
        legajo = get_int(input("Ingrese el numero de legajo a buscar: (Ingresar 0 si quiere ver todos los alumnos.)\n"))
        if legajo != 0:
            if verificar_legajo(legajo):
                indice = buscar_indice_alumno(legajo, legajos)
                mostrar_datos_promedio(indice, estudiantes, legajos, notas_alumnos, generos, promedios)
            else:
                print("Legajo no válido.")
        else:
            mostrar_datos_todos(estudiantes, legajos, notas_alumnos, generos, promedios)
    else:
        print("\nLos promedios o las notas aún no están calculadas. Calcular promedios y notas antes de utilizar esta función.\n")