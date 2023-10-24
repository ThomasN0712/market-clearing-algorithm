# Name: Thomas Nguyen
# Date: 10/26/2023
# Assignment: 4 Part 1
# Course: CECS 427

import networkx as nx
from networkx.algorithms import bipartite
import matplotlib.pyplot as plt


def main():
    # user input for numbers of nodes and probability for edges
    n = int(input("Enter the number of nodes: "))
    p = float(input("Enter the probability for edges: "))
    nodes = []

    # Create a bipartite graph
    B = nx.bipartite.random_graph(n, n, p)

    # Separate by group 
    node_attribute = nx.get_node_attributes(B, "bipartite")
    l = [node for node in node_attribute if node_attribute[node] == 0]
    r = [node for node in node_attribute if node_attribute[node] == 1]

    pos = {}
    # Update position for node from each group  !!!!!!!
    pos.update((node, (1, -(index))) for index, node in enumerate(l))
    pos.update((node, (2, -(index))) for index, node in enumerate(r))

    try:
        edge_dict = nx.bipartite.maximum_matching(B)
        print("Perfect matching found.")
        edge_list = [(k, v) for k, v in edge_dict.items()]
        nx.draw(B, pos=pos)
        nx.draw_networkx_edges(B, pos=pos, edgelist=edge_list, width=2, edge_color="green")
        nx.draw_networkx_labels(B, pos=pos)
        plt.show()
    except:        
        print("Graph contain constricted set:")
        # Find node that have no edge connected.
        for node in list(B.nodes()):
            if list(B.edges(node)) == []:
                print("Node ", node, " is not connected to any other nodes.")   

        # Find constricted set by finding if S > N(S)
        S = []
        N_S = []
        for node in r:
            S.append(node)
            for neighbor in list(B.neighbors(node)):
                if neighbor not in N_S:
                    N_S.append(neighbor)
            if len(S) > len(N_S):
                print("Set on the right is constricted.")
            else:
                print("Set on the left is constricted.")
            break
        nx.draw(B, pos=pos)
        nx.draw_networkx_labels(B, pos=pos)
        plt.show()
        
if __name__ == "__main__":
    main()
