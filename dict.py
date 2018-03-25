
import csv
from dictionaryDt import dictionary

theDict = dictionary("theDict")

with open('dictionary/dictionary.csv', 'rb') as csvfile:		#Opening up dictionary
	read = csv.reader(csvfile, delimiter=',', quotechar='|')
	count = 0

	for row in read:						#Looping through each line in the csv
		if count == 100:
			break
		key = row[0]
		row.pop(0)
		element = "".join(row)
		element = element.replace("\"","")
		theDict.put(key,element)
		count += 1

with open('dictionary/definitions.csv', 'rb') as csvfile:		#Opening up dictionary
	read = csv.reader(csvfile, delimiter=',', quotechar='|')
	count = 0

	for row in read:						#Looping through each line in the csv
		if count == 100:
			break
		key = row[0]
		row.pop(0)
		element = "".join(row)
		element = element.replace("\"","")
		theDict.update(key,element	)
		count +=1
