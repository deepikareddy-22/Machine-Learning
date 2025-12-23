import random
import matplotlib.pyplot as plt

# 1. Generate a list of random numbers
data = [random.randint(1, 10) for _ in range(100)]

# 2. Calculate frequencies
numbers = sorted(set(data))
frequencies = [data.count(num) for num in numbers]

# 3. Create figure
plt.figure(figsize=(8, 5)) 

# 4. Plot bar graph
plt.bar(numbers, frequencies, label="Random Numbers Frequency")

# 5. Labelling
plt.xlabel("Numbers")
plt.ylabel("Frequency")
plt.title("Frequency Distribution of Random Numbers")

# 6. Legend
plt.legend()

# 7. Display plot
plt.show()
