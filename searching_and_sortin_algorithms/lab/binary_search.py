sequence = [int(x) for x in input().split(' ')]
target = int(input())


def binary_search():
    left = 0
    right = len(sequence) - 1
    if not sequence[left] <= target <= sequence[right]:
        return -1

    while True:
        mid_index = (left + right) // 2
        if sequence[left] <= target < sequence[mid_index]:
            right = mid_index - 1
        elif sequence[mid_index] < target <= sequence[right]:
            left = mid_index + 1
        else:
            break
    return mid_index


print(binary_search())
