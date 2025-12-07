n = int(input())
commands = []
for _ in range(n):
    line = input().split()
    cmd = line[0]
    k = int(line[1])
    if cmd == "add":
        v = int(line[2])
        commands.append((cmd, k, v))
    else:
        commands.append((cmd, k))

# Please write your code here.

d={}
for c in commands:
    if len(c)==3:
        d[c[1]]=c[2]

    else:
        if c[0]=='remove':
            d.pop(c[1])
        else:
            if c[1] in d:
                print(d[c[1]])
            else:
                print('None')


    
