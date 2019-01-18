#answer is 0.00886031360000012

import numpy as np

start = 2
matrix_size = 3
global answer
answer = 0.0

max_value = 5
center = 1

p_ver = np.array([0.3, 0.5, 0.2])
p_hor = np.array([0.4, 0.4, 0.2])


def isShouldFinish(step, i, j, p):
    if step == 0:
        if i == start and j == start:
            global answer
            answer = answer + p
        return True
    return False


def generateCurrentStepArray(p):
    array = np.ones((matrix_size, matrix_size))
    array = array * p
    array = array.transpose() * p_hor
    array = array.transpose() * p_ver
    return array


def computeNearP(i, j, step, p):
    array = generateCurrentStepArray(p)

    if isShouldFinish(step, i, j, array[center][center]):
        return

    computeNearP(i, j, step - 1, array[center][center])

    if i > 0:
        computeNearP(i - 1, j, step - 1, array[center - 1][center])
        if j > 0:
            computeNearP(i - 1, j - 1, step - 1, array[center - 1][center - 1])
            computeNearP(i, j - 1, step - 1, array[center][center - 1])
        if j < max_value:
            computeNearP(i - 1, j + 1, step - 1, array[center - 1][center + 1])
            computeNearP(i, j + 1, step - 1, array[center][center + 1])
    if i < max_value:
        computeNearP(i + 1, j, step - 1, array[center + 1][center])
        if j > 0:
            computeNearP(i + 1, j - 1, step - 1, array[center + 1][center - 1])
        if j < max_value:
            computeNearP(i + 1, j + 1, step - 1, array[center + 1][center + 1])


computeNearP(start, start, max_value, 1.0)
print(answer)
