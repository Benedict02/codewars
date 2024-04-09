import sys

def LuckyNumber():
    x = list(sys.stdin.readline())
    x.pop()
    I = list(map(int, x))
    if I.count(7) + I.count(4) == 4 or I.count(7) + I.count(4) == 7:
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":
    sys.stdout.write(str(LuckyNumber()))