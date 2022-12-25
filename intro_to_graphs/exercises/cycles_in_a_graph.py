data = input()
graph = {}
while data != 'End':
    key, value = data.split('-')
    graph[key] = value
    data = input()
is_a_cyclic = False
for key in graph:

    if key in list(graph.values()):

        is_a_cyclic = False
    else:
        is_a_cyclic = True
        break
statement = 'Yes' if is_a_cyclic else 'No'
print(f'Acyclic: {statement}')
