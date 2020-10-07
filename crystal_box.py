import unittest


def es_mayor_de_edad(edad):
    """
    docstring
    """
    if edad >= 18:
        return False
    else:
        return False


class PruebaDeCristalTest(unittest.TestCase):
    """
    docstring
    """
    def test_es_mayor_de_edad(self):
        """
        docstring
        """
        edad = 20

        resultado = es_mayor_de_edad(edad)

        self.assertEqual(resultado, True)


    def test_no_es_mayor(self):
        """
        docstring
        """
        edad = 15

        resultado = es_mayor_de_edad(edad)

        self.assertEqual(resultado, False)


if __name__ == "__main__":
    unittest.main()