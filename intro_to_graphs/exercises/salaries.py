n = int(input())
graph = []
for i in range(n):
    graph.append(list(input()))
visited = []

salaries_dict = {}


def dfs(node):
    for child in range(len(graph[node])):
        if graph[node][child] == 'Y':
            if (node, child) in visited:
                continue

            visited.append((node, child))

            dfs(child)
            if node not in salaries_dict:
                salaries_dict[node] = []
            salaries_dict[node].append(child)


for node in range(len(graph)):
    if 'Y' not in graph[node]:
        salaries_dict[node] = []
    else:
        dfs(node)

base_nodes = {}

for node in salaries_dict:
    if not salaries_dict[node]:
        base_nodes[node] = 1

done_nodes = list(base_nodes.keys())


def deep(node):
    if node not in base_nodes:
        base_nodes[node] = 0
    for child in salaries_dict[node]:
        if child in base_nodes:

            base_nodes[node] += base_nodes[child]
        else:

            deep(child)
            done_nodes.append(child)
            base_nodes[node] += base_nodes[child]


for node in salaries_dict:
    if salaries_dict[node]:
        if node not in done_nodes:
            deep(node)

print(sum(list(base_nodes.values())))
