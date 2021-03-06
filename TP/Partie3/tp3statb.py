"""
utilisation des fonctions statistiques de numpy
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
    val_x -- nombre
    >>> fct_2(0)
    -1
    >>> fct_2(-3)
    14
    """
    return val_x ** 2 - 2 * val_x - 1


def stat_tableau(tab_x):
    """
    fonction calule la valeur moyenne, l'écart type ,et les extremums du tableau tab_x.
    La valeur de retour de la fonction est égal à la moyenne, l'écart type,
    le minimum et le maximum    x^2-2x-1
    Argument:
    tab_x -- tableau numpy
    >>> stat_tableau(np.array([0,20,40,60]))
    (30.0, 22.360679774997898, 0, 60)
    >>> fct_2(-3)
    14
    """
    return np.mean(tab_x), np.std(tab_x), np.min(tab_x), np.max(tab_x)


def affiche_stat(stat,nom):
    """
    fonction affichage des statistiques
    Argument:
    stat -- tuple des statistiques
    nom -- chaine
    """
    moyenne,ecart_type,min_y,max_y=stat
    print("La moyenne des valeurs de", nom,"est ", moyenne)
    print("L'écart type des valeurs de", nom,"est ", ecart_type)
    print("Le maximum des valeurs de", nom,"est ", max_y)
    print("Le minimum des valeurs de", nom,"est ", min_y)




if __name__ == '__main__':
    doctest.testmod()
    x = np.arange(0, 10)
    y = fct_1(x)
    y2 = fct_2(x)
    # calcul des stat pour y
    print('Les valeurs de x :', x)
    print('les valeurs de fct1(x) : ', y)
    print('les valeurs de fct2(x) : ', y2)
    stat_y = stat_tableau(y)
    # affichage pour y
    affiche_stat(stat_y, "fct1(x)")
    # calcul des stat pour y2
    stat_y2 = stat_tableau(y2)
    # affichage pour y2
    affiche_stat(stat_y2, "fct2(x)")
