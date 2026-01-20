import math


def print_path(parent, destination):
    if parent[destination] == destination:
        print(destination, end = " ")
    else:
        print_path(parent, parent[destination])
        print(destination, end = " ")

def bellman(graph,source,v):
    distance=[math.inf]*v
    parent=[-1]*v  
    v=v
    distance[source]=0
    parent[source]=source
    for i in range(v):
        flag=False
        for j,k in graph.items():
            for l in k:
                if distance[l[0]]>distance[j]+l[1]:
                    distance[l[0]]=distance[j]+l[1]
                    parent[l[0]]=j
                    flag=True
        if flag==False:
            break
        if i==v-1:
            print("Negative Cycle detected")
            return
    
    print(distance)
    print(parent)
    for i in range(v):
        print_path(parent, i)
        print()


# 
# graph={
#     0:[(1,7),(2,4)],
#     1:[(2,-4)],
#     2:[]
#     }
# 
# v=3
# source =0
# 
# 
# graph2={
#     0:[(1,5)],
#     1:[(2,4)],
#     2:[(0,-10)]
#     }
# 
# bellman(graph,source,v)
# bellman(graph2,source,v)
#     
