from dictionaryDt import dictionary

theDict = dictionary("theDict")

var = 1
while var == 1 :

    print("Welcome to the dictionary!")
    print('Enter "n" to enter new word/definition ')
    print('Enter "e" to edit a definition ')
    print ('Enter "s" to search for a word ')
    response = input("Please enter a letter ")
    print(response)

    if response=="n":
      word = input("Please enter a word")
      definition = input("Please enter a definition")
      theDict.put(word,definition)
        
    elif response=="e":
      word= input("Enter word to change definition")
      definition= input("Enter new definition")
      theDict.update(word,definition)

    elif response=="s":
      word=input("Enter word to search")
      result=theDict.get(word)
      for i in range(0,len(result)):
          print(result[i]);

