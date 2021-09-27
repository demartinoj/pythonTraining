#this script prints the first parameter given to the script

#import statements
import sys

#declare callFunction with arg1 input var
def callFunction(arg1):
    print("arg1 : ", arg1) #print statement

inputdata = sys.argv #declare inputData variable housing the return of sys.argv
inputlength = len(sys.argv) #declare inputLength var = length of sys.argv return

if inputlength == 1: #if inputLength is = 1:
    #readout string to terminal line for error case
    sys.stdout.write("usage: python3 solution.py PARAM")
else:
    print(str(inputdata[1])) #otherwise print current inputData contents
