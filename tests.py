import unittest
# Librería test unitario. Para testeo automático de códigopygame.examples.aliens.main()
# La librería tiene una clase definida "testCase" > Busca tests y ejecuta tests
from numeros_normal import a_numero

class RomanosTests(unittest.TestCase):
    # nuestra clase hereda la funcionalidad de la clase inserta en la librería.
    def test_digitos_romanos(self):
        self.assertEqual(a_numero('I'), 1) 
        # Método específico de la clase testCase que asegura que lo que se ponga como primer parámetro de la función sea igual al segundo parámetro.
        self.assertEqual(a_numero('V'), 5)

    def test_numeros_completos(self):
        self.assertEqual(a_numero('XXV'), 25)
        self.assertEqual(a_numero('CDXXIV'), 424)

    def test_no_se_resta_ni_V_L_D(self):    
        with self.assertRaises(ValueError):
            a_numero('VC')
            a_numero
            # Me quedo por aquí
            
    def test_no_se_resta_mas_de_un_salto(self):
        self.assertEqual(a_numero('IV'), 4)
        self.assertEqual(a_numero('IX'), 9)
        self.assertEqual(a_numero('XL'), 40)
        self.assertEqual(a_numero('XC'), 90)
        self.assertEqual(a_numero('CD'), 400)
        self.assertEqual(a_numero('CM'), 900)
        with self.assertRaises(ValueError):
            a_numero('IL')
        with self.assertRaises(ValueError):
            a_numero('IC')
        with self.assertRaises(ValueError):
            a_numero('IM')
        with self.assertRaises(ValueError):
            a_numero('XM')
        with self.assertRaises(ValueError):
            a_numero('XD')
        
    def test_no_mas_de_tres_repeticiones(self):
        self.assertEqual(a_numero('III'), 3)
        self.assertEqual(a_numero('XXXIII'), 33)
        
        with self.assertRaises(ValueError):
            a_numero('IIII')
        
    def test_no_restas_dos_iguales(self):
        with self.assertRaises(ValueError):
            a_numero('CCM')
        with self.assertRaises(ValueError):
            a_numero('IIX')

    def test_no_restas_consecutivas(self):
        with self.assertRaises(ValueError):
            a_numero('MIXC')

    def test_no_repeticiones_cincos(self):
        with self.assertRaises(ValueError):
            a_numero('DD')
        with self.assertRaises(ValueError):
            a_numero('MDDLL')
        with self.assertRaises(ValueError):
            a_numero('MDLLL')
