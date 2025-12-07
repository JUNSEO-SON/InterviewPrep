n = int(input())
words = [sorted(input()) for _ in range(n)]
memory={}
# Please write your code here.
for word in words:
    if tuple(word) not in memory:
        memory[tuple(word)]=1
    else:
        memory[tuple(word)]+=1

print(max(memory.values()))
