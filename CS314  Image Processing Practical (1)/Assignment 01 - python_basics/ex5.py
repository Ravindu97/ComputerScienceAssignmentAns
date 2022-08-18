# calculating distance between two points

import math

def calculate_distance(p1,p2):
    return math.sqrt( ((p2[0]-p1[0])**2) + ((p2[1]-p1[1])**2) )

point1 = [4,0]
point2 = [6,6]


print(calculate_distance(point1,point2))

## there is a inbuilt function in python to calculate the distance between two points

print("\nThis was calculated using the math module in python: ")
print(math.dist(point1,point2))
