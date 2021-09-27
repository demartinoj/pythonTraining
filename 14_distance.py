#this function finds and returns the distance between two farthest apart values

#declare dist function with points input var
def dist(points):
    distlist = points #declare distList var as copy of points input
    minimum = min(distlist) #declare minimum var as smallest value in distList
    maximum = max(distlist) #declare maximum var as largest value in distList 
    solution = abs(maximum - minimum) #declare solution var as the absolute value of maximum - minimum vars
    return solution #return solution var

if __name__ == "__main__":
    assert dist([1, 2, 3]) == 2
    assert dist([1, 2, 3, 2.5]) == 2
    assert dist([1, 2, 3, 2.5, 3.5]) == 2.5
    assert dist([1, 2, 3, 2.5, 3.5, 120]) == 119
    assert dist([1, 2, 3, 2.5, 3.5, 120, -1000]) == 1120