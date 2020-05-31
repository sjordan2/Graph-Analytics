import Vertex


class Graph:
    def __init__(self, name="None"):
        self.name = name;
        self.vertices = []
        self.edges = []

    def __str__(self):
        return "Graph: '{}' \n Vertices: {} \n Edges: {}".format(self.name, self.vertices, self.edges)

    def add_vertex(self, name):
        if name not in self.vertices.__getattribute__('name'):
            new_vertex = Vertex(name)
            self.vertices.append(new_vertex)
        else:
            raise NameError("That vertex name is already in your graph!")
