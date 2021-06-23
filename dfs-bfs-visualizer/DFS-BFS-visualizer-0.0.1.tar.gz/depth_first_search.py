
def DFS(graph):
    stack = [next(iter(graph))]
    visited = {}
    results = []

    while stack:
        curr = stack[-1]
        for node in nodes_list[curr]:
            if node not in visited:
                visited[node] = True
                stack.append(node)
                break
            if nodes_list[curr][-1] == node:
                results.append(stack.pop())
    return results

nodes_list = {
    "A": ["B","D"],
    "B": ["A","C"],
    "C": ["B"],
    "D": ["A","E","F"],
    "E": ["D","F","G"],
    "F": ["D","E","H"],
    "G": ["E","H"],
    "H": ["G","F"],
} 

results = DFS(nodes_list)
        
results.pop()
            
print(results)