from Funciones_utiles import Funciones_parcial
from Funciones_utiles import funciones_menu

notas_alumnos=[
 [7, 3, 9, 10, 10],
 [6, 10, 2, 10, 10],
 [5, 7, 3, 10, 10],
 [8, 6, 4, 10, 10],
 [9, 2, 5, 10, 10],
 [4, 8, 6, 10, 10],
 [1, 9, 3, 10, 10],
 [2, 4, 8, 10, 10],
 [3, 5, 7, 10, 10],
 [10, 10, 10, 10, 10],
 [7, 1, 9, 10, 10],
 [6, 8, 2, 10, 10],
 [5, 7, 3, 10, 10],
 [8, 6, 4, 10, 10],
 [9, 3, 5, 10, 10],
 [4, 8, 6, 10, 10],
 [2, 10, 3, 10, 10],
 [1, 4, 6, 10, 10],
 [3, 5, 7, 10, 10],
 [6, 8, 10, 10, 10],
 [7, 3, 5, 10,10],
 [4, 6, 8, 10, 10],
 [9, 2, 4, 10, 10],
 [5, 3, 6, 10, 10],
 [2, 4, 7, 10, 10],
 [10, 5, 3, 10, 10],
 [7, 2, 4, 10, 10],
 [1, 1, 1, 10, 10],
 [6, 7, 2, 10, 10],
 [9, 5, 3, 10, 10]
]
estudiantes = [
    "Mateo", "Valentina", "Sofía", "Lucía", "Martín",
    "Alonso", "Isabella", "Camila", "Benjamín", "Emma",
    "Lucas", "Juana", "Daniel", "Valeria", "Sebastián",
    "Paula", "Diego", "Victor", "Jorge", "Sara",
    "Carlos", "Natalia", "Andrés", "Renata", "Gabriel",
    "Mía", "Elena", "Javier", "Laura","Lautaro"
]
generos = [
    'M', 'F', 'F', 'X', 'M', 'M', 'X', 'F', 'X', 'F',
    'M', 'F', 'X', 'F', 'M', 'X', 'M', 'M', 'X', 'F',
    'M', 'X', 'M', 'F', 'X', 'F', 'F', 'X', 'F', 'M'
]
legajos = [
    48392, 10245, 75634, 89901, 34082,
    65127, 27468, 58392, 19284, 74012,
    86543, 90321, 47285, 63819, 12457,
    75102, 86173, 29486, 56712, 41329,
    90284, 14867, 37520, 64281, 79014,
    50632, 81923, 27465, 19584, 64329
]
promedios=Funciones_parcial.inicializar_array(30,0)
notas_estudiantes=Funciones_parcial.inicializar_matriz(30,5,0)
nombres_estudiantes=Funciones_parcial.inicializar_array(30,"")
genero_estudiantes=Funciones_parcial.inicializar_array(30,"")
legajo_estudiantes=Funciones_parcial.inicializar_array(30,0)
notas_existe=True
promedios_existe=False
promedio_materias = Funciones_parcial.inicializar_array(5, 0)

while True:
    print("--------------------------------------\n")
    valor=input(f"Ingresar El numero de la opcion que quiera elegir \n ----------------------------\n 1_Cargar Datos De matriz \n 2_Mostrar Datos \n 3_Calcular Promedio \n 4_Mostrar Datos De Manera Decendiente \n 5_Materias Con Mayor Promedio \n 6_Buscar y Mostrar Datos\n 7_mostrar cuantas veces se repite cada calificación en una asignatura determinada\n 8_Salir\nOpcion: ")
    match valor:
        case "1":
                notas_existe=funciones_menu.opcion1(notas_estudiantes, nombres_estudiantes, genero_estudiantes, legajo_estudiantes,notas_existe)
        case "2":
                funciones_menu.opcion2(notas_existe,legajos,estudiantes,generos,notas_alumnos)
        case "3":
                promedios_existe=funciones_menu.opcion3(notas_existe,notas_alumnos,promedios)
        case "4":
                funciones_menu.opcion4(notas_existe,estudiantes,legajos,notas_alumnos,generos,promedios)
        case "5":
                funciones_menu.opcion5(notas_existe,notas_alumnos)
        case "6":
                funciones_menu.opcion6(promedios_existe,notas_existe,estudiantes,legajos,notas_alumnos,generos,promedios)
        case "7": 
                funciones_menu.opcion7(notas_existe,notas_alumnos)
                
        case "8":
                print("Saliendo del programa...")
                break
        case _:
                print("Opcion no valida, por favor ingrese una opcion valida")