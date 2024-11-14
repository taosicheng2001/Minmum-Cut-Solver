import networkx as nx
import graphviz
from myGraphviz import *
import copy
import itertools

class BR:
    n_BR = 4
    mesh_ncols = 4
    mesh_nrows = 4
    candidates = [ (x,y) for x in range(4) for y in range(4) if x*y == 0 or x == 3 or y == 3 ]
    placement = []

    def __init__(self, num, mesh_ncols = 4, mesh_nrows = 4, candidates= []):
        self.n_BR = num
        self.mesh_ncols = 4
        self.mesh_nrows = 4
        self.candidates = candidates if len(candidates) else self.candidates

    def coordinates2indexV(self, vertex):
        return vertex[0] * self.mesh_ncols + vertex[1]

    def coordinates2indexE(self, edge):
        vertex0 = edge[0]
        vertex1 = edge[1]
        return ( self.coordinates2indexV(vertex0), self.coordinates2indexV(vertex1))

    def generate_placement(self):
        placement = []
        placementGraph = []
        combinations = list(itertools.combinations(self.candidates, self.n_BR))

        # Create vertexs and edges for Mesh
        vertexs = [ (x,y) for x in range(4) for y in range(4) ]
        edges = []
        for vertex in vertexs:
            x = vertex[0]
            y = vertex[1]
            if x < self.mesh_ncols - 1:
                edges.append([(x,y), (x+1, y)])
            if y < self.mesh_ncols - 1:
                edges.append([(x,y), (x, y+1)])

        # Create Graph
        BasicG = nx.Graph()
        BasicG.add_nodes_from(self.coordinates2indexV(vertex) for vertex in vertexs)
        BasicG.add_edges_from(self.coordinates2indexE(edge) for edge in edges)

        # extern node for omorphic check
        ext_node = (10,10)

        for combination in combinations:
            cur_G = copy.deepcopy(BasicG)
            cur_G.add_nodes_from([self.coordinates2indexV(ext_node)])
            cur_G.add_edges_from((self.coordinates2indexV(ext_node), self.coordinates2indexV(br)) 
                                 for br in combination)
            # Check generated Graph
            newFlag = True
            for Graph in placementGraph:
                if nx.is_isomorphic(Graph, cur_G):
                    newFlag = False
                    break
            if newFlag:
                placement.append(combination)
                placementGraph.append(cur_G)
        self.placement = placement

if __name__ == "__main__":
    br = BR(4)
    br.generate_placement()
    for i, placement in enumerate(br.placement):
        save_graph(placement, name = str(i), view = False, dir = "./images/placement")
