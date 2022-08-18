import random
import numpy as np

#### part a.

array = [0] * 10 

# print(array)

"""
we can use numpy method
array = np.zeros(10,dtype=int)
"""

#### part b


nump_array = np.array(array)
#print(type(nump_array))


# np.zeros already returns a numpy array object


def generate2D_array(size=5):

    array = []

    for x in range(size):

        array.append([random.random() for y in range(size)])

    return array

generated2D_numpy_array_01 = np.array(generate2D_array())
generated2D_numpy_array_02 = np.array(generate2D_array())

#print(type(generated2D_numpy_array))


#### part c

# numpy matrix multiplication(dot product)

dot_product = np.dot(generated2D_numpy_array_01,generated2D_numpy_array_02)

# comparing custom matrix multiplication runtime and numpy.multiply() method runtime

"""

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

"""



#print(dot_product)

#### part d

# Performing matrix addition and matrix substraction

added_matrix = np.add(generated2D_numpy_array_01,generated2D_numpy_array_02)

#print(added_matrix)

substracted_matrix = np.subtract(generated2D_numpy_array_01,generated2D_numpy_array_02)

#print(substracted_matrix)

#### part e ####

stat_array = np.array([4,7,9,-1,3,5,8])

#print(stat_matrix)

# Maximum of the matrix

max_array = stat_array.max()
#print(max_matrix)

# minimum of a matrix

min_array = stat_array.min()
#print(min_matrix)

# summation of a matrix

sum_array = stat_array.sum()
#print(sum_matrix)

#### part f

# finding the index of the minimum

index_min = np.argmin(stat_array)
#print(index_min)

#### part g

# Create an array(A) which has values starting from 5 to 23 with increments of 2

array_A = np.arange(5,24,2)

#print(array_A)

array_B = np.linspace(5,10,9)

#print(array_B)

#### part i

reshaped_array = array_B.reshape(3,3)

#print(reshaped_array)


#### part j

# finding the cosine of each index of the array(A)

cosine_array_A = np.cos(array_A)

#print(cosine_array_A)

#### part k

# finding the expotential of each index of the array_A

expo_array_A = np.exp(array_A)

#print(expo_array_A)


#### part l

# slicing the array

#print(array_A)

sliced_array = array_A[2:7]

#print(sliced_array)

#### part m

# slicing the reshaped array B ==> display all the values of coloum 1

#print(reshaped_array)

#print(reshaped_array[0:3,0])

#### part n

random_array_A = np.random.rand(4)
random_array_B = np.random.rand(4)

#print(random_array_A)


hstack_array = np.hstack((random_array_A,random_array_B))

#print(hstack_array)

vstack_array = np.vstack((random_array_A,random_array_B))

#print(vstack_array)

#### part 0

# splitting the arrays

#print(hstack_array)

#print("\n\n ******* \n\n")

hsplit_array = np.hsplit(hstack_array,4)

#print(hsplit_array)

# Vsplit()

#print(vstack_array)

vsplit_array = np.vsplit(vstack_array,2)

#print(vsplit_array)
























    


