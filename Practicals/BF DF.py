graph = { 
    
    '5': ['3', '7'], 
    '3': ['2', '4'], 
    '7': ['8'], 
    '2': [], 
    '4': [], 
    '8': [] 
} 

visited_DFS = [] 

def dfs(visited_list, graph, node): 
 if node not in visited_list: 
     print(node, end=" ") 
 visited_list.append(node)
 for neighbour in graph[node]: 
    dfs(visited_list, graph, neighbour) 
    

visited_BFS = [] 
queue = [] 
def bfs(Visited_list, graph, node): 
 Visited_list.append(node) 
 queue.append(node)
 while queue: 
     front = queue.pop(0) 
     print(front, end=" ") 
     
     for neighbour in graph[front]:
             if neighbour not in Visited_list: 
                  Visited_list.append(neighbour) 
                  queue.append(neighbour) 

print("Following is the Depth-First Search:") 
dfs(visited_DFS, graph, '5') 
print("\nFollowing is the Breadth-First Search:") 
bfs(visited_BFS, graph, '5')