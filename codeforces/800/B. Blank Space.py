import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MI(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))

def BlankSpace():
    t = int(I())
    for _ in range(t):
        n = int(I())
        s = MI()
        t = 0
        h = 0
        for i in range(n):
            if s[i] == 0:
                t += 1
                if t > h:
                    h = t
            else:
                t = 0
        O(h)



if __name__ == '__main__':
    BlankSpace()