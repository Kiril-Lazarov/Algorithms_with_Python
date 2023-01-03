from collections import deque

nodes, edges = int(input()), int(input())

graph = {}

for _ in range(edges):
    node, edge = [int(x) for x in input().split()]
    if node not in graph:
        graph[node] = []
    graph[node].append(edge)
start, end = int(input()), int(input())
# print(graph)
queue = deque()

queue.append(start)
output = []
visited = []
is_found = False
while queue:
    node = queue.pop()
    if node not in visited and node in graph:
        output.append(node)
        visited.append(node)
        for child in graph[node]:
            queue.append(child)
            if child == end:
                is_found = True
                output.append(child)
                break
        if is_found:
            break
print(f'Shortest path length is: {len(output) - 1}')
print(*output, sep=' ')



