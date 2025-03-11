import unittest

def contar_vocales_en_str(s: str) -> int:
    """
    Dado un string, retorna la cantidad de vocales (a, e, i, o, u) presentes.
    Ejemplo:
        contar_vocales_en_str("hola") -> 2
    """
    # ESCRIBE TU RESPUESTA AQUI
    return 0

def contar_vocales_en_lista(lista: list) -> int:
    """
    Dada una lista de caracteres, retorna la cantidad de vocales presentes.
    Ejemplo:
        contar_vocales_en_lista(['h', 'o', 'l', 'a']) -> 2
    """
    # ESCRIBE TU RESPUESTA AQUI
    return 0


"""
CODIGO PARA IMPRIMIR MENSAJES DE ERRORES, IGNORAR
"""
class TestContarVocales(unittest.TestCase):
    def test_contar_vocales_en_str_regular(self):
        self.assertEqual(contar_vocales_en_str("hola"), 2)
    
    def test_contar_vocales_en_str_uppercase(self):
        self.assertEqual(contar_vocales_en_str("AEIOU"), 5)
    
    def test_contar_vocales_en_str_empty(self):
        self.assertEqual(contar_vocales_en_str(""), 0)
    
    def test_contar_vocales_en_str_no_vowels(self):
        self.assertEqual(contar_vocales_en_str("xyz"), 0)
    
    def test_contar_vocales_en_lista_regular(self):
        self.assertEqual(contar_vocales_en_lista(['h', 'o', 'l', 'a']), 2)
    
    def test_contar_vocales_en_lista_uppercase(self):
        self.assertEqual(contar_vocales_en_lista(['A', 'E', 'I', 'O', 'U']), 5)
    
    def test_contar_vocales_en_lista_empty(self):
        self.assertEqual(contar_vocales_en_lista([]), 0)
    
    def test_contar_vocales_en_lista_no_vowels(self):
        self.assertEqual(contar_vocales_en_lista(['x', 'y', 'z']), 0)

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
