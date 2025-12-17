data = [11,12,13,14,15,16,17]
print(data)
#calculate the mean of the values in data
mean_value = sum(data) / len(data)
print("Mean value:", mean_value)
#calculate the median of the values in data
sorted_data = sorted(data)
n = len(sorted_data)
if n % 2 == 0:
    median_value = (sorted_data[n//2 -1] + sorted_data[n//2])
else:
    median_value = sorted_data[n//2]
print("Median value:", median_value)
#calculate the mode of the values in data
from collections import Counter
data_counter = Counter(data)
mode_value = data_counter.most_common(1)[0][0]
print("Mode value:", mode_value)
#calculate the standard deviation of the values in data
import math
mean_value = sum(data) / len(data)
variance = sum((x - mean_value) ** 2 for x in data) / len(data)
std_deviation = math.sqrt(variance)
print("Standard deviation:", std_deviation)
#use numpy library to caluculate mean
import numpy as np
mean_value = np.mean(data)
print("Mean value:", mean_value)
#sort the list using bubble sort technique median calculation
arr  =[11,12,13,14,15,16,17]
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
sorted_data = bubble_sort(data.copy())
n = len(sorted_data)
if n % 2 == 0:
    median_value = (sorted_data[n//2 -1] + sorted_data[n//2]) / 2
else:
    median_value = sorted_data[n//2]
print("Median value:", median_value)

