class Calculadora:
    # doctest para probar si funciona
    """
    >>> Calculadora.suma(2, 5)
    7
    >>> Calculadora.resta(2, 5)
    -3
    >>> Calculadora.multiplicacion(2, 5)
    10
    >>> Calculadora.division(6, 2)
    3.0
    """

    def __add__(x,y):
        return x + y

    def __sub__(x,y):
        return x - y

    def __mul__(x,y):
        return x * y

    def __truediv__(x,y):
        return x / y

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
