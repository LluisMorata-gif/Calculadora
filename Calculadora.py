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

    def suma(x,y):
        return x + y

    def resta(x,y):
        return x - y

    def multiplicacion(x,y):
        return x * y

    def division(x,y):
        return x / y

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
