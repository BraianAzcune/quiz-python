import unittest

class Fraccion:
    def __init__(self, dividendo: int, divisor: int):
        """
        Constructor de la clase Fraccion.
        
        Debe asignar los valores a las propiedades 'dividendo' y 'divisor'.
        Si el divisor es 0, debe lanzar un ZeroDivisionError con el mensaje:
            "El divisor no puede ser cero"
        Consulta la siguiente documentación para aprender sobre excepciones:
        https://ellibrodepython.com/excepciones-try-except-finally
        """
        # Escribe tu código aquí

    def __str__(self) -> str:
        """
        Retorna una cadena que represente la fraccion en el formato "dividendo/divisor".
        """
        # Escribe tu código aquí

    def multiplicar(self, otra: 'Fraccion') -> 'Fraccion':
        """
        Multiplica la fraccion actual por otra fraccion.
        Debe retornar una nueva instancia de Fraccion con el resultado.
        """
        # Escribe tu código aquí

    def dividir(self, otra: 'Fraccion') -> 'Fraccion':
        """
        Divide la fraccion actual por otra fraccion.
        Si la fraccion 'otra' tiene dividendo 0, debe lanzar un ZeroDivisionError con el mensaje:
            "No se puede dividir entre una fraccion con dividendo 0"
        Retorna una nueva instancia de Fraccion con el resultado.
        """
        # Escribe tu código aquí

    def sumar(self, otra: 'Fraccion') -> 'Fraccion':
        """
        Suma la fraccion actual con otra fraccion.
        Debe retornar una nueva instancia de Fraccion con el resultado.
        """
        # Escribe tu código aquí

    def restar(self, otra: 'Fraccion') -> 'Fraccion':
        """
        Resta otra fraccion de la fraccion actual.
        Debe retornar una nueva instancia de Fraccion con el resultado.
        """
        # Escribe tu código aquí

"""
Cuando hayas terminado de implementar la clase Fraccion sin ningún error,
crea un nuevo archivo llamado prueba_fraccion.py que importe la clase Fraccion
y pruebe cada uno de sus métodos.

¿Cómo importar desde otro archivo?
haciendo: from fraccion import Fraccion

"""
class TestFraccion(unittest.TestCase):
    def test_str(self):
        f = Fraccion(3, 4)
        self.assertEqual(str(f), "3/4")

    def test_multiplicar(self):
        f1 = Fraccion(1, 2)
        f2 = Fraccion(3, 4)
        resultado = f1.multiplicar(f2)
        self.assertEqual(resultado.dividendo, 3)
        self.assertEqual(resultado.divisor, 8)

    def test_dividir(self):
        f1 = Fraccion(1, 2)
        f2 = Fraccion(3, 4)
        resultado = f1.dividir(f2)
        # (1/2) / (3/4) = (1*4)/(2*3) = 4/6
        self.assertEqual(resultado.dividendo, 4)
        self.assertEqual(resultado.divisor, 6)

    def test_sumar(self):
        f1 = Fraccion(1, 2)
        f2 = Fraccion(1, 3)
        resultado = f1.sumar(f2)
        # 1/2 + 1/3 = (1*3 + 1*2) / (2*3) = 5/6
        self.assertEqual(resultado.dividendo, 5)
        self.assertEqual(resultado.divisor, 6)

    def test_restar(self):
        f1 = Fraccion(3, 4)
        f2 = Fraccion(1, 4)
        resultado = f1.restar(f2)
        # 3/4 - 1/4 = (3*4 - 1*4) / (4*4) = 8/16
        self.assertEqual(resultado.dividendo, 8)
        self.assertEqual(resultado.divisor, 16)

    def test_divisor_zero(self):
        with self.assertRaises(ZeroDivisionError):
            Fraccion(1, 0)

    def test_dividir_por_fraccion_con_dividendo_cero(self):
        f1 = Fraccion(1, 2)
        f2 = Fraccion(0, 3)
        with self.assertRaises(ZeroDivisionError):
            f1.dividir(f2)

if __name__ == '__main__':
    unittest.main(verbosity=2)
