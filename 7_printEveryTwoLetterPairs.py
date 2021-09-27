#This script prints all 2 letter pair combinations with no repeating entries

#import statements
import string

letters1 = string.ascii_lowercase #declare letters1 list as all lowercase letters
letters2 = string.ascii_lowercase #declare letters2 list as all lowercase letters
runninglist = [] #declare blank list called runningList
finallist = [] #declare blank list called finalList

length = len(letters1) #declare length variable as length of letters1 list

#call for loop iterating over letters1 based on length variable
for i in letters1[0:length]:
    #call for loop iterating over letters2 based on length variable
    for j in letters2[0:length]:
        var1=str(i)+str(j) #declare var1 as the i,j combination cast as a string
        runninglist.append(var1) #append var1 string to runningList 
        

#call for loop iterating over runningList
for k in runninglist:
    if k not in finallist: #if k is not in finalList 
        print(k) #print k


    
    