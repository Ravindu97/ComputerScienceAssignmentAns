
# computing factorial of a number can be done in two ways:

# 01: Computing Factorial using Recursion

def calculate_factorial(number):

    if(number == 0):
        return 1

    else: return number*calculate_factorial(number-1)


#print(calculate_factorial(4))


    
# 02: Computing Factorail using the Iterative Approach


def calculate_factorial_iterative(number):

    result = 1

    if(number >= 1):

        for i in range(1,number+1):
            result *= i

        return result

    else:
        return "n has to be positive"
        
    
print(calculate_factorial_iterative(1))

