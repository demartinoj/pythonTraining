#these functions perform celsius to farenheit conversions and viceversa

#declare farenheit_to_celsius function with temp variable input
def fahrenheit_to_celsius(temp):
    cel = (temp -32)/1.8 #declare cel var as converted temp input
    return cel #return cel var

#declare celsius_to_farenheit function with temp variable input
def celsius_to_fahrenheit(temp):
    fer = (temp*1.8)+32 #declar fer var as converted temp input
    return fer #return fer var


if __name__ == "__main__":
    print(celsius_to_fahrenheit(100))
