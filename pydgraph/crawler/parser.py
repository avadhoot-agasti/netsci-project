
import json

class Parser:
    def __init__(self):
        self.node_list = []
        pass

    def parseDependencies(self, json_string):

        loaded_json = json.loads(json_string)
        for x in loaded_json:
            # print("%s: %d" % (x, loaded_json[x]))
            keyx = x['key']
            deps = {}
            keys = []
            values = x['dependencies']
            for y in values:
                keyy = y['key']
                keys.append(keyy)

            deps[keyx] = keys
            self.node_list.append(deps)

        return self.node_list


    def get_node_list(self):
        return self.node_list


