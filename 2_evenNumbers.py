#this function prints all even numbers through range of start and stop inputs

#declare print_even_numbers function with start and stop input vars
def print_even_numbers(start, stop):
    #declare for loop iterating over the start-stop range
    for i in range(start, stop): 
        if (i % 2) == 0: #if i is evenly divisible by 2
            print(i) #print i
        else:  #otherwise pass
            pass
            