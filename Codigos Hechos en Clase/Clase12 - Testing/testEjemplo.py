import unittest

def contar_caracteres(palabra):
    return len(palabra)

def contar_caracteres2(palabra):
    for i in range(len(palabra)):
        if palabra[-1] == palabra[i]:
            return i + 1
        
class TestContarCaracteres(unittest.TestCase):

    def test_contar_palabra_9_caracteres(self):
        palabra="mercancia"
        resultado = contar_caracteres2(palabra)
        self.assertEqual(resultado, 9)

    def test_contar_caracteres_palabra_vacia(self):
        palabra = ""
        resultado = contar_caracteres(palabra)
        self.assertEqual(resultado, 0)

if __name__ == "__main__":
    unittest.main()