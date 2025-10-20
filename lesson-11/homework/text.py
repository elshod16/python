from math_operations import add, subtract, multiply, divide
from string_utils import reverse_string, count_vowels
from geometry.circle import calculate_area, calculate_circumference
from file_operations.file_writer import write_file
from file_operations.file_reader import read_file

# Math operations
print(add(5, 3))
print(subtract(10, 4))
print(multiply(2, 6))
print(divide(8, 2))

# String utils
print(reverse_string("Python"))
print(count_vowels("Data Analytics"))

# Geometry
print(calculate_area(5))
print(calculate_circumference(5))

# File operations
write_file("example.txt", "Hello, this is a test file.")
print(read_file("example.txt"))
