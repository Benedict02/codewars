import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MI(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))

def PLSORMIN():
    n = int(I())
    res = []
    for _ in range(n):
        s = MI()
        if s[0] + s[1] == s[2]:
            res.append("+")
        else:
            res.append("-")
    [O(res[x]) for x in range(len(res))]

if __name__ == '__main__':
    PLSORMIN()