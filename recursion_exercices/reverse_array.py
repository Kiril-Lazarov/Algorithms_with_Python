numbers = [int(x) for x in input().split()]


def reverse_array(idx, numbers):
    if idx == len(numbers):
        return
    reverse_array(idx + 1, numbers)
    print(numbers[idx], end=' ')


reverse_array(0, numbers)
