nodes = int(input())
graph = []
for _ in range(nodes):
    graph.append([int(x) for x in input().split()])


visited = []


output = []


def dfs(node, visited, graph, output):
    if node in visited:
        return
    visited.append(node)
    for child in graph[node]:
        dfs(child, visited, graph,output)
    output.append(node)


for node in range(len(graph)):
    dfs(node, visited, graph,output)

    if output:
        print(f'Connected component: {" ".join([str(x) for x in output])}')
    output.clear()
