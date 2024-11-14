import numpy as np
import graphviz

def coordinates2indexV(vertex, mesh_ncols):
    return vertex[0] * mesh_ncols  + vertex[1]

def save_graph(placement, mesh_ncols = 4, mesh_nrows = 4, name ='squares', view = False, dir = "./images", labels = []):
        dot = graphviz.Graph(format='png')
        normal_style = {
            'shape': 'box',
            'style': 'filled',
            'fillcolor': 'white',
            'fontcolor': 'black',
            'width': '1',
            'height': '1'
        }
        br_style = {
            'shape': 'box',
            'style': 'filled',
            'fillcolor': 'yellow',
            'fontcolor': 'red',
            'width': '1',
            'height': '1'
        }

        for i in range(mesh_ncols):
            with dot.subgraph() as s:
                s.attr(rank="same")
                for j in range(mesh_nrows):
                    cur_coordinate = (i, j)
                    node_name = str(coordinates2indexV(cur_coordinate, mesh_ncols))
                    if cur_coordinate in placement:
                        s.node(node_name, label=str(labels[i][j]) if len(labels) != 0 else node_name, **br_style)
                    else:
                        s.node(node_name, label=str(labels[i][j]) if len(labels) != 0 else node_name, **normal_style)

                    if i < mesh_ncols - 1:
                        dot.edge(node_name, str(coordinates2indexV((i+1,j), mesh_ncols)))
                    if j < mesh_nrows - 1:
                        dot.edge(node_name, str(coordinates2indexV((i,j+1), mesh_ncols)))

        dot.render(name, view = view, directory = dir)
