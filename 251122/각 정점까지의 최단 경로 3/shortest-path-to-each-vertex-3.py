from heapq import heappop,heappush
n, m = map(int, input().split())

graph=[[] for _ in range(n+1)]

for _ in range(m):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))

# Please write your code here.

def dijkstra(graph,start):

    pq=[]
    distances=[float('inf') for _ in range(len(graph))]
    distances[start]=0
    heappush(pq,(0,start))

    while pq:

        curr_d,curr_n=heappop(pq)

        if curr_d>distances[curr_n]:
            continue
        
        for n, w in graph[curr_n]:
            new_d=curr_d+w

            if new_d < distances[n]:
                distances[n]=new_d
                heappush(pq,(new_d,n))

    return distances[start+1:]

distances=dijkstra(graph,1)

for distance in distances:
    if distance == float('inf'):
        print(-1)
    else:
        print(distance)


