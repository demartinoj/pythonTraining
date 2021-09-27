#this excercise separates students based on a grade threshold given at input

#declare select_student function with students as a list var and threshold as an int input
def select_student(students, threshold):
    #declare mainDict dictionary storing 2 empty lists with keys Accepted and Refused
    mainDict = {'Accepted': [], 'Refused': []}
    studentList = students #store copy of students list in studentList
    thresh = threshold #store copy of threshold input as thresh var

    #call for loop iterating over the length of studentList
    for i in range(len(studentList)):
        if studentList[i][1] >= int(thresh): #if grade attribute of each student is above threshold value
            mainDict['Accepted'] += [studentList[i]] #add student to the accepted list in dictionary
        else: #othewise add student to Refused list in dictionary
            mainDict['Refused'] += [studentList[i]]
    #sort mainDictionary's Accepted list
    mainDict['Accepted'].sort(key = lambda grade: grade[1], reverse = True)
    #sort mainDictionary's Refused list
    mainDict['Refused'].sort(key = lambda grade: grade[1], reverse = False)
    return mainDict #return mainDict dictionary

if __name__ == "__main__":

    assert select_student(
        [
            ["Kermit Wade", 27],
            ["Hattie Schleusner", 67],
            ["Ben Ball", 5],
            ["William Lee", 2],
        ],
        20,
    ) == {
        "Accepted": [["Hattie Schleusner", 67], ["Kermit Wade", 27]],
        "Refused": [["William Lee", 2], ["Ben Ball", 5]],
    }

    assert select_student(
        [
            ["Kermit Wade", 27],
            ["Hattie Schleusner", 67],
            ["Ben Ball", 5],
            ["William Lee", 2],
        ],
        50,
    ) == {
        "Accepted": [["Hattie Schleusner", 67]],
        "Refused": [["William Lee", 2], ["Ben Ball", 5], ["Kermit Wade", 27]],
    }