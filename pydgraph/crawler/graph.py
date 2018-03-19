
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.gr = nx.Graph()
        pass

    def add_node(self, name, property=None):
        self.gr.add_node(name)

    def add_edge(self, from_node, to_node, property=None):
        self.gr.add_edge(from_node, to_node)

    def show(self, label=True):
        nx.draw(self.gr, with_labels = label)
        plt.show()

    def test_nx(self):
        # Creates an instance of a networkx graph.
        my_first_graph = nx.Graph()

        # Lets add some nodes to the graph
        my_first_graph.add_node(1)
        my_first_graph.add_node(2)
        my_first_graph.add_node(3)

        # Now lets add some connections
        my_first_graph.add_edge(1, 2)
        my_first_graph.add_edge(3, 2)

        nx.draw(my_first_graph)
        plt.show()