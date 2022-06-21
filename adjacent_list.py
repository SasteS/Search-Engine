class Vertex:
    def __init__(self, lista):
        self.path = lista[0]
        self.dict_ponavljanja = lista[1]
        self.neighbors = list()#lista[2]
	
    def add_neighbor(self, vertex):
        if vertex not in self.neighbors:
            self.neighbors.append((vertex))
            self.neighbors.sort()

class Graph:
    vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.path not in self.vertices:
            self.vertices[vertex.path] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            self.vertices[v].add_neighbor(u)
            return True
        else:
            return False
            
    def print_graph(self):
        for key in self.vertices.keys():
            print(key + "\n" + str(self.vertices[key].dict_ponavljanja) + "\n" + str(self.vertices[key].neighbors))
            print()