class Calculadora:
    # doctest para probar si funciona
    """
    >>> Calculadora.__add__(2, 5)
    7
    >>> Calculadora.__sub__(2, 5)
    -3
    >>> Calculadora.__mul__(2, 5)
    10
    >>> Calculadora.__truediv__()(6, 2)
    3.0
    """
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self):
        return self.a + self.b

    def __sub__(self):
        return self.a - self.b

    def __mul__(self):
        return self.a * self.b

    def __truediv__(self):
        return self.a / self.b

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
