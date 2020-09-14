"""
PExemple d'utilisation des  fonctions np.mean et np.std avec gfx
"""
import doctest
import numpy as np
import matplotlib.pyplot as plt

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
    x = np.arange(-10, 10)
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

    # préparation de la première fenêtre graphique
    # contenant un seul graphique ( une ligne par une colonne)
    fig, ax = plt.subplots(nrows=2, ncols=1)
    fig.tight_layout(h_pad=5, w_pad=5)
    # tracer du graphique
    ax[0].plot(x, y1, marker='o')
    # tracer d'une grille
    ax[0].grid(True)
    # ajout d'un titre pour les ax[0]es x et y et un titre au graphique
    ax[0].set(xlabel='x', ylabel='u.a.',
           title="répartition des points par rapport à la moyenne")
    # ajout d'une légende pour identifier la courbe
    # indice de la position du max[0]imun
    idx_max = np.argmax(y1)
    # indice de la position de l'extremum
    ymin=np.min(y1)
    idx=np.argwhere(y1==ymin)
    # préparation du tracé d'un disque vert de centre x[idx], ymin et de rayon 2
    mon_cercle = plt.Circle((x[idx], ymin), 2, color='green')


    # positionenment du cercle sur le graphique
    ax[0].add_artist(mon_cercle)
    # ajout d'une légende pour identifier la courbe
    ax[0].hlines(moyenne_1, np.min(x), np.max(x),
              colors='red', linestyles='dashed')
    ax[0].hlines(moyenne_1 - ecart_type_1, np.min(x), np.max(x),
              colors='red', linestyles='dotted')
    ax[0].hlines(moyenne_1 + ecart_type_1, np.min(x), np.max(x),
              colors='red', linestyles='dotted',)
    # ajout d'un texte sur le cercle
    ax[0].text(x[idx_max], np.max(y1), 'Maximum')
    ax[0].legend(['y1 fonction de x', 'moyenne', 'm-s', 'm+s'])



    ax[1].plot(x, y2, marker='+')
    # tracer d'une grille
    ax[1].grid(True)
    # ajout d'un titre pour les ax[0]es x et y et un titre au graphique
    ax[1].set(xlabel='x', ylabel='u.a.',
           title="répartition des points par rapport à la moyenne")
    # ajout d'une légende pour identifier la courbe
    # indice de la position du max[0]imun
    ymin=np.min(y2)
    idx=np.argwhere(y2==ymin)
    # préparation du tracé d'un disque vert de centre x[idx], ymin et de rayon 2
    mon_cercle = plt.Circle((x[idx], ymin), 2, color='green')
    # positionenment du cercle sur le graphique
    ax[1].add_artist(mon_cercle)
    # ajout d'une légende pour identifier la courbe
    ax[1].hlines(moyenne_2, np.min(x), np.max(x),
              colors='red', linestyles='dashed')
    ax[1].hlines(moyenne_2 - ecart_type_2, np.min(x), np.max(x),
              colors='red', linestyles='dotted')
    ax[1].hlines(moyenne_2 + ecart_type_2, np.min(x), np.max(x),
              colors='red', linestyles='dotted',)
    # ajout d'un texte sur le cercle
    ax[1].text(x[idx_max], np.max(y2), 'Maximum')
    ax[1].legend(['y2 fonction de x', 'moyenne', 'm-s', 'm+s'])
    plt.show()
