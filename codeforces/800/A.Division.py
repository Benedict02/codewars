import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MI(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))

def isDivision():
    n = int(I())
    for _ in range(n):
        s = int(I())
        if s <= 1399:
            O("Division 4")
        elif 1400 <= s and s <= 1599:
            O("Division 3")
        elif 1600 <= s and s <= 1899:
            O("Division 2")
        elif 1900 <= s:
            O("Division 1")


if __name__ == '__main__':
    isDivision()