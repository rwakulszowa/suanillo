class WithId:
    def __init__(self, base, id):
        self.base = base
        self.id = id

    def input(self, data):
        return self.base.input(self.id, data)

    def output(self, data):
        return self.base.output(self.id, data)

    def error(self, data):
        return self.base.error(self.id, data)