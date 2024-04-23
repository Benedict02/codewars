import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MI(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))

def MishkaNGame():
    n = int(I())
    C = 0
    M = 0
    for _ in range(n):
        sm, sc = MI()
        if sm > sc:
            M += 1
        elif sm < sc:
            C += 1
    if C > M:
        return "Chris"
    elif C < M:
        return "Mishka"
    else:
        return "Friendship is magic!^^"

if __name__ == '__main__':
    O(MishkaNGame())