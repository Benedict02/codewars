import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MI(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))

def BlackSquare():
    n = MI()
    s = list(map(int, I()))
    res = 0
    for i in s:
        res += n[i-1]
    return res



if __name__ == '__main__':
    O(BlackSquare())