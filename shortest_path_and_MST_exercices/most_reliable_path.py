from collections import deque
from queue import PriorityQueue

n, e = int(input()), int(input())

graph = {}

for _ in range(e):
    first, second, weight = [int(x) for x in input().split()]
    if first not in graph:
        graph[first] = []
    if second not in graph:
        graph[second] = []
    graph[first].append((second, weight))
    graph[second].append((first, weight))

start, end = int(input()), int(input())

weights = [float('-inf')] * (n + 1)
parents = [None] * (n + 1)
queue = PriorityQueue()
queue.put((-100, start))

while not queue.empty():
    queue_weight, node = queue.get()
    queue_weight *= -1
    if node == end:
        break
    if node not in graph:
        continue
    for edges in graph[node]:
        second, weight = edges
        new_weight = (queue_weight / 100) * (weight / 100)
        if new_weight > weights[second]:
            weights[second] = new_weight
            parents[second] = node
            queue.put((-new_weight * 100, second))

print(f'Most reliable path reliability: {weights[end] * 100:.2f}%')
node = end
path = deque()
path.appendleft(node)
while node != start:
    parent = parents[node]
    path.appendleft(parent)
    node = parent

print(' -> '.join(str(x) for x in list(path)))
