nums = [int(x) for x in input().split(' ')]

for idx in range(len(nums) -1):
    curr_num = nums[idx]
    min_num = min(nums[idx+1:])
    min_num_idx = nums[idx+1:].index(min_num) + idx +1
    if min_num < curr_num:
        nums[idx], nums[min_num_idx] = nums[min_num_idx], nums[idx]
print(*nums, sep= ' ')
