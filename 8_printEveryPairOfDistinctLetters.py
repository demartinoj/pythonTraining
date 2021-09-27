#this script returns every 2 letter pair without same letter combinations (i.e.: "AA")

#import statements
import string

letters1 = string.ascii_lowercase #declare letters1 list of all lowercase letters
letters2 = string.ascii_lowercase #declare letters2 list of all lowercase letters
runninglist = [] #declare new blank list called runningList

#call for loop iterating over letters1
for i in letters1:
    #call for loop iterating over letters2
    for j in letters2:
        if i == j: #if i is = to j, pass
            pass
        else:
            var1 = str(i)+str(j) #otherwise store i+j cast as string in var1
            runninglist.append(var1) #append var1 to runningList

finallist = [] #declare new blank list called finalList

#call for loop iterating over runningList
for k in runninglist: 
    if k not in finallist: #if k is not in finalList:
        finallist.append(k) #add k to finalList

for l in finallist:
    print(l) #print each element of finalList
    