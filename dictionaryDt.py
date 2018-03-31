from elementDt import element
import math

class dictionary(object):
    name = ""
    wordsList = []
    words = []

    def __init__(self, name):
        self.name = name

    def put(self, key, e):
        newWord = element(key,e)

        if len(self.words) == 0 or key < self.words[0].key():
            self.words.insert(0,newWord)
            print("adding")
        elif len(self.words) == 1 and key > self.words[0].key():
            self.words.insert(1,newWord)
        else:
            for i in range(0,len(self.words)-1):
                if self.words[i].key() <= key and self.words[i+1].key() >= key:
                    self.words.insert(i+1,newWord)
                    print(self.words[i+1].key())
                    break

                elif(i == len(self.words)-2):
                    self.words.append(newWord)
                    print(self.words[i+1].key())
        #self.words.append(newWord)


    def get(self,key):

        found = False
        results = []
        f = 0
        l = len(self.words)-1
        found = False
        num = 0
        while f < l:
            num = math.trunc((f + l)/2)
            if self.words[num].key() < key:
                f = math.ceil((f + l)/2)
            elif self.words[num].key() > key:
                l  = math.floor((f + l)/2)
            if self.words[num].key() == key:
                found = True
                res = self.words[num].gete()
                results.append([num,res])
                break

        found = False
        i = 1
        while found == False:
            # print("Foirst: " + str(len(self.words) > num + i) + "also " + str(self.words[num + i].key() == key) + "word is " + self.words[num + i].key())
            # print("search: " + str(-1 < num-i) + "also " +str(self.words[num - i].key() == key) + "word is: " + self.words[num - i].key())
            if ((len(self.words) > num + i and self.words[num + i].key() == key) or (-1 < num-i and self.words[num - i].key() == key)):
                if len(self.words) > num + i and self.words[num + i].key() == key:
                    # if self.words[num + i].key() == key:
                    results.append([num + i,self.words[num+i].gete()])
                if -1 < num-i and self.words[num - i].key() == key:
                    #if self.words[num  - i].key() == key:
                    results.append([num - i,self.words[num-i].gete()])
            else:

                found = True
            i += 1

        return results

    def remove(self, key):
        results = self.get(key)
        leng = len(results)
        i = 0
        while i < leng:
            print(self.words[results[i][0]].key() + "  has been removed")
            self.words.pop(i)
            leng -= 1
            i += 1
        #for i in range(0,len(results)):


    def update(self, key, e):
        results = self.get(key)
        if len(results) != 0:
            print(self.words[results[0][0]].key() + "  has been updated")
            self.words[0].sete(e)
            return(True)
        else:
            #print("Word not found.")
            return(False)
