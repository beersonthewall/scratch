from collections import deque
from typing import List

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    # inDeg[node] = count of inbound edges to <node>
    inDeg = {i:0 for i in range(numCourses)}
    # adjacency list representation of a graph
    graph = {}

    # Calculate inDegree for each node and construct
    # the adjacency lists.
    for start,end in prerequisites:
        inDeg[end] = inDeg.get(end,0) + 1
        adj = graph.get(start, [])
        adj.append(end)
        graph[start] = adj
    
    sources = []
    for node, deg in inDeg.items():
        if deg == 0:
            sources.append(node)
    
    if not sources:
        return False
    
    q = deque(sources)

    topSort = []
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            topSort.append(node)
            for child in graph.get(node, []):
                inDeg[child] -= 1
                if inDeg[child] == 0:
                    q.append(child)
    return len(topSort) == numCourses

def main():
    print(canFinish(2, [[1,0]]))
    print(canFinish(2, [[1,0],[0,1]]))

if __name__ == '__main__':
    main()

    
