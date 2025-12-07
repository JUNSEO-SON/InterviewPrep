from collections import Counter,defaultdict
s = input()

# Please write your code here.
def solution():
    d=defaultdict(int)
    for c in s:
        d[c]+=1

    for k,v in d.items():
        if v==1:
            print(k)
            return

    print(None)

solution()