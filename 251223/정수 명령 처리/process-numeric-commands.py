N = int(input())
stack=[]
for _ in range(N):
    command=input().split()

    if len(command)==2:
        stack.append(command[1])

    else:
        if command[0]=='pop':
            print(stack.pop())
        elif command[0]=='size':
            print(len(stack))
        elif command[0]=='empty':
            if len(stack)==0:
                print(1)
            else:
                print(0)
        elif command[0]=='top':
            print(stack[-1])