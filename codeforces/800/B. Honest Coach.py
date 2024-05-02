import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MI(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))

def HonestCoach():
    n = int(I())
    for _ in range(n):
        ns = int(I())
        s = MI()
        s = sorted(s)
        a = []
        for i in range(ns):
            for j in range(i+1, ns):
                a.append(s[j] - s[i])
        O(min(a))


if __name__ == '__main__':
    HonestCoach()