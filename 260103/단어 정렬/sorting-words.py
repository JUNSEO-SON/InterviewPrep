n = int(input())
word = [input() for _ in range(n)]

# Please write your code here.
print(*sorted(word),sep='\n')