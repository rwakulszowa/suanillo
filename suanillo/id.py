class Ctr:
    def __init__(self):
        self.value = 0

    def next(self):
        self.value += 1
        return self.value

_ctr = Ctr()

def make():
    return _ctr.next()