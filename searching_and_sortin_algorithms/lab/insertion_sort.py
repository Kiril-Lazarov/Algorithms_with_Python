nums = [int(x) for x in input().split(' ')]
is_swapped = False


def move_num(idx, nums):
    if nums[idx] > nums[idx + 1]:
        nums[idx], nums[idx + 1] = nums[idx + 1], nums[idx]
        if idx - 1 < 0:
            move_num(0, nums)
        else:
            move_num(idx - 1, nums)


def insertion_swap(nums, idx):
    if idx == len(nums) - 1:
        return

    else:
        move_num(idx, nums)
        insertion_swap(nums, idx + 1)
    return nums


print(*insertion_swap(nums, 0), sep=' ')


