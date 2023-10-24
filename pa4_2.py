import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite

def main():
    # Open files and read data
    f = open("text.txt", "r")
    lines = f.readlines()

    # Get number of houses
    n = int(lines[0])

    # Get list of the houses intial values
    p_str = lines[1].replace("\n", '').split(",")
    p = [eval(i) for i in p_str]
     
    # Get list of lists of buyers values
    v = []
    for i in range (len(p)):
        v_j_str = lines[i+2].replace("\n", '').split(",")
        v_j = [eval(i) for i in v_j_str]
        v.append(v_j)
    
    iteration = 0
    while(True):
        print("Iteration: ", iteration)
        iteration += 1
        try:
            # Create matrix of prefer values and find the indexes of max numbers using list comprehension
            matrix = [list(v[i][j] - p[j] for j in range(len(p))) for i in range(len(p))]
            prefer_value_index = [list(i for i, x in enumerate(matrix[j]) if x == max(matrix[j])) for j in range(len(p))]

            print("Buyer payoff: ", matrix)
            print("Sellers payoff: ", p)

            # Create graph and add edges
            B = nx.bipartite.random_graph(n, n, 0) 
            edge_list = []
            for i in range(len(p)):
                for j in range(len(prefer_value_index[i])):
                    edge_list.append((i + 3, prefer_value_index[i][j]))
            B.add_edges_from(edge_list)

            # Separate by group 
            node_attribute = nx.get_node_attributes(B, "bipartite")
            l = [node for node in node_attribute if node_attribute[node] == 0]
            r = [node for node in node_attribute if node_attribute[node] == 1]
            
            pos = {}
            # Update position for node from each group
            pos.update((node, (1, -(index))) for index, node in enumerate(l))
            pos.update((node, (2, -(index))) for index, node in enumerate(r))

            # Test for perfect matching
            edge_dict = nx.bipartite.maximum_matching(B)
            print("Perfect matching found.")
            edge_list = [(k, v) for k, v in edge_dict.items()]

            # Draw graph with perfect matching highlighted
            nx.draw_networkx_edges(B, pos=pos, edgelist=edge_list, width=2, edge_color="green")
            nx.draw_networkx_labels(B, pos=pos)
            nx.draw(B, pos=pos)
            plt.show()

            break
        except:
            # Draw graph
            nx.draw_networkx_labels(B, pos=pos)
            nx.draw(B, pos=pos)
            plt.show()

            # Update seller values
            temp_arr = [prefer_value_index[i][j] for i in range(len(prefer_value_index)) for j in range(len(prefer_value_index[i]))]
            for i in range(n):
                if temp_arr.count(i) > 1:
                    p[i] += 1

if __name__ == "__main__":
    main()