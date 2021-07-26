# Estructura de datos que vamos a usar para guardar los símbolos romanos, a esta estructura le llamaremos "símbolo"
# Diccionario con clave : valor

simbolos = {
    'unidades': ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
    'decenas': ['','X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
    'centenas': ['','C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
    'millares': ['','M', 'MM', 'MMM']
}


def validar(n):
    """    
        Restricciones: n es un entero
            n > 0
            n < 4000
    """
        
    if not isinstance(n, int):
        raise ValueError("{} debe de ser un entero".format(n))

    if n < 0 or n > 3999:
        raise ValueError("{} debe de estar entre 0 y 3999".format(n))


def a_romano(n):
    """
        Restricciones: n es un entero
            n > 0
            n < 4000
        
        Descomponer n en millares, centenas, decenas y unidades
        Traducir millares, centenas, decenas y unidades
        Concatenar millares, centenas, decenas y unidades
        con isinstance, puedo comprobar el tipo de dato que tenemos delante
    
    """


    # lo primero sería validar que el número fuera mayor que 0 y menor que 4000
    # lo segundo sería descomponer.     

    validar(n)

    # try and except

    # Ahora toca descomponer - bucle FOR o IF

    # c = "{:04d}".format(n) > función leading zeros, al ser números menores de 4 zeros, rellena con zeros a la izquierda (así hacemos la función fija en 4 números)
    # mirar clase de nuevo del día 20, al inicio se plantea con la función de arriba.


    c = "{:04d}".format(n)
    #str(n)

    unidades = int(c[-1])
    #0 
    decenas = int(c[-2])
    #0
    centenas = int(c[-3])
    #0
    millares = int(c[-4])
    #0

    #    if len(c) >= 1:
    #        unidades = int(c[-1])
    #    if len(c) >= 2:
    #        decenas = int(c[-2])
    #    if len(c) >= 3:
    #        centenas = int(c[-3])
    #    if len(c) >= 4:
    #        millares = int(c[-4])

    
    # Traducción

    return simbolos['millares'][millares] + simbolos['centenas'][centenas] + simbolos['decenas'][decenas] + simbolos['unidades'][unidades]