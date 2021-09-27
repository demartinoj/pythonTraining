#import statements
import string 

#declare longest_word function with input variable text
#this function should return the longest word in a string input at function call
def longest_word(text):
    var1 = text.split() #declare var1 as the return of split function performed on input var text
    length = len(var1) #declare length variable as lenght of var1 list
    longStr = "" #declare longStr var as empty string

    #call for loop iterating based on length var
    for i in range(length):
        if len(var1[i]) > len(longStr): #if current string is longer than current longStr:
            longStr = var1[i] #set longStr variable as current string
        else: #otherwise pass
            pass
    return(longStr) #return longStr var
            
           
    
if __name__ == "__main__":
    print(longest_word("We want a SHRUBBERY"))
