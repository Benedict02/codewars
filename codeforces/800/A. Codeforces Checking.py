import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MI(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))

def CodeforcesChecking():
    n = int(I())
    for _ in range(n):
        if I().lower() in "codeforces":
            O("YES")
        else:
            O("NO")

if __name__ == '__main__':
    CodeforcesChecking()