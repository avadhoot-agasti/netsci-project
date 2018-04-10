
import subprocess
import json
import os

class Crawler:

    def __init__(self):
        self.dep_json = None
        self.load_results()
        pass

    def generate_deptree(self):
        result = subprocess.check_output(["pipdeptree", "--json-tree"])
        jsonStr = json.loads(result)
        filepath = os.path.join('resources', 'data.txt')
        if not os.path.exists('resources'):
            os.makedirs('resources')
        with open(filepath, 'w+') as outfile:
            json.dump(jsonStr, outfile)

    def load_results(self):
        data = None
        filepath = os.path.join('resources', 'data.txt')
        if not os.path.exists(filepath):
            self.generate_deptree()

        with open (filepath, "r") as myfile:
            data=myfile.read().replace('\n', '')
        self.dep_json = data

    def get_dependency_list(self):
        return self.dep_json

