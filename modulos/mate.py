def suma(a:int,b:int)->int:
    """funcion para sumar dos numeros

    args:
        b(int): numero entero positivo
        a(int): numero entero positivo puede =>0

    return
    int: retorna el resultado d ela suma  de a+b
    none: en caso el valor de la a o b sea memnor a 0
    """
    if a<0:
        return None
    elif b<0:
        return None
    return a+b
PI=3,141516