limit = 2
array = [0] * limit


def vector_gen(idx, array):
    if idx == len(array):
        print(''.join([str(x) for x in array]))
        return
    for num in range(2):
        array[idx] = num

        vector_gen(idx + 1, array)



vector_gen(0, array)
