from graphanalytics.graph import Graph

if __name__ == '__main__':
    graph = Graph("Test Graph")
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")

    print(graph)
