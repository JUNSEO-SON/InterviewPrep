unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Please write your code here.

class explosion:
    def __init__(self,code, color, second):
        self.code=unlock_code
        self.color=wire_color
        self.second=seconds

    def info(self):
        print(f'code : {self.code}')
        print(f'color : {self.color}')
        print(f'second : {self.second}')

exp=explosion(unlock_code, wire_color, seconds)
exp.info()