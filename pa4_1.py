import networkx as nx
from networkx.algorithms import bipartite
import matplotlib.pyplot as plt

def find_constricted_set(graph, left, right):
    """
    Find constricted set in a bipartite graph
    :param graph: bipartite graph
    :param left: left nodes
    :param right: right nodes
    :return: constricted set
    """
    neighbor_node_list = []
    for node in right:
        neighbor_node = [n for n in graph.neighbors(node)]
        print(neighbor_node)
        for node in neighbor_node:
            if node not in neighbor_node_list:
                neighbor_node_list.append(node)
            else:
                continue
    if len(neighbor_node_list) == len(right):
        return neighbor_node_list #None
    else:
        return neighbor_node_list

    # neighbor_node_list = [graph.neighbors(node) for node in right]
    # neighbor_node_list = [node for sublist in neighbor_node_list for node in sublist if node not in neighbor_node_list]
    # return None if len(neighbor_node_list) == len(right) else neighbor_node_list

def main():
    # user input for numbers of nodes and probability for edges
    n = int(input("Enter the number of nodes: "))
    p = float(input("Enter the probability for edges: "))
    nodes = []

    # Create a bipartite graph
    B = nx.bipartite.random_graph(n, n, p, seed=100)  # random graph for probability or gnmk for number of edges

    # Separate by group 
    node_attribute = nx.get_node_attributes(B, "bipartite")
    l = [node for node in node_attribute if node_attribute[node] == 0]
    r = [node for node in node_attribute if node_attribute[node] == 1]

    pos = {}
    # Update position for node from each group  !!!!!!!
    pos.update((node, (1, index)) for index, node in enumerate(l))
    pos.update((node, (2, index)) for index, node in enumerate(r))

    constricted_set = find_constricted_set(B, l, r)
    print("constricted set", constricted_set)

    if constricted_set is None:
        edge_dict = nx.bipartite.maximum_matching(B)
        edge_list = [(k, v) for k, v in edge_dict.items()]
        nx.draw_networkx_edges(B, pos=pos, edgelist=edge_list, width=2, edge_color="green")
    else:
        print("contain constricted set")
        # nx.draw_networkx_edges(B, pos=pos, edgelist=edge_list, width=2, edge_color="green")
        nx.draw_networkx_nodes(B, pos=pos, nodelist=constricted_set, node_color="red")

    nx.draw(B, pos=pos)
    plt.show()

if __name__ == "__main__":
    main()
