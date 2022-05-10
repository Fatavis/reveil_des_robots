import numpy as np
import heapq 

A = [["R1", 1], ["R2", 1], ["R3", 1], ["R4", 1000]]
B = [["R0", 1], ["R2", np.sqrt(2)], ["R3", 2], ["R4", 1000]] #value of c bug for 4
C = [["R0", 1], ["R1", np.sqrt(2)], ["R3", np.sqrt(2)], ["R4", 1001]]
D = [["R0", 1], ["R1", 2], ["R2", np.sqrt(2)], ["R4", 1000]]
E = [["R0", 1000], ["R1", 1000], ["R2", 1001], ["R3", 1000]]

G = [A, B, C, D, E]

working_robots = []
moving_robot = []

def get_closer_vertice(vertice : int, G : list) -> float:
    """
    :param vertice: int current vertice
    :param G: list Graph
    :return: list ["name of the vertice", distance] close vertice
    """
    mini = G[vertice][0]
    for s in G[vertice][1:]:
        if s[1] < mini[1]:
            mini = s[1]
    return mini

def get_far_vertice(vertice : int, G : list) -> float:
    """
    :param vertice: int current vertice
    :param G: list Graph
    :return: list ["name of the vertice", distance] far vertice
    """
    maxi = G[vertice][0]
    for s in G[vertice][1:]:
        if s[1] > maxi[1]:
            maxi = s[1]
    return maxi

start_vertice = 0
close_vertice = get_closer_vertice(start_vertice, G)



