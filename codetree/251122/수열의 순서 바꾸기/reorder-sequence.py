n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.

l=len(sequence)
for i in range(l-1,-1,-1):
    if sequence[i]<sequence[i-1]:
        break

print(i)