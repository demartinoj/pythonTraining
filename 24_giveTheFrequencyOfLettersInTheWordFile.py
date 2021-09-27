#This script opens a text file and returns the frequency of each letters'
#occurance based on the percentage of the overall text file length

#import statements
import string

fileName = 'words.txt' #designate file name
file = open(fileName, 'r') #open file and store as file var
readFile = file.read() #read file stored in file var
abcString = string.ascii_lowercase #create string of all ascii lowercase letters
abc = list(abcString) #create list of lowercsae letters

frequency = [] #blank list called frequency
for i in abc: #for each element in abc list
    var = readFile.count(i) #var is the count of how many times element appears in file
    frequency.append([i, var]) #add 2 element array to frequency list

percentage = [] #blank list called perecentage

for letter in frequency: #for each letter in frequency list
    if letter[1] == 0: #if there are 0 occurrances, skip
        pass
    else: #else
        tempvar = float(letter[1]/len(readFile)) #tempVar = percentage of occurance in file
        tempRound = round(tempvar, 2) #round floating point to 2 decimals
        tempFormat = format(tempRound, '.2f') #ensure whole integer formatting to 2 digits precisoin
        tempStr = (str(letter[0] + ": " + str(tempFormat))) #string formatting
        print(tempStr) #print tempStr
