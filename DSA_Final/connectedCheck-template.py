V,E = map(int, input().split())
edgeList = []
for i in range(E):
    edgeList.append(tuple(map(int, input().split())))

from disjointsets3 import DisjointSets

s = DisjointSets(V)

# Complete the code below

# Sort the edges by weight
edgeList.sort(key=lambda a: a[2])

# Initialize variables
W = 0  # Total weight of the minimum spanning tree
edgeCount = 0  # Number of edges in the minimum spanning tree

# Iterate through the sorted edges
for u, v, w in edgeList:
    if s.findset(u) != s.findset(v):  # Check if adding this edge forms a cycle
        W += w  # Add the weight of the edge to the total weight
        s.union(u, v)  # Merge the sets containing u and v
        edgeCount += 1  # Increment the edge count

    # If the number of edges in the minimum spanning tree is equal to V - 1,
    # where V is the number of vertices, we have found the minimum spanning tree.
    if edgeCount == V - 1:
        break

# Check if the graph is connected
if edgeCount >= V - 1:
    print("Connected")
    print(W)  # Print the total weight of the minimum spanning tree
else:
    print("Not Connected")

    
# 6 9
# 0 1 5
# 0 2 10
# 1 2 8
# 1 3 7
# 2 3 6
# 2 4 9
# 3 4 11
# 3 5 20
# 4 5 12
# Connected
# 39