#this script returns the name of its file

#import statement
import sys


var1 = str(sys.argv) #store the return of sys.argv in var1 
splitvar = var1.split("/") #declare splitvar which houses var1 split on "/" characters
length = len(splitvar) #declare lengthvar = the length of splitvar
print(splitvar[length-1][:-2]) #print statement