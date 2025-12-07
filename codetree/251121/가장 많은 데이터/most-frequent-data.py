from collections import Counter
n = int(input())
words = [input() for _ in range(n)]

# Please write your code here.

word_cnt=Counter(words)
print(word_cnt.most_common(1)[0][1])