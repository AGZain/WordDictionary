import csv
from dictionaryDt import dictionary
import time


def addDict(n, theDict):            #getting words from the dictionary
    with open('dictionary/dictionary.csv', 'r', encoding='utf8',errors='ignore') as csvfile:		#Opening up dictionary
        read = csv.reader(csvfile, delimiter=',', quotechar='|')
        count = 0
        for row in read:						#Looping through each line in the csv
            if count == 0:
                print("skipping")
                count += 1
                continue
            if count == n:
                break
            key = row[0]
            row.pop(0)
            element = "".join(row)
            element = element.replace("\"","")
            key = key.replace("\"","")
            result = theDict.get(key)
            if len(result) == 0:
                count += 1
            theDict.put(key,element)


def addDef(n, theDict):                 #Adding definations to the dictionary
    with open('dictionary/definitions.csv', 'r', encoding='utf8',errors='ignore') as csvfile:		#Opening up dictionary
        read = csv.reader(csvfile, delimiter=',', quotechar='|')
        count = 0
        for row in read:						#Looping through each line in the csv
            if count == 0:
                count += 1
                continue
            key = row[0]
            row.pop(0)
            element = "".join(row)
            element = element.replace("\"","")
            key = key.replace("\"","")
            update = theDict.update(key,element)
            if update == True:
                count += 1
            if count == 100:
                break
def searchTxt(n, theDict):                  #Searching for words in the dictionary
    with open('dictionary/words.txt') as wordFile:
        words = wordFile.readlines()
        if n == -1:
            n = len(words)
        for i in range(0,n):
            line = words[i].strip()
            line = line.strip()
            result=theDict.get(line)
            for i in range(0,len(result)):
                print(result[i][1]);
                print("")

def removeWords(n, theDict):            #Removing words from the dictionary
    with open('dictionary/words.txt') as wordFile:
        words = wordFile.readlines()
        if n == -1:
            n = len(words)
        for i in range(0,n):
            line = words[i].strip()
            theDict.remove(line)



def exercise(n):                #calling each function
    theDict = dictionary("theDict")
    addDict(n,theDict)
    addDef(n, theDict)
    searchTxt(n, theDict)
    removeWords(n, theDict)

start_time = time.time()
exercise(100)
exercise(1000)
exercise(2500)
exercise(5000)
exercise(10000)
exercise(-1)
print("--- %s seconds ---" % (time.time() - start_time))
