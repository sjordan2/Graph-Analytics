from .vertex import Vertex
from .edge import Edge


class Graph:
    def __init__(self, name="None"):
        self.name = name
        self.vertices = []
        self.edges = []

    def __str__(self):
        return "Graph: '{}' \n Vertices: {} \n Edges: {}".format(self.name,
                                                                 [vert.name for vert in self.vertices],
                                                                 [edg.name for edg in self.edges])

    def add_vertex(self, vertex_name):
        if vertex_name not in [vert.name for vert in self.vertices]:
            new_vertex = Vertex(vertex_name)
            self.vertices.append(new_vertex)
        else:
            raise NameError("That vertex name is already in your graph!")

    def add_edge(self, vert_one, vert_two, weight=1.0):
        if vert_one not in [vert.name for vert in self.vertices]:
            raise NameError("Vertex '" + vert_one + "' does not exist in your graph!")
        if vert_two not in [vert.name for vert in self.vertices]:
            raise NameError("Vertex '" + vert_two + "' does not exist in your graph!")
        new_edge = Edge(vert_one, vert_two, weight)
        self.edges.append(new_edge)
