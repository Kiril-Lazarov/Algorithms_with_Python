count = int(input())


def loops_recursion(loops_list):
    if len(loops_list) == count:
        print(*loops_list, sep=' ')

        return
    for idx in range(1, count + 1):
        loops_list.append(idx)
        loops_recursion(loops_list)
        del loops_list[-1]


loops_recursion([])
