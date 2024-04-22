import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MI(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))

def AmusingJoke():
    n1 = list(I())
    n2 = list(I())
    s = list(I())
    if sorted(s) == sorted(n1+n2):
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    O(AmusingJoke())