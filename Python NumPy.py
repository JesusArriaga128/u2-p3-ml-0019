# Array indexing in NumPy
# Jesus Arriaga 0019
import numpy as np

n0019 = np.array([10, 20, 30, 40, 50])
print(n0019)
print(n0019[0])
print(n0019[3])
print(n0019[-1])
print(n0019[-2])
print("----------------------------------------")
n0019 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(n0019)
print(n0019[0, 0])
print(n0019[1, 2])
print(n0019[-1, -1])
print(n0019[-2, -2])
print("----------------------------------------")
# 3D array 2x(2x3)
n0019 = np.array([
    # 0 -2
    [
        [10, 20, 30],
        [40, 50, 60]
    ],
    # 1 -1
    [
        [70, 80, 90],
        [100, 110, 120]
    ]
])
print(n0019)
print(n0019[0, 0, 0])
print(n0019[1, 1, 2])
print(n0019[-1, -1, -2])
print("Jesus Arriaga 0019")