
numbers = [int(x) for x in input().split(' ')]
idx = len(numbers)-1
def calc_sum(numbers, idx):
    if idx == len(numbers) - 1:
        return numbers[idx]
    return numbers[idx] + calc_sum(numbers, idx + 1)
print(calc_sum(numbers, 0))
