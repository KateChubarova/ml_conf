import numpy as np

start = 2
matrix_size = 3
global answer
answer = 0.0

max_value = 5
center = 1

p_ver = np.array([0.3, 0.5, 0.2])
p_hor = np.array([0.4, 0.4, 0.2])


def compucateNearP(i, j, value, p):
    array = np.ones((matrix_size, matrix_size))
    array[center][center] = p
    array = array.transpose() * p_hor
    array = array.transpose() * p_ver
    array = array * array[center][center]

    if i == start and j == start and value == 0:
        global answer
        answer = answer + array[center][center]

    if value == 0:
        return

    compucateNearP(i, j, value - 1, array[center][center])

    if i > 0:
        compucateNearP(i - 1, j, value - 1, array[center - 1][center])
        if j > 0:
            compucateNearP(i - 1, j - 1, value - 1, array[center - 1][center - 1])
            compucateNearP(i, j - 1, value - 1, array[center][center - 1])
        if j < max_value:
            compucateNearP(i - 1, j + 1, value - 1, array[center - 1][center + 1])
            compucateNearP(i, j + 1, value - 1, array[center][center + 1])
    if i < max_value:
        if j > 0:
            compucateNearP(i + 1, j - 1, value - 1, array[center + 1][center - 1])
        if j < max_value:
            compucateNearP(i + 1, j + 1, value - 1, array[center + 1][center + 1])


compucateNearP(2, 2, max_value, 1.0)

print(answer)
