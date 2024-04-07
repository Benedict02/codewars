import sys

def StonesOnTable():
    n = int(sys.stdin.readline())
    s = list(sys.stdin.readline())
    s.pop()
    res = 0
    for i in range(0, n):
        if i < n-1:
            if s[i] == s[i+1]:
                res += 1
    return res

if __name__ == '__main__':
    sys.stdout.write(str(StonesOnTable()))