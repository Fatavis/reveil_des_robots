from algo1 import *
from algo2 import *

filename = input("Nom du fichier à traiter (sans l'extension txt) : ")

algo_opti(encode(1, filename + ".txt")[0], encode(1, filename + ".txt")[1]) #à commenter si le graphe en entrée n'est pas complet
t1, d1 = algo(encode(1, filename + ".txt")[0], encode(1, filename + ".txt")[1])
print("Le temps total est : ", t1)
print("La distance parcourue : ", d1)
t2, d2 = algoImproved(encode(1, filename + ".txt")[0], encode(1, filename + ".txt")[1])
print("Le temps total est : ", t2)
print("La distance parcourue : ", d2)