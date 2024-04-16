import sys

O = lambda s: sys.stdout.write(str(s))
def I(): return sys.stdin.readline().replace('\n', '')
def MI(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))

def Divisibility():
    res = []
    n = int(I())
    for i in range(n):
        displacement = 0
        num = MI()
        a, b = num[0], num[1]
        while a % b != 0:
            a += 1
            displacement += 1
        res.append(displacement)
    for j in range(len(res)):
        print(res[j])

if __name__ == '__main__':
    Divisibility()