class Edges:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight


edges = int(input())

graph = []
max_num = float('-inf')

for _ in range(edges):
    first, second, weight = [int(x) for x in input().split(', ')]
    graph.append(Edges(first, second, weight))
    max_num = max(first, second, max_num)
parents = [n for n in range(max_num + 1)]
forest = []


def find_root(parents, node):
    while node != parents[node]:
        node = parents[node]
    return node


for edge in sorted(graph, key=lambda e: e.weight):
    first_node_root = find_root(parents, edge.first)
    second_node_root = find_root(parents, edge.second)
    if first_node_root != second_node_root:
        parents[first_node_root] = second_node_root
        forest.append(edge)

for edge in forest:
    print(f'{edge.first} - {edge.second}')
