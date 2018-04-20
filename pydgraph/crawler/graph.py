
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout
import os


class Graph:
    def __init__(self):
        pass

    def init_graph(self):
        self.gr = nx.DiGraph()
        nx.draw(self.gr)

    def add_node(self, name, property=None):
        self.gr.add_node(name)

    def add_edge(self, from_node, to_node):
        self.gr.add_edge(from_node, to_node)

    def draw(self, label=True):
        nx.draw(self.gr, pos=graphviz_layout( self.gr), node_size=200, cmap=plt.cm.Blues, label=True,
                node_color=range(len( self.gr)),
                prog='dot', with_labels = True, font_size=8)
        self.export()
        print(nx.info(self.gr))
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

    def export(self):
        filepath = os.path.join('resources', 'pydgraph.gml')
        if not os.path.exists('resources'):
            os.makedirs('resources')
        print("filepath:", filepath)
        if not os.path.exists(filepath):
            nx.write_gml(self.gr, filepath)
            print("filepath: done")

    def plot_graph(self, node_list):
        # print("node lis: ", node_list)
        self.init_graph()
        for node in node_list:
            self.gr.add_nodes_from(list(node.keys()))
            for key, values in node.items():
                # self.gr.add_node(key)
                for v in values:
                    # print("key: %s, v: %s" %(key, v))
                    self.gr.add_node(v)
                    self.gr.add_edge(v, key)


        self.draw()