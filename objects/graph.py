from objects.edge import Edge


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = [list() for _ in range(vertices)]

    def add_edge(self, source, destination, weight):
        edge = Edge(source, destination, weight)
        self.adjacency_list[source].insert(0, edge)

    def print_graph(self):
        for i in range(self.vertices):
            lst = self.adjacency_list[i]
            for j in range(len(lst)):
                print("vertex-" + str(i) + " is connected to " +
                      str(lst[j].destination) + " with weight " + str(lst[j].weight))
