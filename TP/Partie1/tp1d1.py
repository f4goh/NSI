"""
Numpy et liste
"""
import doctest
import numpy as np


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

if __name__ == '__main__':
    # test unitaire
    doctest.testmod()
    # création d'un tableau numpy
    # contenant les valeurs de 0 à 10 par pas de 0.5
    x = np.arange(0, 10, 0.5)
    y1 = fct_1(x)
    y2 = fct_2(x)
    # Affichage des valeurs contenues dans les tableaux numpy x et y
    print('Les valeurs de x :', x)
    print('les valeurs de fct1(x) : ', y1)
    print('les valeurs de fct2(x) : ', y2)
    # type des varaibles x et y
    print("Le type de x est : ", type(x))
    print("Le type de y1 est : ", type(y1))
    print("Le type de y2 est : ", type(y2))
    # Dimension des tableaux numpy x et y
    print("Dimension d'un tableaux = nombre d'éléments dans un tableau")
    print('La dimension du tableau numpy x :', x.shape)
    print('La dimension du tableau numpy y1 :', y1.shape)
    print('La dimension du tableau numpy y2 :', y2.shape)
