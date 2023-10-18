#questionone
import math
def degrees_to_radians(degrees):
    radians = degrees * (math.pi / 180)
    return radians
degree = 15
radians = degrees_to_radians(degree)
print(f'Degree: {degree}')
print(f'Radians: {radians}')


#Question two

base_of_parallelogram =float(input('Enter the lenght: '))
height_of_parallelogram =float(input('Enter the height: '))
area = base_of_parallelogram * height_of_parallelogram

# Print the result
print("Area is:", area)

#Question three

import math

def find_smallest_multiple_factors(n):
    factors = []
    smallest_multiple = 1

    for i in range(n, 1, -1):
        if smallest_multiple % i != 0:
            for j in range(2, i + 1):
                if i % j == 0:
                    count_i = 0
                    count_j = 0
                    while i % j == 0:
                        i = i // j
                        count_i += 1
                    while smallest_multiple % j == 0:
                        smallest_multiple = smallest_multiple // j
                        count_j += 1
                    factors.extend([j] * max(count_i - count_j, 0))
            smallest_multiple *= i
    factors.sort(reverse=True)

    return smallest_multiple, factors

n = 13
smallest_multiple, factors = find_smallest_multiple_factors(n)

print("Factors of the smallest multip    le of the first", n, "numbers:")
print(factors)
print("Smallest multiple:", smallest_multiple)


#Question four
import numpy as np

# Create a sample array containing a mix of complex and real numbers
array = np.array([1, 2.5, 3 + 4j, 5, 6 - 2j])

# Check if each element in the array is complex
is_complex = np.iscomplex(array)

# Check if each element in the array is real
is_real = np.isreal(array)

# Check if a given number is of a scalar type
number = 42
is_scalar = np.isscalar(number)


print("Array:")
print(array)
print("Is Complex:")
print(is_complex)
print("Is Real:")
print(is_real)
print(f"{number} is a scalar: {is_scalar}")
