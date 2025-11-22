from heapq import heappop,heappush
n, m = map(int, input().split())

graph=[[] for _ in range(n+1)]

for _ in range(m):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))

# Please write your code here.

def dijkstra(graph,start):
    l=len(graph)
    distances=[float('inf') for _ in range(l)]
    distances[start]=0

    pq=[]
    heappush(pq,(start,0))

    while pq:
        curr_node,curr_dist=heappop(pq)

        if distances[curr_node]<curr_dist:
            continue
    
        for n,w in graph[curr_node]:
            new_dist=curr_dist+w
            if new_dist<distances[n]:
                distances[n]=new_dist
                heappush(pq,(n,new_dist)) 
    
    return distances


distances=dijkstra(graph,1)

for d in distances[2:]:
    if d==float('inf'):
        print(-1)
    else:
        print(d)

