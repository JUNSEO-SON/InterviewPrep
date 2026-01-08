N = int(input())

command = []
num = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push_back" :
        num.append(int(line[1]))
    elif line[0] == "get":
        print(num[int(line[1])-1])
    else:
        if line[0] == 'pop_back':
            num.pop()
        else: #size
            print(len(num))
            

# Please write your code here.

