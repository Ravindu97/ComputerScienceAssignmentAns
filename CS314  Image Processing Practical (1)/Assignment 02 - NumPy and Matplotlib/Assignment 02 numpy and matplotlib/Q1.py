import random
import numpy as np  # just to check
import time
import timeit


# Q1 part a.

def generate2D_array(size=5):

    array = []

    for x in range(size):

        array.append([random.randint(0,10) for y in range(size)])

    return array


#generate2D_array()

# Q1 part b.

def generate_identity_matrix(rows,coloumns):

    array = []

    for row in range(rows):
        array.append([0 for coloumn in range(coloumns)])

    
    for row in range(rows):

        for coloumn in range(coloumns):

            if(row == coloumn):
                array[row][coloumn] = 1
    
    print(array)    

#generate_identity_matrix(5,5)

# Q1 part c.

mat_a = generate2D_array(5)
mat_b = generate2D_array(5)



def matrix_multiplication(mat_a,mat_b):

    if(len(mat_b[0]) == len(mat_a)):

        result = np.zeros((5,5))

        for i in range(len(mat_a)):

            for j in range(len(mat_b[0])):

                for k in range(len(mat_b)):
                    result[i][j] += mat_a[i][k] * mat_b[k][j]
            
        print(result)

    else:
        print("Error : invalid operation: The two matrices cannot be multiplied")
        return


#print("multiplication using numpy")

#print(np.multiply(mat_a,mat_b))

start_time = time.time()


#matrix_multiplication(mat_a,mat_b)

end_time = time.time()

#print("Execution time : " + str(end_time-start_time))


#### Caluluating the time using Timeit module

# run same code 5 times to get measurable data
n = 5

# calculate total execution time
result_custom_method = timeit.timeit(stmt='matrix_multiplication(mat_a,mat_b)', globals=globals(), number=n)
result_np_method = timeit.timeit(stmt='matrix_multiplication(mat_a,mat_b)', globals=globals(), number=n)
# calculate the execution time
# get the average execution time
print("Execution time of custom method : " + str(result_custom_method/n) + "seconds")
print("Execution time of np method :  " + str(result_np_method/n) + "seconds")

