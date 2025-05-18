def es_numero_flotante(num:str)->bool:
    """verifica si una cadena es un numero flotante

    Args:
        num (str): cadena a verificar

    Returns:
        bool: retorna true si es flotante false si no es flotante
    """
    es_flotante=True
    arrlego_prueba=["0","1","2","3","4","5","6","7","8","9","."]
    for caracter in num:
        if caracter not in arrlego_prueba:
            es_flotante=False
    return es_flotante
            
    
def es_numero_entero(num:str)->bool:
    """Verifica si el parametro es un numero entero

    Args:
        num (int): numero a verificar

    Returns:
        bool: devuelve el True si el valor es numero entero False en caso de no serlo
    """
    es_un_numero_entero=True
    if len(num)==0:
        es_un_numero_entero=False
    for i in range(len(num)):
        if ord(num[i])<48 or ord(num[i])>57:
            es_un_numero_entero=False
    return es_un_numero_entero
def pasar_a_mayuscula(palabra:str)->str:
    """pasa una palabra a mayuscula

    Args:
        palabra (str): palabra a pasar a mayuscula

    Returns:
        str: devuelve la palabra en mayuscula
    """
    palabra_mayuscula=""
    for i in range(len(palabra)):
        if ord(palabra[i])>96 and ord(palabra[i])<123:
            palabra_mayuscula+=chr(ord(palabra[i])-32)
        else:
            palabra_mayuscula+=palabra[i]
    return palabra_mayuscula
def pasar_a_minuscula(palabra:str)->str:
    """pasa una palabra a minuscula

    Args:
        palabra (str): palabra a pasar a minuscula

    Returns:
        str: devuelve la palabra en minuscula
    """
    palabra_minuscula=""
    for i in range(len(palabra)):
        if ord(palabra[i])>64 and ord(palabra[i])<91:
            palabra_minuscula+=chr(ord(palabra[i])+32)
        else:
            palabra_minuscula+=palabra[i]
    return palabra_minuscula
def verificar_legajo(legajo:int)->bool:
    """verifica si el legajo es valido

    Args:
        legajo (int): legajo a verificar

    Returns:
        bool: retorna true si el legajo es valido y false si no
    """
    es_valido=True
    if legajo<1 or legajo>99999:
        es_valido=False
    return es_valido

def vericar_nombre(nombre:str)->bool:
    """verifica si el nombre es valido

    Args:
        nombre (str): nombre a verificar

    Returns:
        bool: retorna true si el nombre es valido y false si no
    """
    es_valido=True
    if len(nombre)<1:
        es_valido=False
    for letra in nombre:
        if ((ord(letra)>64 and ord(letra)<91) or (ord(letra)>96 and ord(letra)<123)) != True:
            es_valido=False
    return es_valido

def vericar_nota(nota:int)->bool:
    """verifica si la nota es valida

    Args:
        nota (int): nota a verificar

    Returns:
        bool: retorna true si la nota es valida y false si no
    """
    es_valida=True
    if nota<1 or nota>10:
        es_valida=False
    return es_valida

def verificar_genero(genero:str)->bool:
    """verifica si es un genero valido

    Args:
        genero (str): genero a verificar

    Returns:
        bool: retorno true si el genero es valido y false si no
    """

    generos_validos=["F","M","X"]
    retorno=False
    if pasar_a_mayuscula(genero)  in generos_validos:
        retorno=True
    return retorno

