def has_path(graph, start, end, visited = None):
    if visited is None:
        visited = set()
    if start == end:
        return True
    if start not in graph or start in visited:
        return False

    visited.add(start)

    for neighbor in graph[start]:
        if has_path(graph, neighbor, end, visited):
            return True

    return False

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'F'],
    'C': ['E'],
    'D': [],
    'E': ['F'],
    'F': ['G'],
    'G': []
}

print("A -> E:", has_path(graph, 'A', 'E'))
print("A -> G:", has_path(graph, 'A', 'G'))
print("C -> D:", has_path(graph, 'C', 'D'))
print("E -> G:", has_path(graph, 'E', 'G'))
print("G -> A:", has_path(graph, 'G', 'A'))