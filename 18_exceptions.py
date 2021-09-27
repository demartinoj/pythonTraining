#this excercise is a brief introduction to exceptions 

#import statements
import sys

#declaration of var1 as return of sys.argv 
var1 = sys.argv

try:
    print(sys.argv[1]) #try to print first element of sys.argv
except IndexError:  #otherwise print error statement if try statement returns IndexError
    print("Not enough parameters.")
    
    
    
    
