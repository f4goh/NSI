"""
tp1c2 Programme pour tracer deux graphiques une fenêtre mais séparément
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
    # données pour la courbe 1 et 2
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
    # préparation de la fenêtre graphique
    # contenant deux seul graphique ( deux lignes par une colonne)
    fig, ax = plt.subplots(nrows=2, ncols=1)
    #reglage de l'écartement entre les 2 graphes
    fig.tight_layout(h_pad=5, w_pad=5)
    # tracer de première courbe dans le graphique du haut
    ax[0].plot(x,y1)
    #tracer d'une grille
    ax[0].grid(True)
    #ajout d'un titre pour les axes x et y et un titre au graphique
    ax[0].set(xlabel='x', ylabel='u.a.', title='Mes premiers graphiques avec matplot')
    #ajout d'une légende pour identifier la courbe
    ax[0].legend(['y1 fonction de x'])

    # tracer du graphique
    ax[1].plot(x,y2)
    #tracer d'une grille
    ax[1].grid(True)
    #ajout d'un titre pour les axes x et y et un titre au graphique
    ax[1].set(xlabel='x', ylabel='u.a.', title='Mes premiers graphiques avec matplot')
    #ajout d'une légende pour identifier la courbe
    ax[1].legend(['y2 fonction de x'])
    #les graphiques sont terminés, on les affiche sur l'écran
    plt.show()
