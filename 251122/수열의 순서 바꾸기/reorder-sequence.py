n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.


if sequence==sorted(sequence):
    print(0)
else:
    print(n-1)