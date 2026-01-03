a, b = map(int, input().split())
n = input()

# Please write your code here.

target=(int(n,a))

lst=[]
while target>0:
    lst.append(target%b)
    target=target//b

print(*lst[::-1],sep='')