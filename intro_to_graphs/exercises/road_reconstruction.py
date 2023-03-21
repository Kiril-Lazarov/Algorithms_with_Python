from collections import deque

buildings_count = int(input())
streets_count = int(input())

graph = {}
edges = []
dots = []
important_streets = []
for _ in range(streets_count):
    street, building = [int(x) for x in input().split(' - ')]
    if street not in graph:
        graph[street] = []
    graph[street].append(building)
    edges.append((street, building))


def dfs(street, visited, temp_removed_edge):

    if street in visited:
        return

    visited.add(street)
    dots.append('*')
    if street in graph:

        for child in graph[street]:

            if (street, child) != temp_removed_edge:
                dfs(child, visited, temp_removed_edge)


def check_streets(temp_removed_edge):
    visited = set()
    child_to_remove = temp_removed_edge[1]
    node_of_child = temp_removed_edge[0]
    child_index = graph[node_of_child].index(child_to_remove)
    graph[node_of_child].remove(child_to_remove)

    for node in graph:


            dfs(node, visited, temp_removed_edge)

    graph[node_of_child].insert(child_index, child_to_remove)
    return len(visited) == len(graph)


for edge in edges:
    if not check_streets(edge):
        important_streets.append(edge)
print(important_streets)





