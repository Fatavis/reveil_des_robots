import numpy as np
import heapq 
import time

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

if __name__ == '__main__':
    A = [["R1", 1], ["R2", 1], ["R3", 1], ["R4", 1000]]
    B = [["R0", 1], ["R2", np.sqrt(2)], ["R3", 2], ["R4", 1000]] #value of c bug for 4
    C = [["R0", 1], ["R1", np.sqrt(2)], ["R3", np.sqrt(2)], ["R4", 1001]]
    D = [["R0", 1], ["R1", 2], ["R2", np.sqrt(2)], ["R4", 1000]]
    E = [["R0", 1000], ["R1", 1000], ["R2", 1001], ["R3", 1000]]

    G = [A, B, C, D, E]

    heap = []
    heapq.heapify(heap)
    
    
    total_time = 0
    target_robots = [] #robot vers lesquels on doit se déplacer
    working_robot = [] #robot que l'on doit déplacer
    visited_vertices = [] 
    start_vertice = 0
    visited_vertices.append(G[1][0][0])
    close_vertice = get_closer_vertice(start_vertice, G, target_robots, visited_vertices)
    #working_robot.append("R0")
    target_robots.append(close_vertice[0])
    heapq.heappush(heap, close_vertice)
    #working_robot.pop()
    #working_robot.append(target_robots)


    while (len(visited_vertices) < len(G)):
        print("New turn")
        element = heapq.heappop(heap)
        print(element)
        target_robots.remove(element[0])
        print("visited vertices", visited_vertices)
        visited_vertices.append(element[0])
        total_time += element[1]
        update_heap(heap, element)
        close_vertice = get_closer_vertice(int(element[0][1]), G, target_robots, visited_vertices)
        print(close_vertice)
        far_vertice = get_far_vertice(int(element[0][1]), G, target_robots, visited_vertices)
        print(far_vertice)
        if (close_vertice):
            target_robots.append(close_vertice[0])
            heapq.heappush(heap, close_vertice)
        if (far_vertice):
            target_robots.append(far_vertice[0])
            heapq.heappush(heap, far_vertice)
        time.sleep(1)
    
    print("Le temps total est : ", total_time)