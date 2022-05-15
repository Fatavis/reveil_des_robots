import numpy as np
import heapq 
import time
from encode import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import copy

def get_closer_vertice(vertice : int, G : list, target_robots : list, visited_vertices : list) -> float:
    """
    :param vertice: int current vertice
    :param G: list Graph
    :param target_robots: list Graph
    :return: list ["name of the vertice", distance] close vertice
    """
    i = 0
    while((G[vertice][i][0] in target_robots or G[vertice][i][0] in visited_vertices) and i < len(G[vertice])-1):
        i +=1
    if (i == len(G[vertice])-1 and (G[vertice][i][0] in target_robots or G[vertice][i][0] in visited_vertices)):
        i+=1
    if (len(G[vertice]) == i):
        return None
    else:
        mini = G[vertice][i]
        for s in G[vertice][i:]:
            if s[1] < mini[1] and s[0] not in target_robots and s[0] not in visited_vertices:
                mini = s
        return mini

def get_far_vertice(vertice : int, G : list, target_robots : list, visited_vertices : list) -> float:
    """
    :param vertice: int current vertice
    :param G: list Graph
    :param target_robots: list Graph
    :return: list ["name of the vertice", distance] far vertice
    """
    i = 0
    while((G[vertice][i][0] in target_robots or G[vertice][i][0] in visited_vertices) and i < len(G[vertice])-1):
        i +=1
    if (i == len(G[vertice])-1 and (G[vertice][i][0] in target_robots or G[vertice][i][0] in visited_vertices)):
        i+=1
    if (len(G[vertice]) == i):
        return None
    else:
        maxi = G[vertice][i]
        for s in G[vertice][i:]:
            if s[1] > maxi[1] and s[0] not in target_robots and s[0] not in visited_vertices:
                maxi = s
        return maxi

def update_heap(heap, element):
    """Modifify the distance of vertices by side effect"""
    for elt in heap:
        elt[1] -= element[1]

def separate_point_visited_and_not_visited(G : list, visited_vertices : list, coords : list) -> None:
    visited_coords = []
    not_visited_coords = []
    for vertice in visited_vertices:
        visited_coords.append(coords[int(vertice[1])])
    for c in coords:
        if c not in visited_coords:
            not_visited_coords.append(c)
    return visited_coords, not_visited_coords

def two_random_points(vertice : int, G : list, target_robots : list, visited_vertices : list):
    count = 0 
    i = 0 
    results = []
    while(count < 2 and i < len(G[vertice])-1):
        if G[vertice][i][0] not in target_robots or G[vertice][i][0] not in visited_vertices:
            count += 1
            results.append(G[vertice][i][0])
        i +=1
    return results

def viewer(G : list, coords : list, memory_visited_vertices : list = None) -> None:
    fig = plt.figure()
    x, y = zip(*coords)
    plt.xlim(min(x)-2,max(x)+2)
    plt.ylim(min(y)-2,max(y)+2)
    def animate(i):
        visited_coords, not_visited_coords = separate_point_visited_and_not_visited(G, memory_visited_vertices[i], coords)
        visited_coords_x, visited_coords_y = zip(*visited_coords)
        scat2 = []
        if not_visited_coords:
            not_visited_coords_x, not_visited_coords_y = zip(*not_visited_coords)
            scat2 = plt.scatter(not_visited_coords_x, not_visited_coords_y, color="cyan")
        scat = plt.scatter(visited_coords_x, visited_coords_y, color="red")
        return scat, scat2
    ani = animation.FuncAnimation(fig, animate, frames = len(memory_visited_vertices), repeat = False, interval = 500)
    plt.show()

def algo_opti(G : list, coords : list):
    heap = []
    heapq.heapify(heap)

    total_time = 0
    vertice_count = 0
    target_robots = [] #robot vers lesquels on doit se déplacer
    working_robot = [] #robot que l'on doit déplacer
    visited_vertices = [] 
    memory_of_visited_vertices = []
    start_vertice = 0
    visited_vertices.append(G[1][0][0])
    close_vertice = get_closer_vertice(start_vertice, G, target_robots, visited_vertices)
    target_robots.append(close_vertice[0])
    vertice_count += 1
    heapq.heappush(heap, close_vertice)

    while (len(visited_vertices) < len(G)):
        memory_of_visited_vertices.append(copy.deepcopy(visited_vertices))
        heap = sorted(heap, key = lambda x: x[1])
        element = heapq.heappop(heap)
        vertice_count += 1
        target_robots.remove(element[0])
        if not(element[0] in visited_vertices):
            visited_vertices.append(element[0])
        total_time += element[1]
        close_vertice = get_closer_vertice(int(element[0][1:]), G, target_robots, visited_vertices)
        far_vertice = get_far_vertice(int(element[0][1:]), G, target_robots, visited_vertices)
        #print(close_vertice)
        #print(far_vertice)
        if (close_vertice):
            target_robots.append(close_vertice[0])
            heapq.heappush(heap, close_vertice)
            if (far_vertice) and (far_vertice != close_vertice):
                target_robots.append(far_vertice[0])
                heapq.heappush(heap, far_vertice)
    
    memory_of_visited_vertices.append(visited_vertices)
    #print(memory_of_visited_vertices)
    #viewer(G, coords, memory_of_visited_vertices)
    #print("sorted vertices")
    #print(sorted(visited_vertices))
    print("Le temps total est : ", total_time)
    print("Le nombre de sommets parcourus : ", vertice_count)
    return total_time, vertice_count

def calcul_mean(filename : str):
    total_time_mean = 0
    vertice_number_mean = 0
    for k in range(10):
        total_time, vertice_number = algo_opti(encode(1, file_name)[0], encode(1, file_name)[1])
        total_time_mean += total_time
        vertice_number_mean += vertice_number
    total_time_mean /= 10
    vertice_number_mean /= 10
    print("Le temps moyen sur 10 itérations est de : ", total_time)
    print("Le nombre de sommets sur 10 itérations est de : ", vertice_number_mean)

if __name__ == '__main__':
    A = [["R1", 1], ["R2", 1], ["R3", 1], ["R4", 1000]]
    B = [["R0", 1], ["R2", np.sqrt(2)], ["R3", 2], ["R4", 1000]] #value of c bug for 4
    C = [["R0", 1], ["R1", np.sqrt(2)], ["R3", np.sqrt(2)], ["R4", 1001]]
    D = [["R0", 1], ["R1", 2], ["R2", np.sqrt(2)], ["R4", 1000]]
    E = [["R0", 1000], ["R1", 1000], ["R2", 1001], ["R3", 1000]]

    # A = [["R1", 20], ["R2", 20], ["R3", 20], ["R4", 20]]
    # B = [["R0", 20], ["R2", 32], ["R3", 40], ["R4", 32]] #value of c bug for 4
    # C = [["R0", 20], ["R1", 32], ["R3", 32], ["R4", 40]]
    # D = [["R0", 20], ["R1", 40], ["R2", 32], ["R4", 32]]
    # E = [["R0", 20], ["R1", 40], ["R2", 32], ["R3", 32]]

    G = [A, B, C, D, E]
    # A = [['1', 8.06225774829855], ['2', 16.15549442140351]] 
    # B = [['R', 8.06225774829855], ['2', 22.090722034374522]]
    # C = [['R', 16.15549442140351], ['1', 22.090722034374522]]
    # G = [A, B, C]

    coords = [[0, 0], [0, 1], [-1, 0], [0, -1], [1000, 0]]
    #G = encode(1, "bigtest.txt")[0]
    #viewer(G, encode(1, "bigtest.txt")[1])
    file_name = input("Entrer le nom du fichier de données à lire : ")
    calcul_mean(file_name)


