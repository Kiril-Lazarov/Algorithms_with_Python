n = int(input())
graph_dict = {}
max_node = 0
for _ in range(n):
    source, destination, weight = [int(x) for x in input().split(', ')]
    if source not in graph_dict:
        graph_dict[source] = []
    graph_dict[source].append([weight, destination])
    if max_node < source:
        max_node = source

start, end = int(input()), int(input())

destinations = [float('inf')] * (max_node + 1)

path = []
min_path_dict = {}
for node, values in graph_dict.items():
    for items in values:
        weight, destination = items
        if node == start:
            previous_node_path = 0
            if node not in min_path_dict:
                min_path_dict[node] = []

        else:
            if not min_path_dict:
                continue
            previous_node_path = destinations[node]
        if weight + previous_node_path < destinations[destination]:
            destinations[destination] = weight + previous_node_path
            path.append((node, destination))
            if destination not in min_path_dict:
                min_path_dict[destination] = []
            min_path_dict[destination] = min_path_dict[node] + [node]
        if destination == end:
            break

if destinations[end] != float('inf'):
    min_path_dict[end].append(end)
    print(destinations[end])
    print(' '.join([str(x) for x in min_path_dict[end]]))
else:
    print('There is no such path.')
