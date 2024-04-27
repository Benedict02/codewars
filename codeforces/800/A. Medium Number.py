import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MI(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))

def Median():
    n = int(I())
    for _ in range(n):
        s = MI()
        O(sorted(s)[len(s)//2])


if __name__ == '__main__':
    Median()