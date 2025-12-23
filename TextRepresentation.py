fruits = ['apple', 'banana', 'orange']
origin = ['India', 'USA', 'Spain']
task = ['classification', 'regression', 'clustering']

def one_hot_encode(categories, item):
    encoding = [0] * len(categories)
    if item in categories:
        index = categories.index(item)
        encoding[index] = 1
    return encoding

# ---- Function calls (IMPORTANT) ----
print("Apple encoding:", one_hot_encode(fruits, 'apple'))
print("Banana encoding:", one_hot_encode(fruits, 'banana'))

print("India encoding:", one_hot_encode(origin, 'India'))
print("Spain encoding:", one_hot_encode(origin, 'Spain'))

print("Classification encoding:", one_hot_encode(task, 'classification'))
print("Clustering encoding:", one_hot_encode(task, 'clustering'))