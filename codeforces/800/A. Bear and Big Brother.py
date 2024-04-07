import sys

def WhoIsBigger():
    a, b = map(int, sys.stdin.readline().split())
    loop = True
    res = 0
    while(loop):
        if a < b or a==b:
            a *= 3
            b *= 2
            res += 1
        else:
            loop = False
            return res

if __name__ == '__main__':
    sys.stdout.write(str(WhoIsBigger()))