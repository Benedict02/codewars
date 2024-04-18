import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MI(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))

def RemoveSmallest():
    # Wrong. Rewrite your whole algorithm. Im not at my prime time. Its nighttime I cant think
    t = int(I())
    for _ in range(t):
        n = int(I())
        s = MI()
        if len(s) > 1 and s[n-1] - s[0] <= 1:
            O("YES")
        elif len(s) == 1:
            O("YES")
        else:
            O("NO")



if __name__ == '__main__':
    RemoveSmallest()