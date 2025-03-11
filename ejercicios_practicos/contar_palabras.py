import unittest

def contar_palabras(s: str) -> int:
    """
    Dado un string, retorna la cantidad de palabras presentes.
    Se considera palabra cualquier secuencia de caracteres separada por espacios.
    Ejemplos:
        contar_palabras("hola pepe como estas") -> 4
        contar_palabras("    hola    pepe    como    estas    ") -> 4
    """
    # ESCRIBE TU RESPUESTA AQUI
    return 0

class TestContarPalabras(unittest.TestCase):
    def test_regular(self):
        self.assertEqual(contar_palabras("hola pepe como estas"), 4)
    
    def test_with_extra_spaces(self):
        self.assertEqual(contar_palabras("    hola    pepe    como    estas    "), 4)
    
    def test_empty_string(self):
        self.assertEqual(contar_palabras(""), 0)
    
    def test_only_spaces(self):
        self.assertEqual(contar_palabras("     "), 0)
    
    def test_multiple_spaces_between_words(self):
        self.assertEqual(contar_palabras("hello     world"), 2)
    
    def test_single_word(self):
        self.assertEqual(contar_palabras("word"), 1)

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
