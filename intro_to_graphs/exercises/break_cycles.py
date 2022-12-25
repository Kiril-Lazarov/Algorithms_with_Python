n = int(input())
graph = {}
erased_values = {}
visited = []
'''{1: [2, 5, 4], 2: [1, 3], 3: [2, 5], 
4: [1], 5: [1, 3], 6: [7, 8], 7: [6, 8], 8: [6, 7]}'''
is_cycle = False
result = {}
def dfs(node, previous_node, check_node):
    if node not in visited:
        visited.append(node)
    for child in graph[node]:
        if child != previous_node:
            if child not in graph[check_node]:
                if child == check_node:
                    if child not in result:
                        # graph[node].remove(child)
                        result[child] = node
                        print(visited)
                        is_cycle = True
                        break
            previous_node = node
            dfs(child, previous_node, check_node)
            break


for _ in range(n):
    key, value = input().split(' -> ')
    graph[key] = value.split()
print(graph)
while True:
    for node in graph:
        previous_node = node
        check_node = node

        dfs(node, previous_node, check_node)
        if is_cycle:
            pass

