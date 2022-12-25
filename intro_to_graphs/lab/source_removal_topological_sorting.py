nodes = int(input())
graph = {}
for _ in range(nodes):
    line = input().split('->')
    node, edge = [char.strip() for char in line]
    graph[node] = edge.split(', ') if edge else []
"{'A': ['B, C'], 'B': ['D, E'], 'C': ['F'], 'D': ['C, F'], 'E': ['D'], 'F': []}"




def find_zeroes(graph):
    graph_count_edges = {}
    for node in graph:
        graph_count_edges[node] = 0
        for nodes, edges in graph.items():
            if node != nodes:
                if node in edges:
                    graph_count_edges[node] += 1
    return graph_count_edges


ll = []


def is_node_not_exist_in_other_edges(node, graph):
    for check_node, check_edge in graph.items():
        if node not in check_edge:
            continue
        else:
            return False
    return True



while True:

    if not graph:
        print(f'Topological sorting: {", ".join(ll)}')
        break
    graph_values = find_zeroes(graph)
    if list(graph_values.values()).count(0) == 0:
        print("Invalid topological sorting")
        break

    for node in graph:
        if is_node_not_exist_in_other_edges(node, graph):
            ll.append(node)
            del graph[node]
            break
