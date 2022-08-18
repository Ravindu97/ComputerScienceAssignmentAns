import math


#calclating the area/circumference of the rectangle

def  calculate_area_rectangle(length,breath):
    return length*breath

def calculate_circumference_rectangle(length,breath):
    return 2(length + breath)
    
#calculate the area/circumference of the circle

def calculate_area_Circle(radius):
    return math.pi*(radius**2)

def calculate_circumference_circle(radius):
    return 2*math.pi*radius


#calculate the area/circumference of the traingle

def calcualte_area_triangle(base,height):
    return (base*height)/2


def calculate_circumference_triangle(sidea,sideb,sidec):
    return (sidea+sideb+sidec)

#calculate the area/circumference of the parallelogram

def calculate_area_Parallelogram(base,height):
    return base*height

def calculate_circumference_parallelogram(parrallel_side_a,parrallel_side_b):
    return (parrallel_side_a + parrallel_side_b)*2






