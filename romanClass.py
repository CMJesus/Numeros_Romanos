class RomanNumber():

    simbolos = {
        'unidades': ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
        'decenas': ['','X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
        'centenas': ['','C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
        'millares': ['','M', 'MM', 'MMM']
}

    digitos_romanos = {
    'I': 1, 'V':5,  'X':10,  'L':50, 'C':100, 'D':500, 'M':1000
}


    def __init__(self, valor):

        if isinstance(valor, int):
            self.valor = valor
            self.cadena = self.a_romano()

        if isinstance(valor, str):
            self.cadena = valor
            self.valor = self.a_numero()


    def validar(self):
        #Método de instancia. Muy importante indicar el parámetro de la instancia. 
        if not isinstance(self.valor, int):
            raise ValueError("{} debe de ser un entero".format(self.valor))

        if self.valor < 0 or self.valor > 3999:
            raise ValueError("{} debe de estar entre 0 y 3999".format(self.valor))


    def a_romano(self):
        self.validar()
        c = "{:04d}".format(self.valor)

        unidades = int(c[-1])
        decenas = int(c[-2])
        centenas = int(c[-3])
        millares = int(c[-4])

        return self.simbolos['millares'][millares] + self.simbolos['centenas'][centenas] + self.simbolos['decenas'][decenas] + self.simbolos['unidades'][unidades]


    def a_numero(self):
        acumulador = 0
        valor_ant = 0
        cuenta_repeticiones = 0
        cuenta_restas = 0
    
        for caracter in self.cadena:
            valor = self.digitos_romanos.get(caracter)
            if not valor:
                raise ValueError("El mío")
        
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
    
    def __str__(self):
        return self.cadena

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self.cadena)

    def __eq__(self, other):
        if isinstance(ther, RomanNumber):
            return self.valor == other.valor
        if isinstance(other, int):
            return self.valor == other
        if isinstance(other, float):
            return self.valor == other
        if isinstance(other, str):
            return self.cadena == other
        raise ValueError("{} solo puede ser entero, cadena, flotante o ROmanNumber".forma(other))
