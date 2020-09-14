import csv
import numpy as np
from matplotlib import pyplot as plt
import wx


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



wx.App()
nom_fichier_csv = wx.FileSelector("Fichier de données")
with open(nom_fichier_csv,'r') as fichier:
    tableur = csv.DictReader(fichier)
    tableau =[]
    for ligne in tableur:
        tableau.append([float(ligne['Time (s)']), float(ligne['Linear Acceleration x (m/s^2)'])])
    for ligne in tableau:
        print(ligne)
    plt.title('Graphe du fichier mon_fichier.csv')
    x = np.array(tableau)
    stat_x = stat_tableau(x)
    # affichage pour y
    affiche_stat(stat_x, "l'accelération")
    plt.plot(x[:,0],x[:,1],color='r', label=nom_fichier_csv)
    plt.xlabel(tableur.fieldnames[0])
    plt.ylabel(tableur.fieldnames[1])
    # ajout d'une légende pour identifier la courbe
    plt.hlines(stat_x[0], np.min(x), np.max(x),
              colors='red', linestyles='dashed')
    plt.hlines(stat_x[1], np.min(x), np.max(x),
              colors='red', linestyles='dotted')
    plt.legend(['acc', 'moyenne', 'ecart type'])
    plt.grid()
    plt.show()
