#this script should return the circumference of a circle based on the input radius value


#import statement
import math

#declare circle_perimeter function with radius var as input
def circle_perimeter(radius):
    pi = math.pi #declare pi variable
    d = radius*2 #declare diameter variable as diameter of circle formula
    perimeter = pi*d #declare perimiter variable as perimiter formula 
    return perimeter #return perimeter var
    

# You don't need to modify the follwoing part
# it allows you to test your code before submitting it:

if __name__ == "__main__":
    print(circle_perimeter(1))