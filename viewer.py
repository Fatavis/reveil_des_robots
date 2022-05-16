import matplotlib.pyplot as plt
import matplotlib.animation as animation

def separate_point_visited_and_not_visited(G : list, visited_vertices : list, coords : list) -> tuple:
    """
    :param G: list Graph
    :param visited_vertices: list of visited vertices 
    :return: tuple with visited coordinates and not visited coordinates
    """
    visited_coords = []
    not_visited_coords = []
    for vertice in visited_vertices:
        visited_coords.append(coords[int(vertice[1:])])
    for c in coords:
        if c not in visited_coords:
            not_visited_coords.append(c)
    return visited_coords, not_visited_coords

def viewer(G : list, coords : list, memory_visited_vertices : list = None) -> None:
    """
    Display the graph evolution
    :param G: list Graph
    :param memory_visited_vertices: list of list of visited vertices 
    """
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
            scat2 = plt.scatter(not_visited_coords_x, not_visited_coords_y, label="Sommet non visité", color="cyan")
        scat = plt.scatter(visited_coords_x, visited_coords_y, label="Sommet visité", color="red")
        return scat, scat2
    ani = animation.FuncAnimation(fig, animate, frames = len(memory_visited_vertices), repeat = False, interval = 500)
    plt.show()