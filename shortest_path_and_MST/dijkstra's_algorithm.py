
from collections import deque
from queue import PriorityQueue


class Dijkstra:
    def __init__(self, node, child, weight):
        self.node = node
        self.child = child
        self.weight = weight


edges = int(input())

graph = {}

for _ in range(edges):
    node, child, weight = (int(x) for x in input().split(', '))
    if node not in graph:
        graph[node] = []
    graph[node].append((child, weight))

start, target = int(input()), int(input())

parents = ['-'] * (max(graph) + 1)
d = [float('inf')] * (max(graph) + 1)

queue = PriorityQueue()
queue.put(list((start, 0)))

while not queue.empty():
    distance, node = queue.get()

    if node == target:
        break
    if node not in graph:
        continue
    for child in graph[node]:
        new_distance = distance + child[1]
        if new_distance < d[child[0]]:
            d[child[0]] = new_distance
            parents[child[0]] = node

            queue.put(list((new_distance, child[0])))

if queue.empty():
    print('There is no such path.')

else:
    end = target
    final = deque()
    while end != start:
        final.appendleft(end)
        new_index = parents[end]
        end = new_index
    final.appendleft(start)
    print(d[target])
    print(' '.join(str(x) for x in list(final)))
