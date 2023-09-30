# Function to print a DFS of graph 
def dfs(graph, vertex, path=[]):
  path += [vertex]

  for neighbor in graph[vertex]:
    if neighbor not in path:
        path = dfs(graph, neighbor, path)

  return path

# small graph with a starting node of 2
graph1 = {
  0: [1, 2],
  1: [2],
  2: [0, 3],
  3: [3]
}

print("Depth First Traversal on Graph 1 (starting from node 2): " + str(dfs(graph1, 2)) )

# large graph with a starting node of 1
graph2 = {
  1: [2, 3],
  2: [4, 5],
  3: [5],
  4: [6],
  5: [6],
  7: []
}

print("Depth First Traversal on Graph 2 (starting from node 1): " + str(dfs(graph2, 1)) )