class Calculadora:
    # doctest para probar si funcona
    """
    >>> Calculadora.suma(2, 5)
    7
    >>> Calculadora.resta(2, 5)
    -3
    >>> Calculadora.multi(2, 5)
    10
    >>> Calculadora.suma(6, 2)
    3
    """

    def suma(x,y):
        return x + y

    def resta(x,y):
        return x - y

    def multi(x,y):
        return x * y

    def division(x,y):
        return x / y

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
