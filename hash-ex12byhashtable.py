#nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
# What was the average temperature in first week of Jan
# What was the maximum temperature in first 10 days of Jan
# Figure out data structure that is best for this problem

import csv


class HashTable():
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for ch in key:
            hash += ord(ch)
        return hash % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for index, element in enumerate(self.arr[h]):
            if len(element)== 2 and element[0] == key:
                self.arr[h][index] = (key,val)
                found = True
        if not found:
            self.arr[h].append((key, val))   

    def __getitem__(self, key):
        h = self.get_hash(key)
        for kv in self.arr[h]:
            if kv[0] == key:
                return kv[1]

    def delitem(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                print("Deleting ", index)
                del self.arr[h][index] 

def avg_temp(hashT,totaldays):
    summ = 0
    for i in range(totaldays):
        summ += float(t.__getitem__(days[i]))
    return summ/7    

def max_temp(hashT,totaldays):
    listtemp = []
    for i in range(totaldays):
        listtemp.append(int(t.__getitem__(days[i])))
    return max(listtemp)

def find_temp(hashT,day):
    return hashT.__getitem__(day)


if __name__== '__main__':
    t = HashTable()
    with open('hash-ex1.csv', 'r') as f:
        csv_reader = csv.reader(f)
        next(csv_reader)
        days = []
        for row in csv_reader:
            days.append(row[0])
            #print(t.get_hash(row[0]))
            t.__setitem__(row[0], row[1])

    print(t.arr)
    #print(days)

    print(avg_temp(t,7))
    print(max_temp(t,10))
    print(find_temp(t,'Jan 9'))
    print(find_temp(t,'Jan 4'))
   

