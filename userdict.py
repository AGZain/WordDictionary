from dictionaryDt import dictionary

theDict = dictionary("theDict")

print("Welcome to the dictionary!")
print('Enter "n" to enter new word/definition')
print('Enter "e" to edit a definition')
print ('Enter "s" to search for a word')
response = input("Please enter a letter ")
print(response)

if response=="n":
  word = input("Please enter a word")
  definition = input("Please enter a definition")
	theDict.put(word,definition)
    
else if response=="e":
  word= input("Enter word to change definition")
  definition= input("Enter new definition")
  theDict.update(word,definition)

else if response=="s":
  word=input("Enter word to search")
  theDict.get(word)
  
  
