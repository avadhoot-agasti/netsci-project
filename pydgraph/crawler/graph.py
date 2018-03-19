
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        pass

    def init_graph(self):
        self.gr = nx.Graph()

    def add_node(self, name, property=None):
        self.gr.add_node(name)

    def add_edge(self, from_node, to_node):
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

    def plot_graph(self, node_list):
        print("node lis: ", node_list)
        self.init_graph()
        for node in node_list:
            for key, values in node.items():
                self.add_node(key)
                for v in values:
                    e = (key, v)
                    print("key: %s, v: %s" %(key, v))
                    self.add_node(v)
                    self.gr.add_edge(*e)


        self.show()