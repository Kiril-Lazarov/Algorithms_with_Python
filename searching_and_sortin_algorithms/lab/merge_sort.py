nums = [int(x) for x in input().split(' ')]


def final_merge(left_nums, right_nums):
    result = [None] * (len(left_nums) + len(right_nums))
    left_idx = 0
    right_idx = 0



def merge_sort(nums):
    if len(nums) == 1:
        return nums
    sep_idx = len(nums)//2
    left_nums = nums[:sep_idx]
    merge_sort(left_nums)
    right_nums = nums[sep_idx:]
    merge_sort(right_nums)
    final_merge(merge_sort(left_nums), merge_sort(right_nums))
    return nums






print(merge_sort(nums))