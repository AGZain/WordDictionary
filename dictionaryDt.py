from elementDt import element

class dictionary(object):
	name = ""
	wordsList = []
	words = []
	def __init__(self, name):
		self.name = name


	def put(self, key, e):
		newWord = element(key,e)
		self.words.append(newWord)
		

	def get(self,key):
		found = False
		results = []
		for i in range(0,len(self.words)):
			if self.words[i].key() == key:
				found = True
				res = self.words[i].gete()
				results.append([i, res])
		return results

	def remove(self, key):
		for i in range(0,len(self.words)):
			if self.words[i].key() == key:
				self.words.pop(i)
				print("Removed")

	def update(self, key, e):
		found = False
		for i in range(0,len(self.words)):
			if self.words[i].key() == key:
				self.words[i].sete(e)
				print("Updated")
				found = True
