from Funciones_utiles import Funciones_parcial
from Funciones_utiles import setterts
notas_alumnos=[
 [7, 3, 9, 1, 5],
 [6, 10, 2, 4, 8],
 [5, 7, 3, 9, 2],
 [8, 6, 4, 10, 1],
 [9, 2, 5, 7, 3],
 [4, 8, 6, 2, 10],
 [1, 9, 3, 5, 7],
 [2, 4, 8, 6, 10],
 [3, 5, 7, 9, 1],
 [10, 10, 10, 10, 10],
 [7, 1, 9, 3, 5],
 [6, 8, 2, 10, 4],
 [5, 7, 3, 9, 1],
 [8, 6, 4, 2, 10],
 [9, 3, 5, 7, 2],
 [4, 8, 6, 1, 9],
 [2, 10, 3, 5, 7],
 [1, 4, 6, 8, 10],
 [3, 5, 7, 9, 2],
 [6, 8, 10, 1, 4],
 [7, 3, 5, 9, 2],
 [4, 6, 8, 10, 1],
 [9, 2, 4, 7, 5],
 [5, 3, 6, 8, 10],
 [2, 4, 7, 9, 1],
 [10, 5, 3, 5, 6],
 [7, 2, 4, 6, 9],
 [1, 1, 1, 1, 1],
 [6, 7, 2, 4, 8],
 [9, 5, 3, 7, 2]
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
while True:
    valor=input(f"Ingresar El numero de la opcion que quiera elegir \n ----------------------------\n 1_Cargar Datos De matriz \n 2_Mostrar Datos \n 3_Calcular Promedio \n 4_Mostrar Datos De Manera Decendiente \n 5_Materias Con Mayor Promedio \n 6_Buscar y Mostrar Datos\n 7_Salir\n Opcion: ")
    match valor:
        case "1":
            setterts.cargar_notas(notas_estudiantes)
            setterts.cargar_nombres(nombres_estudiantes)
            setterts.cargar_generos(genero_estudiantes)
            setterts.cargar_legajos(legajo_estudiantes)
            notas_existe=True
        case "2":
            if notas_existe:
                Funciones_parcial.mostrar_datos(estudiantes,legajos,notas_alumnos,generos)
            else:
                print("No hay datos para mostrar")
                
        case "3":
            if notas_existe:
                
                Funciones_parcial.calcular_promedio(notas_alumnos,promedios)
            else:
                print("No hay datos para calcular promedios")
        case "4":
            Funciones_parcial.ordenar_datos(estudiantes,legajos,notas_alumnos,generos,promedios,"ASC")
            print(promedios)
        case "5":
            pass