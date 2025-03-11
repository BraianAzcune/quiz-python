import unittest

def sumar_numeros_de_lista(lista: list) -> int:
    """
    Dada una lista de números, retorna la suma de sus elementos.
    Ejemplo:
        sumar_numeros_de_lista([1, 2, 3]) -> 6
    """
    # ESCRIBE TU RESPUESTA AQUI
    return 0

"""
CODIGO PARA IMPRIMIR MENSAJES DE ERRORES, IGNORAR
"""
class TestSumarNumerosDeLista(unittest.TestCase):
    def test_regular(self):
        self.assertEqual(sumar_numeros_de_lista([1, 2, 3]), 6)
    
    def test_empty_list(self):
        self.assertEqual(sumar_numeros_de_lista([]), 0)
    
    def test_negatives(self):
        self.assertEqual(sumar_numeros_de_lista([-1, -2, -3]), -6)
    
    def test_mixed(self):
        self.assertEqual(sumar_numeros_de_lista([1, -2, 3]), 2)

class MinimalTestResult(unittest.TextTestResult):
    def _exc_info_to_string(self, err, test):
        exctype, excvalue, _ = err
        mensaje = str(excvalue).splitlines()[0]
        return f"{exctype.__name__}: {mensaje}"
    
    def printErrors(self):
        for test, err in self.errors:
            self.stream.writeln(f"ERROR: {self.getDescription(test)}: {err.splitlines()[0]}")
        for test, err in self.failures:
            self.stream.writeln(f"FAIL: {self.getDescription(test)}: {err.splitlines()[0]}")

class MinimalTestRunner(unittest.TextTestRunner):
    resultclass = MinimalTestResult

if __name__ == '__main__':
    unittest.main(testRunner=MinimalTestRunner, verbosity=2)
