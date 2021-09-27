#this is a simple script for performing addition

#import statements
import sys

#declare callFunction with arg1 and arg2 input variables
def callFunction(arg1, arg2):
    print(arg1+arg2) #print the sum of arg1 and arg2

inputdata = sys.argv #declare inputdata as return of sys.argv 
inputlength = len(sys.argv) #declare inputLength var as the length of sys.argv

#error handling and write to terminal line 
if inputlength == 1:
    sys.stdout.write("usage: python3 solution.py OP1 OP2")
elif inputlength == 2:
    sys.stdout.write("usage: python3 solution.py OP1 OP2")
else:
    callFunction(int(sys.argv[1]),int(sys.argv[2]))

