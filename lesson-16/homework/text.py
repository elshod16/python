import numpy as np

# 1

lst = [12.23, 13.32, 100, 36.32]
arr1 = np.array(lst)
print("Original List:", lst)
print("One-dimensional NumPy array:", arr1)

# 2

arr2 = np.arange(2, 11).reshape(3, 3)
print(arr2)

# 3

arr3 = np.zeros(10)
print(arr3)
arr3[6] = 11
print(arr3)

# 4

arr4 = np.arange(12, 38)
print(arr4)

# 5

arr5 = np.array([1, 2, 3, 4])
arr5 = arr5.astype(float)
print(arr5)

# 6

celsius = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])
fahrenheit = celsius * 9/5 + 32
print("Values in Centigrade degrees:", celsius)
print("Values in Fahrenheit degrees:", fahrenheit)

# 7

arr7 = np.array([10, 20, 30])
arr7 = np.append(arr7, [40, 50, 60, 70, 80, 90])
print(arr7)

# 8

arr8 = np.random.rand(10)
print("mean:", np.mean(arr8))
print("median:", np.median(arr8))
print("std:", np.std(arr8))

# 9

arr9 = np.random.rand(10, 10)
print("min:", np.min(arr9))
print("max:", np.max(arr9))

# 10

arr10 = np.random.rand(3, 3, 3)
print(arr10)
