# Original
"""
import sys

def WSubtraction():
    n, k = sys.stdin.readline().split()
    ln = list(map(int, n))
    for i in range(int(k)):
        if ln[len(ln)-1] == 0:
            ln.pop()
        else:
            ln[len(ln)-1] -= 1
    return "".join(map(str, ln))


if __name__ == '__main__':
    sys.stdout.write(str(WSubtraction()))
"""
# Alternative:
import sys

def WSubtraction():
    n, k = map(int, sys.stdin.readline().split())
    for i in range(k):
        if n % 10 == 0:
            n /= 10
        else:
            n -= 1
    return int(n)


if __name__ == '__main__':
    sys.stdout.write(str(WSubtraction()))


