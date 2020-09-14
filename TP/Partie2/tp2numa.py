"""
PExemple d'utilisation des  fonctions np.mean et np.std
"""
import doctest
import numpy as np


def fct_1(val_x):
    """
    fonction que vous pouvez modifier selon les questions.
    La valeur de retour de la fonction est égal à
    x^2+2x+1
    Argument:
    val_x -- nombre
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
    doctest.testmod()
    x = np.arange(0, 10)
    y1 = fct_1(x)
    y2 = fct_2(x)
    print('Les valeurs de x :', x)
    print('les valeurs de fct1(x) : ', y1)
    print('les valeurs de fct2(x) : ', y2)
    moyenne_1 = np.mean(y1)
    ecart_type_1 = np.std(y1)
    min_y_1 = np.min(y1)
    max_y_1 = np.max(y1)
    moyenne_2 = np.mean(y2)
    ecart_type_2 = np.std(y2)
    min_y_2 = np.min(y2)
    max_y_2 = np.max(y2)
    print("La moyenne des valeurs de fct1(x) est ", moyenne_1)
    print("L'écart type des valeurs de fct1(x) est ", ecart_type_1)
    print("Le maximum des valeurs de fct1(x) est ", max_y_1)
    print("Le minimum des valeurs de fct1(x) est ", min_y_1)

    print("La moyenne des valeurs de fct2(x) est ", moyenne_2)
    print("L'écart type des valeurs de fct2(x) est ", ecart_type_2)
    print("Le maximum des valeurs de fct2(x) est ", max_y_2)
    print("Le minimum des valeurs de fct2(x) est ", min_y_2)
