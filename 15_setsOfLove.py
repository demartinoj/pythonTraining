#this script has 2 portions:
#Portion 1: Returns a list of the same places that bob and alice visit daily to meet
#Portion 2: Returns a list of the places alice can have an affair with silvester with no chance of bob being there. 

def love_meet(bob, alice):
    bobset = set(bob) #set of bob districts
    aliceset = set(alice) #set of alice districts
    crossPaths = set() #creates an empty set
    for i in bobset: #for each item in bobset
        for j in aliceset: #for each item in aliceset
            if i == j: #if item from bobset = item from alice set:
                crossPaths.add(j) #add item to crossPaths set
            else: #otherwise pass
                pass
    return crossPaths #return crossPaths set


def affair_meet(bob, alice, silvester):
    bobset1 = set(bob) #create set of bob
    aliceset1 = set(alice) #create set of alice
    silvesterset1 = set(silvester) #create set of silvester
    removedupes = set() #create empty set of removedupes
    noBob = set() #create empty set called noBob
    cheatList = set() #create empty set called cheatList

    for a in aliceset1: #for each item in aliceset1
        if a not in bobset1:
            removedupes.add(a)

    for i in silvesterset1: #for each item in bobset1:
        if i not in bobset1:
            noBob.add(i)

    for k in noBob: #for each item in aliceset1:
        if k in removedupes:
            cheatList.add(k)
    return cheatList

if __name__ == "__main__":
    assert love_meet(
        ["IV", "III", "II", "XX", "II", "XX"],
        ["II", "IV", "II", "XIX", "XV", "IV", "II"],
    ) == {"II", "IV"}

    assert affair_meet(
        ["IV", "III", "II", "XX", "II", "XX"],
        ["II", "IV", "II", "XIX", "XV", "IV", "II"],
        ["XVIII", "XIX", "III", "I", "III", "XVIII"],
    ) == {"XIX"}