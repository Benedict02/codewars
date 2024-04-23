import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MI(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))

def ShortSort():
    n = int(I())
    legal = ["abc", "acb","bac","cba"]
    for _ in range(n):
        if I() in legal:
            O("YES")
        else:
            O("NO")


if __name__ == '__main__':
    ShortSort()