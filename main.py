from objects.graph import Graph


def main():
    vertices = 6
    graph = Graph(vertices)
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 2, 3)
    graph.add_edge(1, 3, 2)
    graph.add_edge(1, 2, 5)
    graph.add_edge(2, 3, 7)
    graph.add_edge(3, 4, 2)
    graph.add_edge(4, 0, 4)
    graph.add_edge(4, 1, 4)
    graph.add_edge(4, 5, 6)
    graph.print_graph()

if __name__ == "__main__":
    main()

