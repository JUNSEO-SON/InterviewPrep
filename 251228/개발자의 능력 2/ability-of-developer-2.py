ability = list(map(int, input().split()))

# Please write your code here.
ability.sort()
lst=[ability[0]+ability[-1],ability[1]+ability[-2],ability[2]+ability[-3]]
print(max(lst)-min(lst))