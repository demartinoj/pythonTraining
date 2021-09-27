#this function multiplies all of the numbers given at input 

#declare mul function with numbers input (list)
def mul(numbers):
    holder = int() #declare holder as empty integer var
    maxIndex = len(numbers)-1 #finds the maximum index of numbers list input
    if maxIndex == 1: #if there is only 2 values given:
        holder = numbers[0]*numbers[1] #holder var = to two entries multiplied
    else: #otherwise
        #call for loop iterating over the range of maxIndex
        for i in range(maxIndex):
            if i == 0: #if i is equal to 0
                holder = numbers[i] #set holder var as first entry
            elif i > 0: #otherwise
                holder = holder * numbers[i] #holder is equal to current value of holder multiplied by i
    return holder #return holder var

if __name__ == "__main__":
    assert mul([1, 2, 3]) == 6
    assert mul([0, 1, 2, 3]) == 0
    assert mul([2, 3, 4]) == 24