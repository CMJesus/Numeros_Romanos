import unittest
from romanClass import RomanNumber

#Instanciamos la clase. Una clase es un código que es un molde, que permitirá instanciar objetos, que son patrones de la misma clase -objeto-. La clase es un tipo de objeto -type-. 
#La clase tiene características pertenecientes a sí misma. Roman Number es la clase, y 1 y 2 son objetos de dicha clase.
#Cuando quiero instanciar una clase, hay que inicializarla, el constructor.


class RomanBumberClassTests(unittest.TestCase):
    def test_crear_numero_romano(self):
        uno = RomanNumber(1)
        dos = RomanNumber(2)

        self.assertEqual(uno.cadena, 'I')
        self.assertEqual(dos.cadena, 'II')

        self.assertEqual(uno.valor, 1)                
        self.assertEqual(dos.valor, 2)
        self.assertEqual(uno.cadena, 'I')
        self.assertEqual(dos.cadena, 'II')

        with self.assertRaises(ValueError):
            cuatromil = RomanNumber(4000)

        with self.assertRaises(ValueError):
            cuatromil = RomanNumber('MMMM')

    def test_metodos_magicos_representacion(self):
        uno = RomanNumber(1)

        self.assertEqual(uno.cadena, "I")
