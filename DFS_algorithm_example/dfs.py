from collections import deque

graph = {
    'A': ['B', 'G'],
    'B': ['C', 'D', 'E'],
    'C': [],
    'D': [],
    'E': ['F'],
    'F': [],
    'G': ['H'],
    'H': ['I'],
    'I': [],
}

def dfs(graph, node):
    visited = []
    stack = deque()

    visited.append(node)
    stack.append(node)

    while stack:
        s = stack.pop()
        print(s, end=" ")

        for n in reversed(graph[s]):
            if n not in visited:
                visited.append(n)
                stack.append(n)


dfs(graph, 'A')


# OUTPUT:
# A B C D E F G H I 
