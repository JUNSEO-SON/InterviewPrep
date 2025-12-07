from itertools import permutations
n = int(input())

# Please write your code here.
lst=[i for i in range(1,n+1)]
lst=list(permutations(lst,n))
lst.sort(reverse=True)
for perm in lst:
    print(*perm)