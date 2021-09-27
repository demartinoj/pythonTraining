#this script will print the sum of all even numbers over the range 0 - 100

start = 0 #declare start variable
stop = 101 #declare stop variable
val = 0 #declare val variable
#for loop iterating over start-stop range
for i in range (start, stop):
    if (i % 2) == 0: #if i is evenly divisible by 2
        val += i  #add to current value of val
    else: #otherwise pass
        pass
    
print(val) #print val variable