n, k, t = input().split()
n, k = int(n), int(k)
strs = [input() for _ in range(n)]

# Please write your code here.
l=len(t)
target=[]
for s in strs:
    if s[:l]==t:
        target.append(s)

target.sort()

print(target[k-1])