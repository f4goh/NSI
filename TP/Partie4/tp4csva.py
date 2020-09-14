import csv
import numpy as np
from matplotlib import pyplot as plt
import wx

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
    plt.plot(x[:,0],x[:,1],color='r', label=nom_fichier_csv)
    plt.xlabel(tableur.fieldnames[0])
    plt.ylabel(tableur.fieldnames[1])
    plt.grid()
    plt.show()
