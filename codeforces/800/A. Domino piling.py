import sys

def domino():
    m, n = map(int, sys.stdin.readline().split())
    return (m * n)//2

if __name__ == '__main__':
    sys.stdout.write(str(domino()))