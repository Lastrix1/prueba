import random

def mostrar_datos(lista_a:list, lista_b:list, lista_c:list) -> None:

    for i in range(len(lista_a)):

        if len(lista_a[i]) < 8:
            print(f"{lista_a[i]}\t\t{lista_b[i]}\t{lista_c[i]}")
        else:
            print(f"{lista_a[i]}\t{lista_b[i]}\t{lista_c[i]}")    

def copiar_lista(lista_a:list, lista_b:list)->list:
    nombres_originales = [-1] * len(lista_a)
    edades_originales = [-1] * len(lista_b)

    for i in range(len(lista_a)):
        nombres_originales[i] = lista_a[i]
        edades_originales[i] = lista_b[i]
    
    return nombres_originales, edades_originales

def ordenar_ascendente(lista_a:list, lista_b:list, lista_c:list) -> None:

    for i in range(0, len(lista_a)-1, 1):
        
        for j in range(i + 1, len(lista_a), 1):
            
            if lista_c[i] > lista_c[j]:
            
                edad_auxiliar = lista_b[i]
                lista_b[i] = lista_b[j]
                lista_b[j] = edad_auxiliar

                nombre_auxiliar = lista_a[i]
                lista_a[i] = lista_a[j]
                lista_a[j] = nombre_auxiliar

                genero_auxiliar = lista_c[i]
                lista_c[i] = lista_c[j]
                lista_c[j] = genero_auxiliar
#2 criterio 
            elif lista_c[i] == lista_c[j]:
                if lista_a[i] > lista_a[j]:
                    edad_auxiliar = lista_b[i]
                    lista_b[i] = lista_b[j]
                    lista_b[j] = edad_auxiliar

                    nombre_auxiliar = lista_a[i]
                    lista_a[i] = lista_a[j]
                    lista_a[j] = nombre_auxiliar

def ordenar_descendente(lista_a:list, lista_b:list, lista_c:list) -> None:

    for i in range(0, len(lista_a)-1, 1):
        
        for j in range(i + 1, len(lista_a), 1):
            
            if lista_c[i] < lista_c[j]:
            
                edad_auxiliar = lista_b[i]
                lista_b[i] = lista_b[j]
                lista_b[j] = edad_auxiliar

                nombre_auxiliar = lista_a[i]
                lista_a[i] = lista_a[j]
                lista_a[j] = nombre_auxiliar

                genero_auxiliar = lista_c[i]
                lista_c[i] = lista_c[j]
                lista_c[j] = genero_auxiliar
#2 criterio 
            elif lista_c[i] == lista_c[j]:
                if lista_a[i] < lista_a[j]:
                    edad_auxiliar = lista_b[i]
                    lista_b[i] = lista_b[j]
                    lista_b[j] = edad_auxiliar

                    nombre_auxiliar = lista_a[i]
                    lista_a[i] = lista_a[j]
                    lista_a[j] = nombre_auxiliar

def ordenar(lista_a:list, lista_b:list, lista_c:list, primer_modo = 1, segundo_modo= 1) -> None:

    for i in range(0, len(lista_a)-1, 1):
        
        for j in range(i + 1, len(lista_a), 1):
            
            if (lista_c[i] > lista_c[j] and primer_modo == 1) or (lista_c[i] < lista_c[j] and primer_modo == 2):
                #SWAP(intercambio)
                edad_auxiliar = lista_b[i]
                lista_b[i] = lista_b[j]
                lista_b[j] = edad_auxiliar

                nombre_auxiliar = lista_a[i]
                lista_a[i] = lista_a[j]
                lista_a[j] = nombre_auxiliar

                genero_auxiliar = lista_c[i]
                lista_c[i] = lista_c[j]
                lista_c[j] = genero_auxiliar
#2 criterio 
            elif lista_c[i] == lista_c[j]:
                if (lista_a[i] > lista_a[j] and segundo_modo == 1) or (lista_a[i] < lista_a[j] and segundo_modo == 2):
                    edad_auxiliar = lista_b[i]
                    lista_b[i] = lista_b[j]
                    lista_b[j] = edad_auxiliar

                    nombre_auxiliar = lista_a[i]
                    lista_a[i] = lista_a[j]
                    lista_a[j] = nombre_auxiliar

def inicializar_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz


def SumaMatriz(matriz1, matriz2):
    filas = len(matriz1)
    columnas = len(matriz1[0])
    resultado = inicializar_matriz(filas, columnas, 0)
    for i in range(filas):
        for j in range(columnas):
            resultado [i][j] = matriz1[i][j] + matriz2[i][j]
    for l in range(len(resultado)):
        for h in range(len(resultado[i])):
            print(resultado[l][h], end=" ")
        print(" ")

#SumaMatriz(matiz1, matiz2)

def productoMatrices_escalar(matriz1, escalar):
    filas = len(matriz1)
    columnas = len(matriz1[0])
    resultado = inicializar_matriz(filas, columnas, 0)
    for i in range(len(matriz1)):
        for j in range(len(matriz1[i])):
            resultado[i][j] = matriz1[i][j] * escalar

    for l in range(len(resultado)):
        for h in range(len(resultado[i])):
            print(resultado[l][h], end=" ")
        print(" ")
    
#productoMatrices_escalar(matiz1, 5)

def producto_matricial(matriz_A,matriz_B,filas_A,filas_B,columnas_A,columnas_B):
    resultado = inicializar_matriz(filas_A,columnas_B,0)
    for i in range(filas_A):
        for j in range(columnas_B):
            for k in range(columnas_A):
                resultado[i][j] += matriz_A[i][k] * matriz_B[k][j] 

    for l in range(len(resultado)):
        for h in range(len(resultado[i])):
            print(resultado[l][h], end=" ")
        print(" ")
    return resultado

def palindromo(palabra:str)->bool:
    Es_Palindromo=True
    for i in range(len(palabra)):   
        if palabra[i] != palabra[(len(palabra)-1)-i]:

            Es_Palindromo=False
            break
    return Es_Palindromo

def limpiar_espacios(palabra:str)->str:
    lista_frase=""
    for i in range(len(palabra)):
        if palabra[i] != " ":
            lista_frase+=palabra[i]
    return lista_frase


def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end = " ")
        print("")

def buscar_datos(dnis:list,dni:int) -> int:

    indice = None
    for index in range (len(dnis)): 
        if dnis[index] == dni:
            indice = index
            break
    return indice

def cargar_datos_secuencial(nombres: list, edades: list, generos: list, estaturas: list, dnis: list, tamano: int) -> None:
    for i in range(tamano):
        nombres[i] = input("Nombre: ")
        while nombres[i] == "x":
            nombres[i] = input("Nombre: ")

        edades[i] = int(input("Edad: "))
        while edades[i] < 0 or edades[i] > 100:
            edades[i] = int(input("Edad: "))

        generos[i] = input("Genero: ")
        estaturas[i] = input("Estatura: ")
        dnis[i] = input("DNI: ")

def imprimir_dato(nombres: list, edades: list, generos: list, estaturas: list, dnis: list, indice: int) -> None:
    print(f"{nombres[indice]}\t {edades[indice]}\t  {generos[indice]}\t  {estaturas[indice]}\t\t{dnis[indice]}")

def imprimir_datos(nombres: list, edades: list, generos: list, estaturas: list, dnis: list, tamano: int) -> None:
#def imprimir_datos(tamano: int) -> None:
    for i in range(tamano):
        imprimir_dato(nombres, edades, generos, estaturas, dnis, i)


def suma_pares(lista:list[int]) -> int:
    """
    Función para calcular la suma de los números pares en una lista.
    Args:
        lista: list[int]: Lista de números enteros.
    Returns:
        int: Suma de los números pares en la lista.
    """
    pares = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            pares += lista[i]
    return pares

def pares(lista:list[int]) -> int:
    """
    Función para contar la cantidad de números pares en una lista.
    Args:
        lista: list[int]: Lista de números enteros. 
    Returns:
        int: Cantidad de números pares en la lista.
    """
    pares = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            pares += 1
    return pares

def neg(lista:list[int]) -> int:
    """
    Función para contar la cantidad de números negativos en una lista.
    Args:
        lista: list[int]: Lista de números enteros.
    Returns:
        int: Cantidad de números negativos en la lista.
    """
    negativos = 0
    for i in range(len(lista)):
        if lista[i] < 0:
            negativos +1
    return negativos

def positivos(lista:list[int]) -> int:
    """
    Función para contar la cantidad de números positivos en una lista.
    Args:
        lista: list[int]: Lista de números enteros.
    Returns:
        int: Cantidad de números positivos en la lista.
    """
    positivos = 0
    for i in range(len(lista)):
        if lista[i] > 0:
            positivos += 1
    return positivos

def mayor_inpar(lista:list[int]) -> int | None:
    """
    Función para encontrar el número impar más grande en una lista.
    Args:
        lista: list[int]: Lista de números enteros.
    Returns:
        int | None: El número impar más grande en la lista, o None si no hay impares.
    """
    mayor = None
    for i in range(len(lista)):
        if lista[i] % 2 != 0:
            if mayor == None:
                mayor = lista[i]
            elif lista[i] > mayor:
                mayor = lista[i]
    return mayor

def get_int(mensaje: str, mensaje_error: str, minimo:int, maximo:int, reintentos:int) -> int | None:
    """
    Función para validar un número entero dentro de un rango específico.
    Args:
        mensaje: str: Mensaje que se muestra al usuario para ingresar el número.
        mensaje_error: str: Mensaje de error que se muestra si la validación falla.
        minimo: int: Valor mínimo permitido.
        maximo: int: Valor máximo permitido.
        reintentos: int: Número de intentos permitidos para ingresar un valor válido.
    Returns:
        int | None: Devuelve el número entero ingresado si es válido, de lo contrario None.
    """
    flag = None
    print(mensaje)
    for i in  range(reintentos):
        num = input(f'Ingrese un entero entre {minimo} y {maximo}, tenes {reintentos} intentos: ')
        flag, flag_2 = validate_number(num, maximo, minimo)
        if flag == None or flag_2 == True: 
            print(mensaje_error)
        else:
            break
    return flag

def validate_length(palabra:str, longitud:int) -> str | None:
    """
    Función para validar la longitud de una cadena de texto.
    Args:
        palabra: str: Cadena de texto a validar.
        longitud: int: Longitud exacta que debe tener la cadena.
    Returns:
        str | None: Devuelve la cadena si es válida, de lo contrario None.
    """
    flag = None
    letras = len(palabra)
    if letras == longitud:
        flag = palabra
    return flag

def validate_number(num:int, maximo:int, minimo:int,) -> int | None:
    '''
    Función para validar un número dentro de un rango específico.
    Args:
        num: str: Número a validar.
        maximo: int: Valor máximo permitido.
        minimo: int: Valor mínimo permitido.
    Returns:
        int | None: Devuelve el número entero si es válido, de lo contrario None.
    '''
    numero = None
    flag_2 = None
    no_digit = False
    for elemento in num:
        if elemento == '.':
            flag_2 = True
        if ord(elemento) < 44 or ord(elemento) > 57:
            no_digit = True   
            break
    if no_digit == False:
        if flag_2 == True:
            num = float(num)
        else:
            num = int(num)
        if num > maximo or num < minimo:
            numero = None
        else:
            numero = num
    return numero, flag_2


def get_float(mensaje: str, mensaje_error: str, minimo:int, maximo:int, reintentos:int) -> float | None:
    """
    Función para validar un número flotante dentro de un rango específico.
    Args:
        mensaje: str: Mensaje que se muestra al usuario para ingresar el número.
        mensaje_error: str: Mensaje de error que se muestra si la validación falla.
        minimo: int: Valor mínimo permitido.
        maximo: int: Valor máximo permitido.
        reintentos: int: Número de intentos permitidos para ingresar un valor válido.
    Returns:
        int | None: Devuelve el número flotante ingresado si es válido, de lo contrario None.
    """
    flag = None
    print(mensaje)
    for i in  range(reintentos):
        num = input(f'Ingrese un float entre {minimo} y {maximo}, tenes {reintentos} intentos: ')
        flag, flag_2 = validate_number(num, maximo, minimo)
        if flag == None:
            print(mensaje_error)
        else:
            flag = float(flag)
            break
    return flag
    
def get_str(mensaje:str, mensaje_error:str, longitud:int, reintentos:int) -> str |None: 
    """
    Función para validar una cadena de texto con una longitud específica.
    Args:
        mensaje: str: Mensaje que se muestra al usuario para ingresar la cadena.
        mensaje_error: str: Mensaje de error que se muestra si la validación falla.
        longitud: int: Longitud exacta que debe tener la cadena.
        reintentos: int: Número de intentos permitidos para ingresar un valor válido.
    Returns:
        str | None: Devuelve la cadena ingresada si es válida, de lo contrario None.
    """
    flag = None
    print(mensaje)
    for i in  range(reintentos):
        palabra = input(f'Ingrese una string con un maximo de {longitud} caracteres, tenes {reintentos} intentos: ')
        flag = validate_length(palabra, longitud)
        if flag == None:
            print(mensaje_error)
        else:
            break
    return flag


def crearlista():
    cantidad = int(input('Ingrese el tamano: '))
    lista = [0] * cantidad
    for i in range(cantidad):
        lista[i] = i
    print(lista)

num = [1, 3, 54, 657, 34, 657]

def max(lista):
    maximo = None
    pos = ''
    for i in lista:
        if maximo == None:
            maximo = i
        if i >= maximo:
            maximo = i
    print(maximo)
    for p in range(len(lista)):
        if lista[p] == maximo:
            pos += str(p)
            pos += ' '
    return pos

def remplazar_nombres(lista_nombres, nombre_nuevo, nombre_viejo):
    remplace = 0
    for i in range(len(lista_nombres)):
        if lista_nombres[i] == nombre_viejo:
            lista_nombres[i] = nombre_nuevo
            remplace += 1
    print(lista_nombres)    
    return remplace


#Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la intersección de los dos arrays.

def inte(lista1, lista2):
    for d in range(len(lista1)):
        for s in range(len(lista2)):
            if lista1[d] == lista2[s]:
                print(lista1[d])

def union(lista1, lista2):
    # Crear una lista vacía con un tamaño suficiente para almacenar la unión
    resultado = [0] * (len(lista1) + len(lista2))
    indice = 0

    # Copiar los elementos de la primera lista al resultado
    for i in range(len(lista1)):
        resultado[indice] = lista1[i]
        indice += 1

    # Agregar los elementos de la segunda lista que no están en la primera
    for i in range(len(lista2)):
        repetido = False
        for j in range(len(lista1)):
            if lista2[i] == lista1[j]:
                repetido = True
                break
        if not repetido:
            resultado[indice] = lista2[i]
            indice += 1

    # Mostrar la unión (sin los espacios vacíos)
    for i in range(indice):
        print(resultado[i])


def diferencia(lista1, lista2):
    # Crear una lista vacía con un tamaño suficiente para almacenar la diferencia
    resultado = [0] * len(lista1)
    indice = 0

    # Agregar los elementos de la primera lista que no están en la segunda
    for i in range(len(lista1)):
        repetido = False
        for j in range(len(lista2)):
            if lista1[i] == lista2[j]:
                repetido = True
                break
        if not repetido:
            resultado[indice] = lista1[i]
            indice += 1

    # Mostrar la diferencia (sin los espacios vacíos)
    for i in range(indice):
       print(resultado[i])

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def indentificar_numeros(cadena):
    hay = None
    for i in cadena:
        if ord(i) < 47 or ord(i) > 57:
            hay = False
        else:
            hay = True
    return hay

def verificar_cadena (palabra:list):
    largo = len(palabra)
    lista = [' '] * largo  
    indice = 0  
    resultado = ''
    for i in palabra:
        if ord(i) >= 48 and ord(i) <= 57: 
            continue
        else:
            lista[indice] = i
            indice += 1
    print(lista)
    for i in lista:
        resultado += i
    print(resultado)

def es_cuadrado_magico(matriz):
    es_magico = None
    n = len(matriz)
    constante_magica = n * (n**2 + 1) // 2

    # Suma de filas
    for fila in matriz:
        if sum(fila) != constante_magica:
            es_magico = False

    # Suma de columnas
    for columnas in range(n):
        if sum(matriz[fila][columnas] for fila in range(n)) != constante_magica:
            es_magico = False

    # Suma de diagonales
    if sum(matriz[i][i] for i in range(n)) != constante_magica:
        es_magico = False
    if sum(matriz[i][n - i - 1] for i in range(n)) != constante_magica:
        es_magico = False
    
    es_magico = True 

    return es_magico

def generar_legajos():

    matriz_legajos = [] 
    for i in range(3):
        fila = [-1] * 5
        matriz_legajos += [fila]
    contador = 0
    print(matriz_legajos)
    for i in range(len(matriz_legajos)):
        for j in range(len(matriz_legajos[i])):
            if matriz_legajos[i][j] == -1:
                legajo = random.randint(1000, 9999)
                matriz_legajos[i][j] = legajo
                contador += 1
                if contador >= 15:
                    break
        if contador >= 15:
            break
    print(matriz_legajos)
    return matriz_legajos

def validar_legajo(legajo, matriz_legajos):
    valido = False
    for i in range(len(matriz_legajos)):
        for j in range(len(matriz_legajos[i])):
            if matriz_legajos[i][j] == legajo:
                valido = True
    return valido