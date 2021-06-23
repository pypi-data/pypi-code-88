from queue import Queue

def bfs(graph):
    
    first_node = next(iter(graph))
    
    visited = {}
    parent  = {}
    level   = {} # distance 
    result = []
    queue = Queue()

    for node in graph:
        visited[node] = False
        parent[node]  = None
        level[node]   = -1

    visited[first_node] = True
    level[first_node] = 0
    queue.put(first_node)
    result = [first_node]

    while not queue.empty():
        curr_node = queue.get() # remove and return element
        for child in graph[curr_node]:
            if not visited[child]:
                visited[child] = True
                parent[child]  = curr_node
                level[child]   = level[curr_node] + 1
                queue.put(child)
                result.append(child)
                
    return result


graph = {
    "A": ["B","D"],
    "B": ["A","C"],
    "C": ["B"],
    "D": ["A","E","F"],
    "E": ["D","F","G"],
    "F": ["D","E","H"],
    "G": ["E","H"],
    "H": ["G","F"],
}

result = bfs(graph)

print(result)