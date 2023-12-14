# Breadth-First Search on Constantly Updated Graph
def bfs(source, sink, graph, reversePath):
    queue = [source]
    visited = set([source])
    while(len(queue) > 0):
        el = queue.pop(0)
        for idx in range(len(graph[el])):
            if graph[el][idx] > 0 and idx not in visited:
                reversePath[idx] = el
                queue.append(idx)
                visited.add(idx)
    if sink in visited:
        return True
    return False
        
# Ford Fulkerson Greedily looks for any other paths that can add to the max
def fordFulkerson(source, sink, graph):
    reversePath = [-1] * len(graph)
    maxPath = 0
    while(bfs(source, sink, graph, reversePath)):
        pathVal = 2000000
        reverse = sink
        while(reverse != source):
            pathVal = min(pathVal, graph[reversePath[reverse]][reverse])
            reverse = reversePath[reverse]
        maxPath += pathVal
        reverse = sink
        while(reverse != source):
            parent = reversePath[reverse]
            graph[parent][reverse] -= pathVal
            graph[reverse][parent] += pathVal
            reverse = reversePath[reverse]
    return maxPath
