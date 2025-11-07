n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
graph=[[] for _ in range(n+1)] 
visited=[False]*(n+1)

for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])


def dfs(graph,visited,v):
    count=0
    visited[v]=True
    for edge in graph[v]:
        if not visited[edge]:
            count+=1
            visited[edge]=True
            count+=dfs(graph,visited,edge)

        
    return count

print(dfs(graph,visited,1))




