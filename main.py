from DisGraph import DisGraph
from myGraphviz import *
from BR import BR

if __name__ == "__main__":
    br = BR(4)
    br.generate_placement()

    for placement in br.placement:
        disG = DisGraph(placement)
        disG.update_DisGraph()
        save_graph(placement, name = str(disG.get_dis_sum())+ "_" + str(placement), 
                   dir="./images/dis_graph", labels = disG.dis_matrix)
