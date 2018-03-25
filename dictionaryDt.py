from elementDt import element

class dictionary(object):

	def __init__(self, name):
		self.name = name
		self.wordsList = []
		self.words = []

	def put(self, key, e):
		self.words.append(element(key,e))

	def get(self,key):
		found = False
		results = []
		for i in range(0,len(self.words)):
			if self.words[i].key() == key:
				found = True
				results.append([i, words[i].gete])
		return results

	def remove(self, key):
		for i in range(0,len(self.words)):
			if self.words[i].key() == key:
				self.words.pop(i)
				print("removed")

	def update(self, key, e):
		found = False
		for i in range(0,len(self.words)):
			if self.words[i].key() == key:
				self.words[i].sete(e)
				found = True
