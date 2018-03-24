from elementDt import element

class dictionary(object):

	def __init__(self, name):
		self.name = name
		self.wordsList = []
		self.words = []

	def put(self, key, e):
		self.words.append(element(key,e))

	def get(self,key):
		for word in self.words:
			if word.key() == key:
				print("MATCH FOUND")

	def remove(self, key):
		for i in range(0,len(self.words)):
			if self.words[i].key() == key:
				self.words.pop(i)
				print("removed")
