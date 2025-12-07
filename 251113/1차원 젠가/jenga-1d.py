n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())
temp=[]
ans=[]
# Please write your code here.
for i in range(len(blocks)):
    if not s1-1<=i<=e1-1:
        temp.append(blocks[i])


for i in range(len(temp)):
    if not s2-1<=i<=e2-1:
        ans.append(temp[i])

print(len(ans))
print(*ans,sep='\n')
