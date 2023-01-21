nums = [int(x) for x in input().split(' ')]
is_swapped = False


def bubble_sort(nums, is_swapped):
    for idx in range(len(nums) - 1):
        if nums[idx + 1] < nums[idx]:
            nums[idx], nums[idx + 1] = nums[idx + 1], nums[idx]
            is_swapped = True
    if is_swapped:
        bubble_sort(nums,is_swapped=False)
    return nums

print(*bubble_sort(nums, is_swapped), sep=' ')
