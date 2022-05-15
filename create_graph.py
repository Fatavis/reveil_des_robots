import random 
from pathlib import Path

name_file = input("Nom du fichier (pas besoin de mettre l'extension du fichier): ")
K = int(input("Valeur de K : "))
N = int(input("Valeur de N : "))

possible_coords = [[i,j] for i in range(1, N+1) for j in range(1, N+1)]
coords = random.sample(possible_coords, K+1)

myfile = Path(name_file+".txt")
myfile.touch(exist_ok=True)
with open(name_file+".txt", "a") as file:
    for i in range(K+1):
            if i != 0:
                file.write(f'{i} : ({coords[i][0]},{coords[i][1]})\n')
            else:
                file.write(f'R : ({coords[i][0]},{coords[i][1]})\n')
