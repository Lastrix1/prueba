from .setterts import *
from .getters import *
from .validaciones import *
from .Funciones_parcial import *
def opcion1(notas_estudiantes, nombres_estudiantes, genero_estudiantes, legajo_estudiantes,notas_existe):
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

def opcion6(promedios_existe:bool,notas_existe:bool,estudiantes,legajos,notas_alumnos,generos,promedios)->None:
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