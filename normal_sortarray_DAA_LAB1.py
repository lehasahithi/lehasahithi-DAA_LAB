import random
import time

arr = []

print("Enter the size of the array: ")
n = int(input())
for _ in range(n):
    arr.append(random.randint(1, 100))

print("Generated random array: ")
for num in arr:
    print(num)

num_iterations = 100
total_execution_time = 0

for _ in range(num_iterations):
    start_time = time.time()
    arr.sort()
    end_time = time.time()
    total_execution_time += end_time - start_time

average_execution_time = total_execution_time / num_iterations

print("The sorted array using sort method: ")
for num in arr:
    print(num)

print("Average execution time over {} iterations: {:.6f} seconds".format(num_iterations, average_execution_time))
