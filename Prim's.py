from queue import PriorityQueue

graph = [
    [(1, 4), (7, 8)],         # Node 0
    [(0, 4), (2, 8), (7, 11)],# Node 1
    [(1, 8), (3, 7), (5, 4), (8, 2)], # Node 2
    [(2, 7), (4, 9), (5, 14)],# Node 3
    [(3, 9), (5, 10)],        # Node 4
    [(2, 4), (3, 14), (4, 10), (6, 2)], # Node 5
    [(5, 2), (7, 1), (8, 6)], # Node 6
    [(0, 8), (1, 11), (6, 1), (8, 7)], # Node 7
    [(2, 2), (6, 6), (7, 7)]  # Node 8
]


visited =[False]* len(graph)

q= PriorityQueue()
mst = [[]for _ in range(len(graph))]

start_node = 0
visited[start_node]= True

for neighbour,weight in graph[start_node]:
    q.put((weight,start_node, neighbour))
##################

while not q.empty():
    weight, u,v = q.get()
    if visited[v]:
        continue
    visited[v] = True
    
    mst[u].append((v,weight))
    mst[v].append((u,weight))

    for neighbour,weight in graph[v]:
        if not visited[neighbour]:
            q.put((weight,v,neighbour))
    
print(mst)

