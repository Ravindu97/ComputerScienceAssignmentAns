# a) Read ten marks of a student and store it in to a empty list called ‘marks_list’.

import numpy
from statistics import mode

def read_input_marks():

    marks_list = []

    for i in range(10):
        mark = int(input("Enter the marks for subject " + str(i+1) + " : "))
        marks_list.append(mark)

    return marks_list


    

# b) Sort the ‘marks’ list in ascending order.

marks_list= read_input_marks()
#print("marks collected from students : ")
#print(marks_list)
#marks_list.sort()
#print("sorted marks list : ")
#print(marks_list)


# c) Print the total, mean, median and mode element of the ‘marks’ list. (import suitable library to
# calculate mean, median and mode)
"""

def print_info(marks):
    print("******* Statitical Summary *********")
    print("Total : " + str(sum(marks)))
    print("Mean : " + str(numpy.mean(marks)))
    print("Median : " + str(numpy.median(marks)))
    print("Mode : " + str(mode(marks)))
    print("************************************")
    
    
print_info(marks_list)

"""


# d) Create a new list called ‘grade’ with the same size as ‘marks’ and find the grade for each mark and
#insert into ‘grade’ list by using following grade criteria.


def grade(mark):

    grade = ""
    
    if(mark>=80):
        grade = "A"

    elif(mark>=60):
        grade = "B"

    elif(mark>=50):
        grade = "C"

    elif(mark>=30):
        grade = "D"

    else:
        grade = "F"
        
    return grade


def save_grades(mark_list):

    grade_list = []
    for mark in mark_list:
        grade_list.append(grade(mark))

    print(grade_list)
    return grade_list



save_grades(marks_list)







