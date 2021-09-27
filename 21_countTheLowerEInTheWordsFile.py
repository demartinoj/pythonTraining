#this excercise returns the ammount of times 'e' is found in a input text file called words.txt

file = open('words.txt') #store opened words.txt file in file var
fopen = file.read() #store the contents of file var in fOpen var
fstrip = fopen.split() #store the split contents of fOpen var in fSplit var
count = int() #declare count var as empty integer

#call for loop iterating over fstrip 
for i in fstrip: #for each element in fStrip 
    templist = list(i) #declare tempList as a list of current string
    #call for loop iterating over all leters in tempList
    for letter in templist:
        if letter == 'e': #if current letter is 'e':
            count+= 1 #increment count var by 1
        else: #otherwise pass
            pass
print(count) #print count