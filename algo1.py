import numpy as np
import heapq 
from encode import *
import copy
from viewer import *

def get_closer_vertice(vertice : int, G : list, target_robots : list, visited_vertices : list) -> list:
    """
    :param vertice: int current vertice
    :param G: list Graph
    :param target_robots: list target for the robots
    :param visited_vertices: list visited vertices
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

def get_far_vertice(vertice : int, G : list, target_robots : list, visited_vertices : list) -> list:
    """
    :param vertice: int current vertice
    :param G: list Graph
    :param target_robots: list target for the robots
    :param visited_vertices: list visited vertices
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

def update_heap(heap, element, distance_count):
    """
    :heap: heapq 
    :param element: list element
    :param distance_count: float distance 
    :return: float distance_count
    """
    for elt in heap:
        elt[1] -= element[1]
        distance_count += element[1]
    return distance_count

def algo_opti(G : list, coords : list) -> tuple:
    """
    :param G: list Graph
    :param coords: list vertices coordinates
    :return: tuple (total_time, distance_count)
    """
    heap = []
    heapq.heapify(heap)

    total_time = 0
    distance_count = 0
    target_robots = [] #robot vers lesquels on doit se déplacer
    working_robot = [] #robot que l'on doit déplacer
    visited_vertices = [] 
    memory_of_visited_vertices = []
    start_vertice = 0
    visited_vertices.append(G[1][0][0])
    close_vertice = get_closer_vertice(start_vertice, G, target_robots, visited_vertices)
    target_robots.append(close_vertice[0])
    heapq.heappush(heap, close_vertice)

    while (len(visited_vertices) < len(G)):
        memory_of_visited_vertices.append(copy.deepcopy(visited_vertices))
        heap = sorted(heap, key = lambda x: x[1])
        element = heapq.heappop(heap)
        distance_count = update_heap(heap, element, distance_count)
        target_robots.remove(element[0])
        if not(element[0] in visited_vertices):
            visited_vertices.append(element[0])
        total_time += element[1]
        distance_count += element[1]
        close_vertice = get_closer_vertice(int(element[0][1:]), G, target_robots, visited_vertices)
        far_vertice = get_far_vertice(int(element[0][1:]), G, target_robots, visited_vertices)
        if (close_vertice):
            target_robots.append(close_vertice[0])
            heapq.heappush(heap, close_vertice)
            if (far_vertice) and (far_vertice != close_vertice):
                target_robots.append(far_vertice[0])
                heapq.heappush(heap, far_vertice)
    
    memory_of_visited_vertices.append(visited_vertices)
    viewer(G, coords, memory_of_visited_vertices)
    print("Le temps total est : ", total_time)
    print("La distance parcourue : ", distance_count)
    return total_time, distance_count

if __name__ == '__main__':
    #Example
    A = [["R1", 1], ["R2", 1], ["R3", 1], ["R4", 100]]
    B = [["R0", 1], ["R2", np.sqrt(2)], ["R3", 2], ["R4", 100]] #value of c bug for 4
    C = [["R0", 1], ["R1", np.sqrt(2)], ["R3", np.sqrt(2)], ["R4", 101]]
    D = [["R0", 1], ["R1", 2], ["R2", np.sqrt(2)], ["R4", 1000]]
    E = [["R0", 100], ["R1", 100], ["R2", 101], ["R3", 100]]

    G = [A, B, C, D, E]

    coords = [[0, 0], [0, 1], [-1, 0], [0, -1], [100, 0]]
    algo_opti(G, coords)


