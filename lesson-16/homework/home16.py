import numpy as np


original_list = [12.23, 13.32, 100, 36.32]
array_1d = np.array(original_list)
print("1. One-dimensional NumPy array:", array_1d)


matrix_3x3 = np.arange(2, 11).reshape(3, 3)
print("\n2. 3x3 Matrix from 2 to 10:\n", matrix_3x3)

null_vector = np.zeros(10)
print("\n3. Null vector:", null_vector)
null_vector[6] = 11
print("Updated vector:", null_vector)

array_12_38 = np.arange(12, 38)
print("\n4. Array from 12 to 38:\n", array_12_38)

int_array = np.array([1, 2, 3, 4])
float_array = int_array.astype(float)
print("\n5. Float type array:", float_array)

celsius = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])
fahrenheit = celsius * 9/5 + 32
print("\n6. Values in Centigrade degrees:", celsius)
print("Values in Fahrenheit degrees:", fahrenheit)


original_array = np.array([10, 20, 30])
appended_array = np.append(original_array, [40, 50, 60, 70, 80, 90])
print("\n7. After append:", appended_array)


random_array = np.random.rand(10)
mean_val = np.mean(random_array)
median_val = np.median(random_array)
std_dev = np.std(random_array)
print("\n8. Random Array:", random_array)
print("Mean:", mean_val)
print("Median:", median_val)
print("Standard Deviation:", std_dev)


array_10x10 = np.random.rand(10, 10)
min_val = np.min(array_10x10)
max_val = np.max(array_10x10)
print("\n9. 10x10 Array Min:", min_val)
print("10x10 Array Max:", max_val)

# 10. Create a 3x3x3 array with random values
array_3x3x3 = np.random.rand(3, 3, 3)
print("\n10. 3x3x3 Array:\n", array_3x3x3)
