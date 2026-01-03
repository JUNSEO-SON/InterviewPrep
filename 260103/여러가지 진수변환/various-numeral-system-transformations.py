N, B = map(int, input().split())

# Please write your code here.
lst=[]
while N>0:
    lst.append(N%B)
    N=N//B

print(*lst[::-1],sep='')