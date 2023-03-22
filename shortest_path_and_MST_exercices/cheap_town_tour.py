towns, streets = int(input()), int(input())

parents = []

[parents.append(idx) for idx in range(towns)]

graph = []
fores_edges = []
forest = []
for _ in range(streets):
    first, second, distance = [int(x) for x in input().split(' - ')]
    graph.append((first, second, distance))


def find_root(node, parents):
    while node != parents[node]:
        node = parents[node]
    return node


for edge in sorted(graph, key=lambda x: x[2]):
    first_node_root = find_root(edge[0], parents)
    second_node_root = find_root(edge[1], parents)
    if first_node_root != second_node_root:
        parents[first_node_root] = second_node_root
        forest.append(edge)
total_cost = sum([edge[2] for edge in forest])
print(f'Total cost: {total_cost}')
