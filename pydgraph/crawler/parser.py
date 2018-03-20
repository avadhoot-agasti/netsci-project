
import json

class Parser:
    def __init__(self):
        self.node_list = []
        pass

    def dependency_parser(self, key, values_array):
        deps = {}
        keys = []
        for v in values_array:
            indeps = self.dependency_parser(v['key'], v['dependencies'])
            keys.append(v['key'])
            deps[v['key']] = indeps


        deps[key] = keys
        return deps

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
                # print("key=%s, value=%s" %(keyx, keyy))
                keys.append(keyy)
                indeps = self.dependency_parser(keyy, y['dependencies'])
                deps[keyy] = indeps

            deps[keyx] = keys
            self.node_list.append(deps)

        return self.node_list


    def get_node_list(self):
        return self.node_list


