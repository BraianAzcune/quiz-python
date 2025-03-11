import unittest

def lista_a_str_normal(lista: list) -> str:
    """
    Dado una lista, retorna un string concatenado.
    Ejemplo:
        lista_a_str_normal(['H', 'o', 'l', 'a']) -> "Hola"
    """
    # ESCRIBE TU RESPUESTA AQUI
    return ""


"""
CODIGO PARA IMPRIMIR MENSAJES DE ERRORES, IGNORAR
"""
class TestListaAString(unittest.TestCase):
    def test_regular(self):
        self.assertEqual(lista_a_str_normal(['H', 'o', 'l', 'a']), "Hola")
    
    def test_empty_list(self):
        self.assertEqual(lista_a_str_normal([]), "")
    
    def test_single_element(self):
        self.assertEqual(lista_a_str_normal(['a']), "a")
    
    def test_words(self):
        self.assertEqual(lista_a_str_normal(['Hello', ' ', 'World']), "Hello World")

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
