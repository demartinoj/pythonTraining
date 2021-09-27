#this script prints out the current time and date

#import statements
from datetime import date
from datetime import datetime

date = date.today() #declare date var as return of date.today() function
curr = datetime.now() #declare curr var as return of datetime.now() function
time = curr.strftime("%H:%M:%S.") #declare time variable as string formatted curr var


print("Today is", date, "and it is", time) #print statment