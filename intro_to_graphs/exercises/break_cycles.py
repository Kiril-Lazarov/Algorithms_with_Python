n = int(input())

graph = {}
edges = []
final_edges = []
for _ in range(n):
    line = input().split(' -> ')
    node = line[0]
    children = line[1].split(' ')
    graph[line[0]] = children
    for child in children:
        edges.append((node, child))


def dfs(node, destination, visited, graph):
    if node in visited:
        return
    visited.append(node)
    if node == destination:
        return

    for child in graph[node]:
        dfs(child, destination, visited, graph)


def path_exists(source, destination, graph):
    visited = []

    dfs(source, destination, visited, graph)
    return destination in visited


for source, destination in sorted(edges, key=lambda x: (x[0], x[1])):
    if destination not in graph[source] or source not in graph[destination]:
        continue

    graph[source].remove(destination)
    graph[destination].remove(source)

    if path_exists(source, destination, graph):
        final_edges.append((source, destination))

    else:
        graph[source].append(destination)
        graph[destination].append(source)

print(f'Edges to remove: {len(final_edges)}')
[print(' - '.join(edge)) for edge in final_edges]
