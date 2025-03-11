import unittest

def str_a_lista_invertida(s: str) -> list:
    """
    Dado un string 's', retorna una lista con las letras en orden inverso.
    Ejemplo:
        str_a_lista_invertida("abc") -> ['c', 'b', 'a']
    """
    # ESCRIBE TU RESPUESTA AQUI
    return []


"""
CODIGO PARA IMPRIMIR MENSAJES DE ERORES, IGNORAR
"""
class TestReverseLetters(unittest.TestCase):
    def test_regular(self):
        self.assertEqual(str_a_lista_invertida("abc"), ['c', 'b', 'a'])

    def test_empty_string(self):
        self.assertEqual(str_a_lista_invertida(""), [])

    def test_single_character(self):
        self.assertEqual(str_a_lista_invertida("x"), ['x'])

    def test_palindrome(self):
        self.assertEqual(str_a_lista_invertida("madam"), ['m', 'a', 'd', 'a', 'm'])

class MinimalTestResult(unittest.TextTestResult):
    def _exc_info_to_string(self, err, test):
        # Retorna solo la primera línea del mensaje de error.
        exctype, excvalue, _ = err
        mensaje = str(excvalue).splitlines()[0]
        return f"{exctype.__name__}: {mensaje}"

    def printErrors(self):
        # Imprime una sola línea por error o fallo.
        for test, err in self.errors:
            self.stream.writeln(f"ERROR: {self.getDescription(test)}: {err.splitlines()[0]}")
        for test, err in self.failures:
            self.stream.writeln(f"FAIL: {self.getDescription(test)}: {err.splitlines()[0]}")

class MinimalTestRunner(unittest.TextTestRunner):
    resultclass = MinimalTestResult

if __name__ == '__main__':
    unittest.main(testRunner=MinimalTestRunner, verbosity=2)
