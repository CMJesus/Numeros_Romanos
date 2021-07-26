simbolos = {
    'unidades': ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
    'decenas': ['','X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
    'centenas': ['','C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
    'millares': ['','M', 'MM', 'MMM']
}

digitos_romanos = {
    'I': 1, 'V':5,  'X':10,  'L':50, 'C':100, 'D':500, 'M':1000
}


def a_numero(cadena):
    acumulador = 0
    valor_ant = 0
    
    """Toda esta parte es la implementada en la clase 03
    Condición de repetición V, 
    if valor_ant in (5, 50, 500) and cuenta_repeticiones > 0: 
        raise ValueError("No se pueden repetir V, L o D")"""

    cuenta_repeticiones = 0
    cuenta_restas = 0
    
    for caracter in cadena:
        valor = digitos_romanos.get(caracter)
        if not valor:
            raise ValueError("El mío")
        
        #if valor_ant in (5, 50, 500) and cuenta_repeticiones > 0:
        #    raise ValueError("No se pueden repetir V, L o D")
        # Esta la comentó Albert, y luego Fran comentó la de la línea 54. Son lo mismo, pero la otra es más natural
        """Hasta aquí"""
        # Para que nos compute los errores, hemos creado cuentarepeticiones.
            # Esta parte se deja sin efecto.
            # for caracter in cadena:
            #    valor = digitos_romanos.get(caracter)
            #   if not valor:
            #       raise ValueError("El Mío")
        
        if valor_ant > 0 and valor > valor_ant:
            #Aquí me falta comprender la parte inicial antes del "and".
            if cuenta_restas > 0:
                raise ValueError("No se pueden realizar restas consecutivas")
            if cuenta_repeticiones > 0:
                raise ValueError("No se pueden hacer restas dentro de repeticiones")
            if valor_ant in (5, 50, 500):
                raise ValueError("No se pueden restar V. L o D")
            if valor_ant > 0 and valor > 10 * valor_ant:    
                raise ValueError("No se admiten restas de dígitos 10 veces mayores")

            acumulador -= valor_ant
            acumulador += valor - valor_ant
            # -= y += lo que hace es lo siguiente acumulador = acumulador - valor_ant, y el sumatorio: acumulador = acumulador + valor - valor_ant
            cuenta_restas += 1
        else:
            acumulador += valor
            cuenta_restas = 0

        if valor == valor_ant:
            if valor_ant in (5, 50, 500):
                raise ValueError("No se pueden repetir V, L o D")
            cuenta_repeticiones += 1
            if cuenta_repeticiones == 3:
                raise ValueError("Demasiadas repeticiones de {}".format(caracter))       
        else:
            cuenta_repeticiones = 0
                
        valor_ant = valor
    
    return acumulador

#def validar(n):

#def a_romano(n): 