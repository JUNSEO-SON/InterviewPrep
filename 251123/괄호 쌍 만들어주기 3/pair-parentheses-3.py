A = input()
count=0
# Please write your code here.
for i in range(len(A)):
    for j in range(i+1,len(A)):
        if A[i]!='(':
            continue

        if A[j]==')':
            count+=1
print(count)