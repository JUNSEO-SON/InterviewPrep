from heapq import heappush,heappop

n, m = map(int, input().split())
k = int(input())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
graph=[[] for _ in range(n+1)]

for u,v,w in edges:
    graph[u].append((v,w))
    graph[v].append((u,w))

def dijkstra(graph,start):
    n=len(graph)
    distances=[float('inf') for _ in range(n)]


    pq=[]
    heappush(pq,(0,start))
    distances[start]=0

    while pq:
        current_dist,current_node=heappop(pq)
        if distances[current_node]<current_dist:
            continue
        
        for n,w in graph[current_node]:
            new_dist=current_dist+w
            
            if new_dist<distances[n]:
                distances[n]=new_dist
                heappush(pq,(new_dist,n))

    return distances

dist=dijkstra(graph,k)

for d in dist[1:]:
    if d!=float('inf'):
        print(d)
    else:
        print(-1)
