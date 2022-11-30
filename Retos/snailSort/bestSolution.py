import numpy as np

array = [[1, 2, 3],
         [8, 9, 4],
         [7, 6, 5]]
m = []
print(array)
array = np.array(array)
print(array)
while len(array) > 0:
    m += array[0].tolist()
    array = np.rot90(array[1:])

print(m)
