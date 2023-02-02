from collections import deque

n = int(input())
p = int(input())

graph = {}

pairs = []
for _ in range(n):
    node, edges = input().split(':')
    if edges:
        graph[int(node)] = [int(x) for x in edges.split(' ')]
    else:
        graph[int(node)] = None
for _ in range(p):
    pairs.append(input())


def bfs(queue, parents, end, visited):
    is_find = False
    while queue:
        node = queue.popleft()
        if node is None:
            continue
        if graph[node] is not None:
            for child in graph[node]:
                if child in visited:
                    continue
                visited.append(child)
                if child not in queue:
                    queue.append(child)
                new_weight = parents[node] + 1
                if child not in parents:
                    parents[child] = parents[node] + 1
                if new_weight < parents[child]:
                    parents[child] = new_weight
                if child == end:
                    is_find = True
                    break
        if is_find:
            return parents[end]
    if not is_find:
        return -1


for pair in pairs:
    start, end = [int(x) for x in pair.split('-')]
    queue = deque()
    queue.append(start)
    parents = {}
    parents[start] = 0
    visited = [start]
    final_value = bfs(queue, parents, end, visited)
    print(f'{{{start, end}}} -> {final_value}')
