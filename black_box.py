import unittest


def suma(num_1, num_2):
    """
    docstring
    """
    return num_1 + num_2


class CajaNegratest(unittest.TestCase):
    """
    docstring
    """
    def test_suma(self):
        num_1 = 10
        num_2 = 5

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, 15)

    def test_suma_negativos(self):
        """
        docstring
        """
        num_1 = -4
        num_2 = -6

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, -10)


if __name__ == "__main__":
    unittest.main()


