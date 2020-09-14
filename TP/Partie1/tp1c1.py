"""
TP1c1 courbes supperposées
"""
import doctest
import matplotlib.pyplot as plt

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
    doctest.testmod()
    x = []
    y1 = []
    y2 = []
    for v in range(0, 10):
        x.append(v)
        y1.append(fct_1(v))
        y2.append(fct_2(v))
    print('Les valeurs de x :', x)
    print('les valeurs de fct1(x) : ', y1)
    print('les valeurs de fct2(x) : ', y2)
    # préparation du fenêtre graphique
    # contenant un seul graphique ( une ligne par une colonne)
    fig, ax = plt.subplots(nrows=1, ncols=1)
    # tracer du graphique
    ax.plot(x,y1,marker='+')
    ax.plot(x,y2,marker='+')
    #tracer d'une grille
    ax.grid(True)
    #ajout d'un titre pour les axes x et y et un titre au graphique
    ax.set(xlabel='x', ylabel='u.a.', title='Mon premier graphique avec matplot')
    #ajout d'une légende pour identifier la courbe
    ax.legend(['fct_1(x)','fct_2(x)'])
    #le graphique est terminé, on l'affiche sur l'écran
    plt.show()

