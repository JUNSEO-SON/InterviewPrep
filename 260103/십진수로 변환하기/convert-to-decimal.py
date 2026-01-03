binary = input()

# Please write your code here.
total=0
for i in range(1,len(binary)+1):
    total+=(2**(i-1))*int(binary[-i])

print(int(total))