class Log(object):
    def input(self, data):
        raise NotImplementedError

    def output(self, data):
        raise NotImplementedError

    def error(self, data):
        raise NotImplementedError

class Print(Log):
    def input(self, data):
        print("> {}".format(data))

    def output(self, data):
        print("< {}".format(data))

    def error(self, data):
        print("<! {}".format(data))