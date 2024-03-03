
# A call to topological_sort must be with two arguments
# 1) The number of vertices of the Directed Acyclic Graph
# 2) The adjacency lists of the graph

visited = []
stack = []

def DFS_visit(s, adj): 
    global visited, stack
    
    for v in adj[s]:
        if not visited[v]:
            visited[v] = True
            DFS_visit(v, adj)
    stack.append(s)

def topological_sort(V, adj):
    global visited, stack
    
    visited = [False]*V
    for s in range(V):
        if not visited[s]:
            visited[s] = True
            DFS_visit(s, adj)
    stack.reverse()
    return stack

V, E = map(int, input("Enter the number of vertices and edges: ").split())

adj = [[] for _ in range(V)]

print("Enter edges (format: 'u v', where u and v are vertices):")
for _ in range(E):
    u, v = map(int, input().split())
    adj[u].append(v)


topological_result = topological_sort(V, adj)

print("Topological Sort:")
print(topological_result)


# Enter the number of vertices and edges: 6 7
# Enter edges (format: 'u v', where u and v are vertices):
# 0 1
# 0 2
# 1 3
# 2 3
# 2 4
# 3 5
# 4 5
