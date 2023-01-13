from collections import deque


class Edges:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


nodes = int(input())
edges = int(input())

graph = []

for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split()]
    graph.append(Edges(source, destination, weight))

source, destination = int(input()), int(input())

distance = [float('inf')] * (nodes + 1)
parent = [None] * (nodes + 1)
distance[source] = 0

for _ in range(nodes - 1):
    for edge in graph:
        if distance[edge.source] == float('inf'):
            continue
        new_distance = distance[edge.source] + edge.weight
        if new_distance < distance[edge.destination]:
            distance[edge.destination] = new_distance
            parent[edge.destination] = edge.source
is_smaller = False
for edge in graph:
    new_distance = distance[edge.source] + edge.weight
    if new_distance < distance[edge.destination]:
        is_smaller = True
        break
if is_smaller:
    print('Negative Cycle Detected')
else:

    end = destination
    final = deque()
    while end != source:
        final.appendleft(end)
        new_end = parent[end]
        end = new_end
    final.appendleft(source)
    print(*final, sep=' ')
    print(distance[destination])
