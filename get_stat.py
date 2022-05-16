from algo2 import *
from algo1 import *

def calcul_mean(filename : str, algo):
    """
    Display the time and distance mean
    :param vertice: str filename
    :param G: function algo
    """
    total_time_mean = 0
    distance_number_mean = 0
    for k in range(10):
        total_time, distance_number = algo(encode(1, file_name+"_"+str(k)+".txt")[0], encode(1, file_name+"_"+str(k)+".txt")[1])
        total_time_mean += total_time
        distance_number_mean += distance_number
    total_time_mean /= 10
    distance_number_mean /= 10
    print("Le temps moyen sur 10 itérations est de : ", total_time)
    print("Le distance parcourue sur 10 itérations est de : ", distance_number_mean)

if __name__ == '__main__':
    file_name = input("Entrer le nom du fichier de données à lire (sans l'extension .txt): ")
    print("Calcul de la moyenne pour l'algo 1")
    calcul_mean(file_name, algo_opti)
    print("Calcul de la moyenne pour l'algo 2")
    calcul_mean(file_name, algo)
    print("Calcul de la moyenne pour l'algo 2 amélioré")
    calcul_mean(file_name, algoImproved)
