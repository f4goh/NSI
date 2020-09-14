"""
Programme pour tracer deux graphiques dans deux fenetres differentes
"""
import doctest
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    doctest.testmod()
    # données pour la courbe
    x1 = [0, 1, 2, 3]
    y1 = [2, 3, 5, 7]
   # préparation de la première fenêtre graphique
    # contenant un seul graphique ( une ligne par une colonne)
    fig, ax = plt.subplots(nrows=1, ncols=1)
    # tracer du graphique
    ax.plot(x1, y1, marker='o')
    # tracer d'une grille
    ax.grid(True)
    # ajout d'un titre pour les axes x et y et un titre au graphique
    ax.set(xlabel='x', ylabel='u.a.',
           title="tracé et affichage du minimum")
    # ajout d'une légende pour identifier la courbe
    # indice de la position du minimum
    idx_min = np.argmin(y1)
    # préparation du tracé d'un disque vert de centre x1[idx_max], np.max(y1) et de rayon 0.1
    mon_cercle = plt.Circle((x1[idx_min], np.min(y1)), 0.1, color='green')
    # positionenment du cercle sur le graphique
    ax.add_artist(mon_cercle)
    # ajout d'un texte sur le cercle
    ax.text(x1[idx_min], np.min(y1), 'Minimum')
    ax.legend(['y1 fonction de x1'])
    plt.show()
