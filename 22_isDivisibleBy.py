#this program finds and prints all numbers between 0 
#and 1000 that are divisible by 7 AND the sum of its 
#digits are divisible by 3

min = int(0) #declare min var as 0
max = int(1000) #declare max var as 1000
divList = [] #create empty list called divList

#call for loop iterating over the range of min-max 
for i in range(min, max):
    if i%7 == False: #if the current number is evenly divisible by 7:
        divList.append(i) #add current number to divList 
    else: #otherwise pass
        pass

tempVar = int() #declare empty integer variable called tempVar
finalList = [] #declare empty list as finalList

#call for loop iterating over the range of divList
for j in divList:
    if len(str(j)) == 0: #if length of current entry in divList is 0
        pass #pass 
    else: #otherwise 
        tempVar = tempVar + j #store sum of all digits in current entry
        if tempVar%3 == False: #check to see if tempVar is evenly divisible by 3
            finalList.append(j) #append current entry
    tempVar = 0 #reset tempVar to 0

for k in finalList: #print each element in finalList
    print(k)
    
