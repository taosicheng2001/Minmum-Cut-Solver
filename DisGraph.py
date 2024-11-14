import numpy as np
import graphviz

class DisGraph:
    mesh_nrows = 4
    mesh_ncols = 4
    brs = []
    dis_matrix = np.zeros((4, 4))

    def __init__(self, brs, mesh_nrows = 4, mesh_ncols = 4):
        self.mesh_nrows = mesh_nrows
        self.mesh_ncols = mesh_ncols
        self.brs = brs
        self.dis_matrix = np.full((self.mesh_nrows, self.mesh_ncols), 1000)

    def update_DisGraph(self):
        for br in self.brs:
            x = br[0]
            y = br[1]

            # Initialize Br Distance
            self.dis_matrix[x, y] = 0

        # DFS from each node
        for  node in [ (x,y) for x in range(self.mesh_nrows) for y in range(self.mesh_ncols)]:
            visited_map = np.zeros((self.mesh_nrows, self.mesh_ncols))
            self.DFS(node, visited_map)

        return self.dis_matrix

    def coordinates2indexV(self, vertex):
        return vertex[0] * self.mesh_ncols + vertex[1]

    def get_neighbors(self, node):
        neighbors = []
        x = node[0]
        y = node[1]
        if x > 0:
            neighbors.append((x - 1, y))
        if x < self.mesh_ncols - 1:
            neighbors.append((x + 1, y))
        if y > 0:
            neighbors.append((x, y - 1))
        if y < self.mesh_nrows - 1:
            neighbors.append((x, y + 1))
        return neighbors

    def DFS(self, cur_node, visited_map):

        # Visited Check and Set Visited
        if visited_map[cur_node[0], cur_node[1]] == 1:
            return
        visited_map[cur_node[0], cur_node[1]] = 1

        # Recursive DFS on neighbors
        neighbors = self.get_neighbors(cur_node)
        for neighbor in neighbors:
            if self.dis_matrix[neighbor[0], neighbor[1]] + 1 < self.dis_matrix[cur_node[0], cur_node[1]]:
                self.dis_matrix[cur_node[0], cur_node[1]] = self.dis_matrix[neighbor[0], neighbor[1]] + 1
            self.DFS(neighbor, visited_map)

    def print_DisMatrix(self):
        print(self.dis_matrix)

    def get_dis_sum(self):
        return np.sum(self.dis_matrix)

if __name__ == "__main__":
    DisG = DisGraph([(0, 0), (3,3)])
    DisG.update_DisGraph()
    DisG.print_DisMatrix()
