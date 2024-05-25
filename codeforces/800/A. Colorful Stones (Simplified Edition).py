import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MII(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))
def MSI(): return list([*sys.stdin.readline()])

def ColorfulStones():
    s = MSI()
    t = MSI()
    res = 1
    j = 0
    for i in range(len(t)):
        if s[j] == t[i]:
            res += 1
            j += 1
    return res


if __name__ == '__main__':
    O(ColorfulStones())