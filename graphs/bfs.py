graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': [],
    'D': [],
    'E': ['F'],
    'F': []
}


def bfs(graph, start_node, final_node):
    visited = []
    queue = []
    visited.append(start_node)
    queue.append(start_node)

    while queue:
        current_node = queue.pop(0)
        print(current_node, end=" ")

        for neighbour in graph[current_node]:
            if neighbour == final_node:
                return True
            elif neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# outputs travers and result of serach
print(bfs(graph, 'A', 'F'))
