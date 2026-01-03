n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
A_set=set(A)
B_set=set(B)

def solver():
    for num in A_set:
        if num not in B_set:
            return False

    return True

ans=solver()
print('Yes' if ans else 'No')