#this script returns a list of all distinct 2 flavor combinations with no repeating entries

import string #import string
#list of flavors 
FLAVORS = [
    "Banana",
    "Chocolate",
    "Lemon",
    "Pistachio",
    "Raspberry",
    "Strawberry",
    "Vanilla",
]
#copy of list of flavors called flavors2 
FLAVORS2 = FLAVORS
blanklist = [] #blank list 

for i in FLAVORS:#for each item in flavors1
    for k in FLAVORS2:#for each item in flavors2
        string = (i,k) #create a string consisting of each possible flavor combinatio
        if i == k: #finds duplicate combinations (i.e. chocolate,chocolate)
            pass #if duplicate found, skip
        else:
            #add string sorted alphabetically to the blanklist
            blanklist.append(sorted(string))


sortlist = [] #empty list called sortlist
            
for j in blanklist: #for each item in blanklist
    if j in sortlist: #if item is alreayd in sortlist
        pass#skip
    else: 
        sortlist.append(j) #add item to sortlist 
        #print first entry of j, second entry of j (formatting)
        print(j[0]+", "+j[1])
