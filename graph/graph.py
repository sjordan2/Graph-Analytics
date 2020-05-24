class Graph:
    def __init__(self, name="None"):
        self.name = name;
        self.vertices = {}
        self.edges = {}

    def __str__(self):
        return "Graph: '{}' \n Vertices: {} \n Edges: {}".format(self.name, self.vertices, self.edges)