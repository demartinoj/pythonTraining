#this excercise performs and returns the following tasks:
    # Student, School, and City have a name attribute, given at initialization time.
    # A Student have an add_exam(mark) method, recording a new mark for him, as a float.
    # A School have an add_student(student) method.
    # A City have an add_school(school) method.
    # Student, School, and City have a get_mean() method giving:
    # For the Student, the average of its results.
    # For the School, the average of the students averages.
    # For the City the average of the School averages.
    # School have a get_best_student() method, returning the best Student.
    # Cities have a get_best_school() and a get_best_student() methods, returning respectively a School and a Student..

#import statements
from statistics import mean

class Student(): #define class Student
    def __init__(self, name): #instantiation of Student Object with name attribute
        self.name = name #stores name attribute
        self.markList = [] #creates markList
        self.meanVal = [] #creates meanVal

    def add_exam(self, mark): #define method add_exam with mark attribute
        self.mark = mark #store mark variable as mark attribute
        self.markList.append(float(self.mark)) #add mark variable to the markList in Student Object (float)

    def get_mean(self): #define method get_mean
        tempMean = mean(self.markList) #create tempMean var which is the mean of the list of marks
        self.meanVal.append(tempMean) #store the mean of markList variable to meanVal list
        return self.meanVal #return the meanVal variable

class School(): #define class School
    def __init__(self, name): #instantiats School Object with name attribute input
        self.name = name #stores name attribute as name var
        self.studentList = [] #creates empty list of students
        self.listOfAverages = []
        self.meanVal = [] #creates meanVal
        self.bestStudent = [] #creates bestStudent
    #Verified Working
    def add_student(self, Student): #defines add_student method with studentName attribute input
        self.studentList.append(Student)

    #verified working
    def get_mean(self): #defines get_mean method
        for i in self.studentList: #for each student in studentList
            self.listOfAverages.append(i.get_mean()) #add the result of get_mean for each student to listOfAverages
        self.meanVal = max(self.listOfAverages) #assign meanVal to the maximum of listOfAverages
        return self.meanVal #return the meanVal

    def get_best_student(self): #defines get_best_student method
        tempStudent = [] #defines temp student variable
        for count, i in enumerate(self.studentList):
            i.get_mean()
            if count == 0:
                self.bestStudent = i
            else:
                if self.bestStudent.meanVal < i.meanVal:
                    self.bestStudent = i
        return self.bestStudent




        #
        #
        # for i in self.studentList:#for each student in student list
        #     i.get_mean()
        #     if len(tempStudent) == 0: #if tempStudent is empty
        #         tempStudent = i #tempStudent = current student object
        #     else: #else
        #         #if the result of current Student.get_mean is greater than tempStudent get_mean result:
        #         if i.meanVal > tempStudent.meanVal:
        #             tempStudent = i #replace previous tempStudent with current Student
        # self.bestStudent = tempStudent #assign bestStudent variable as the tempStudent remaining
        # return self.bestStudent #return bestStudent

class City(): #creates class City
    def __init__(self, name): #instantiates City with name attribute
        self.name = name #stores name input as var
        self.schoolList = [] #create school List var
        self.meanVal = [] #create meanVal list var
        # self.bestSchool = [] #create bestSchool list var
        self.bestStudent = [] #create bestStudent list var

    def add_school(self, School): #define add_school method with school name attribute
        # tempSchool = School(str(schoolName)) #creates a temporary school object with school Name input
        self.schoolList.append(School) #add School object passed in to schoolList
        return(self.schoolList)
        print("added school: ", School.name)

    def get_mean(self): #define get_mean method
        tempSchoolAvgList = [] #create temp School Avg List
        for i in self.schoolList: #for each school in school List
            tempSchoolAvgList.append(i.get_mean()) #add the result of current school get_mean method result to tempSchoolAvgList
        self.meanVal = float(mean(tempSchoolAvgList)) #set self.meanVal to the mean of tempSchoolAvgList
        return self.meanVal #return meanVal (float)


    def get_best_school(self): #define get_best_school method
        tempVar1 = [] #create tempVar1
        # print('before length of tempVar1',len(tempVar1))
        if len(tempVar1) == 0:  # if tempVar1 is empty,
            # print('Bool triggered')
            # tempVar1.append(self.schoolList[:])  # add current school (i) to tempVar1 list
            self.bestSchool = self.schoolList[0]
            # print('after tempVar1 = ', len(tempVar1))
        else:
            for i in self.schoolList: #for each school in School List:
                #if result of get_mean method for student in tempVar1 is less than the get_mean method for current student (i)
                if i.get_mean() > self.bestSchool.get_mean():
                    self.bestSchool = i
        return self.bestSchool #return self.bestSchool

    def get_best_student(self):
        bestie = []
        for i in self.schoolList: #for each school in school List
            if len(bestie) == 0:
                bestie.append(i.get_best_student())
            else:
                if bestie < i.get_best_student():
                    bestie =  i.get_best_student()

         
        self.bestStudent = bestie[0] #store bestie as bestStudent
        return self.bestStudent #return bestStudent




#junk to get it to run test
def main():
    paris = City('paris')
    hkis = School('hkis')
    paris.add_school(hkis)
    for student_name, student_marks in (('alice', (1, 2, 3)),
                                        ('bob', (2, 3, 4)),
                                        ('catherine', (3, 4, 5)),
                                        ('daniel', (4, 5, 6))):
        student = Student(student_name)
        for mark in student_marks:
            student.add_exam(mark)
        hkis.add_student(student)

    #ADDITIONS BY JOE FOR TEST
    # for student in hkis.studentList:
    #     student.get_mean()
    #     print("student average",student.name, student.meanVal)

    print(paris.get_best_school().name)
    print(paris.get_best_student().name)