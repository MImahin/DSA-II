import math
from queue import PriorityQueue

def dijkstra(grap,source,v):
    distance=[math.inf]*v
    parent=[-1]*v
    c=[0]*v
    
    pq=PriorityQueue()
    
    distance[source]=0
    pq.put((distance[source],source))
    parent[source]=source
    
    
    while not pq.empty():
        current_node=pq.get()[1]
        if optimal[current_node]==1:
            continue
        current_node=1
        
        for neighbor, cost in graph[current_node]:
            if found_optimal[neighbor] != 1:
                if distance[neighbor] > distance[current_node] + cost:
                    distance[neighbor] = distance[current_node] + cost
                    pq.put((distance[neighbor], neighbor))
                    parent[neighbor] = current_node
 
    for i in range(V):
        print_path(parent, i)
        print()


# 
# graph={
#     0:[(1,5),(2,4)],
#     1:[(2,2),(3,10)],
#     2:[(3,7)],
#     3:[]
#     }
# 
# v=4
# source =0
# 
# dijkstra(graph,source,v)
#     