# from collections import deque
#
# seq = deque([0,1])
# n = int(input())
# def fibonachi(seq, num):
#     if num == n:
#         print(seq[-1])
#         return
#     seq.append(seq[0] + seq[-1])
#     seq.popleft()
#     fibonachi(seq, num + 1)
#
#
# fibonachi(seq, 0)

n = int(input())
def fibonachi(num):
    if num <= 1:
        return 1
    return fibonachi(num -1) + fibonachi(num -2)


print(fibonachi(n))