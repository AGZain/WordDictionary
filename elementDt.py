
class element(object):
    k = ""
    e = ""
    def __init__(self, k, e):
        self.k = k              #Initially setting word
        self.e = e              #Initially setting definations

    def sete(self, e):
        self.e = e              #Updating defination

    def key(self):
        return self.k           #Returns word (useful when searching)

    def gete(self):
        return self.e           #Returns defination
