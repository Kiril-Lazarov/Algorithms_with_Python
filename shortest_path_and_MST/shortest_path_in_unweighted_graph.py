nodes = int(input())
edges = int(input())
graph = []
for i in range(edges):
    destination, source = [int(x) for x in input().split()]
    graph.append((destination, source))
start_point, end_point = int(input()), int(input())


graph_dict = {}
for destination, source in graph:
    if destination not in graph_dict:
        graph_dict[destination] = []
    graph_dict[destination].append(source)

path = []
total_path = []


def dfs(destination):
    if destination not in path:
        path.append(destination)
    for edge in graph_dict[destination]:
        if edge in graph_dict:
            if edge == end_point:
                path.append(edge)
                total_path.append(tuple(path))
                path.pop()
            else:
                dfs(edge)
                path.pop()
        else:
            path.append(edge)
            total_path.append(tuple(path))
            path.pop()



for destination, source in graph_dict.items():
    if destination == start_point:
        dfs(destination)
filtered_path = {}
for paths in total_path:
    if paths[0] == start_point and paths[-1] == end_point:
        filtered_path[len(paths)] = paths

min_value = min(filtered_path.keys())
shortest_path = filtered_path[min_value]
print(f'Shortest path length is: {min_value -1}')
print(' '.join(str(x) for x in filtered_path[min_value]))
