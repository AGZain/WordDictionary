from elementDt import element

class dictionary(object):

	def __init__(self, name):
		self.name = name
		self.wordsList = []
		self.words = []
	def put(self, key, e):
		self.words.append(element(key,e))
	#def get(key):

	#def remove(key):
