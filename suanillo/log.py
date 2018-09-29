from collections import defaultdict
import json

from .with_id import WithId

class Log(object):
    def input(self, id, data):
        raise NotImplementedError

    def output(self, id, data):
        raise NotImplementedError

    def error(self, id, data):
        raise NotImplementedError

    def with_id(self, id):
        return WithId(self, id)

class Print(Log):
    def input(self, id, data):
        print("> {}".format(data))

    def output(self, id, data):
        print("< {}".format(data))

    def error(self, id, data):
        print("<! {}".format(data))

class Store(Log):
    def __init__(self):
        self.logs = defaultdict(dict)

    def input(self, id, data):
        self.logs[id]["input"] = data

    def output(self, id, data):
        self.logs[id]["output"] = data

    def error(self, id, data):
        self.logs[id]["error"] = data

    def dumps(self):
        return json.dumps(self.logs, indent=4)