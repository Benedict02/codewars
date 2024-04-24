import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MI(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))

def DislikeOfThrees():
    n = int(I())
    res = []
    for _ in range(n):
        s = I()
        

if __name__ == '__main__':
    DislikeOfThrees()