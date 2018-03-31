from dictionaryDt import dictionary
import csv

theDict = dictionary("theDict")

with open('dictionary/dictionary.csv', 'r', encoding='utf8',errors='ignore') as csvfile:		#Opening up dictionary
    read = csv.reader(csvfile, delimiter=',', quotechar='|')
    count = 0
    for row in read:						#Looping through each line in the csv
        key = row[0]
        row.pop(0)
        element = "".join(row)
        element = element.replace("\"","")
        key = key.replace("\"","")
        theDict.put(key,element)
        count += 1
        if count == 100:
            break
def home(response):

    if response[0] == "n":
        word = input("Please enter a word: ")
        definition = input("Please enter a definition: ")
        theDict.put(word,definition)
        print("Definition Added")
        new()

    elif response[0] == "e":
        word= input("Enter word to change definition: ")
        definition= input("Enter new definition: ")
        theDict.update(word,definition)
        new()

    elif response[0] == "s":
        word=input("Enter word to search: ")
        print("")
        result=theDict.get(word)
        for i in range(0,len(result)):
            print(result[i][1]);
            print("")
        if len(result) == 0:
            print("SORRY... no results found")
        print("")
        new()

    elif response[0] == "r":
            word=input("Enter word to remove: ")
            print("")
            theDict.remove(word)
            print("")
            new()

def new():
    response = ["words"]
    print("Welcome to the dictionary!")
    print('Enter "n" to enter new word/definition ')
    print('Enter "e" to edit a definition ')
    print ('Enter "s" to search for a word ')
    print ('Enter "r" to remove a word ')
    response[0] = input("Please enter a letter: ")
    home(response)

new()
