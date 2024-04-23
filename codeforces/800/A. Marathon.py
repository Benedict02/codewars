import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MI(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))

def Marathon():
    n = int(I())
    for _ in range(n):
        res = 0
        a, b, c, d = MI()
        if a < b:
            res += 1
        if a < c:
            res += 1
        if a < d:
            res += 1
        O(res)


if __name__ == '__main__':
    Marathon()