
"""
Programme de base pour le TP1a
"""
import doctest


def fct_1(val_x):
    """
    fonction que vous pouvez modifier selon les questions.
    La valeur de retour de la fonction est égal à
    x^2+2x+1
    Argument:
    x -- nombre
    >>> fct_1(3)
    16
    >>> fct_1(-4)
    9
    """
    return val_x ** 2 + 2 * val_x + 1


def fct_2(val_x):
    """
    fonction que vous pouvez modifier selon les questions.
    La valeur de retour de la fonction est égal à
    x^2-2x-1
    Argument:
    x -- nombre
    >>> fct_2(3)
    2
    >>> fct_2(-4)
    23
    """
    return val_x ** 2 - 2 * val_x - 1

doctest.testmod()
x = []
y1 = []
y2 = []
for v in range(-4, 10):
    x.append(v)
    y1.append(fct_1(v))
    y2.append(fct_2(v))
print('Les valeurs de x :', x)
print('les valeurs de fct1(x) : ', y1)
print('les valeurs de fct2(x) : ', y2)
