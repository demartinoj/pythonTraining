#This script will print the sum of all numbers evenly divisible by 3 and 5 over a range of 0-1000

start = 0 #declare start variable
stop = 1000 #declare stop variable
runninglist = [] #declare runningList variable as empty list

#declare for loop iterating over start-stop range
for i in range(start, stop):
    if (i % 3) == 0: #if i is evenly divisible by 3:
        runninglist.append(i) #add i to runningList list
    elif (i %5) == 0: #if i is evenly divisible by 5:
        runninglist.append(i) #add i to runningList list
    else: #otherwise pass
        pass
    

#declare newList variable as a list of runningList cast as a set
newlist = list(set(runninglist)) 
sumvar = 0 #declare sumvar variable

#declare for loop iterating over newList list
for k in newlist:
    sumvar = sumvar + k #add k to current value of sumvar 
    
print(sumvar) #print sumvar variable