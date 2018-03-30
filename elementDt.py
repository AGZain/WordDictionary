
class element(object):
    k = ""
    e = ""
    def __init__(self, k, e):
        self.k = k
        self.e = e

    def sete(self, e):
        self.e = e

    def key(self):
        return self.k

    def gete(self):
        return self.e
