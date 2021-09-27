#this excercise is to practice sorting lists

#declare sort_a_list function with a_list variable
def sort_a_list(a_list):
    newList = a_list #store copy of a_list as newList var
    newList.sort(reverse=True) #sort entries of newList
    return newList #return newList

#declare sort_by_mark function with my_class variable
def sort_by_mark(my_class):
    classList = my_class #store copy of my_class as classList var
    newClass = [] #declare newClass var as empty string
    #call for loop iterating over classList
    for i in classList:
        newClass.append((i)) #add current i to newClass list
    newClass.sort(reverse=True) #sort newClass list
    return newClass #return newClass

#declare sort_by_name class with my_Class2 variable
def sort_by_name(my_class2):
    newMyClass2 = my_class2 #store copy of my_class2 in newMyClass2 var
    newMyClass2.sort(key= lambda name: name[1]) #sort newMyClass2 list
    return(newMyClass2) #return newMyClass2 

if __name__ == "__main__":
    a_list = [1, 3, 2, 4, 6, 5, 9, 7]
    print(sort_a_list(a_list))