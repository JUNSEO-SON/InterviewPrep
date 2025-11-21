n, m = map(int, input().split())

# Note: Using 1-based indexing for words as per C++ code
words = [""] + [input() for _ in range(n)]
queries = [input() for _ in range(m)]

# Please write your code here.
word_dict={}
for i,v in enumerate(words):
    word_dict[v]=i

print(word_dict)