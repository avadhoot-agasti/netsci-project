import sys
from crawler.crawler import Crawler
from crawler.graph import Graph
from crawler.parser import Parser
import numpy as np
import json

class PyDGraph:
    def __init__(self):
        try:
            self.crawler = Crawler()
            self.pgrpah = Graph()
            self.parser = Parser()
            pass
        except Exception as e:
            print("ERROR " + str(e))
            sys.exit(-1)


    def generate(self):
        print("dependency json: \n",json.dumps(self.crawler.get_dependency_list()))
        nodes = self.parser.parseDependencies(self.crawler.get_dependency_list())
        self.pgrpah.plot_graph(nodes)

def main(argv):
    # My code here
    app = PyDGraph()
    app.generate()

    # app.pgrpah.add_node("six")
    # app.pgrpah.add_node("pyparsing")
    # app.pgrpah.add_edge("six", "pyparsing")
    # app.pgrpah.show()

    pass

if __name__ == "__main__":
    main(sys.argv)