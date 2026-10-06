def astar(graph, h, start, goal):

    queue = [start]
    g = {start: 0}
    parent = {start: None}

    while queue:

        vertex = queue[0]
        for node in queue:
            if g[node] + h[node] < g[vertex] + h[vertex]:
                vertex = node

        queue.remove(vertex)
        print(str(vertex) + " ", end="")

        if vertex == goal:
            path = []
            while vertex is not None:
                path.append(vertex)
                vertex = parent[vertex]
            path.reverse()
            return path, g[goal]

        for neighbour in graph[vertex]:
            new_cost = g[vertex] + graph[vertex][neighbour]
            if neighbour not in g or new_cost < g[neighbour]:
                g[neighbour] = new_cost
                parent[neighbour] = vertex
                if neighbour not in queue:
                    queue.append(neighbour)

    return None, 0


if __name__ == '__main__':
    graph = {
        'S': {'A': 3, 'B': 2, 'C': 5},
        'A': {'G': 2, 'C': 3},
        'B': {'A': 4, 'D': 6},
        'C': {'B': 4, 'H': 3},
        'H': {'A': 4, 'D': 4},
        'G': {'E': 5, 'D': 4},
        'D': {'E': 2, 'F': 3},
        'E': {'F': 5},
        'F': {}
    }
    h = {'S': 10, 'A': 8, 'B': 9, 'C': 7, 'H': 6, 'G': 6, 'D': 4, 'E': 3, 'F': 0}
    print("Following is A* Search (start S, goal F): ")
    path, cost = astar(graph, h, 'S', 'F')
    print()
    print("Path: " + " -> ".join(path))
    print("Total cost: " + str(cost))