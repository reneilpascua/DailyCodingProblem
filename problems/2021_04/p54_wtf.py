class Hello:
    def __init__(self, n):
        self.size = n

    def solve(self):
        i = 0
        j = 0
        while i < 9:
            print(i)
            i+=1

if __name__ == '__main__':
    hello = Hello(3)
    hello.solve()