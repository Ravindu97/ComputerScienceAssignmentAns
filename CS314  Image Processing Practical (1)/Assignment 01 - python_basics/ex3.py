
# there are two ways to compute the fibonacci sequence

# 01: computing using the recursive approach

"""
def fibonacci(number):

    if(number == 0):
        return 0

    if(number == 1):
        return 1

    else:
        return fibonacci(number-2) + fibonacci(number-1)
    
no_of_fibonacci = int(input("Input the number of fibonacci terms required : "))


for i in range(0,no_of_fibonacci+1):
    print(fibonacci(i))
"""


###################################

# 02: Computing fibonacci numbers using the iterative approach

def fibonacii_iterative(number):

    if(number < 1):
        print("Error: Enter an valid number")
        return

    if(number == 1):
        return number

    else:
        left,right = 0,1
        for i in range(2,number+1):
            temp = left + right
            left = right
            right = temp

        return temp


print(fibonacii_iterative(-5))










        

