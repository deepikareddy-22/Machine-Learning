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
#use numpy library to caluculate mean
import numpy as np
mean_value = np.mean(data)
print("Mean value:", mean_value)

