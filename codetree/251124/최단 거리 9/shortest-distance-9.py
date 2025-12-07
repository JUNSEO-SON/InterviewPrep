from collections import deque
from heapq import heappush,heappop
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
A, B = map(int, input().split())
graph=[[] for _ in range(n+1)]
# Please write your code here.
for u,v,w in edges:
    graph[u].append((v,w))
    graph[v].append((u,w))


def dijkstra(graph,start):

    n=len(graph)
    distances=[float('inf') for _ in range(n)]
    pq=[]
    paths=[-1 for _ in range(n)]
    heappush(pq,(0,start))

    while pq:
        curr_dist,curr_node=heappop(pq)

        if distances[curr_node]<curr_dist:
            continue

        for neighbor,w in graph[curr_node]:
            new_dist=curr_dist+w
            if new_dist<distances[neighbor]:
                distances[neighbor]=new_dist
                paths[neighbor]=curr_node
                heappush(pq,(new_dist,neighbor))

    
    return distances,paths


dist,path=dijkstra(graph,A)

node=B
reversed_path=[node]
while node!=A:
    node=path[node]
    reversed_path.append(node)


print(dist[B])
print(*reversed_path[::-1])
