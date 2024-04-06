import sys

def Lexicographical_order():
    s1 = sys.stdin.readline().lower()
    s2 = sys.stdin.readline().lower()
    if s1 > s2:
        return 1
    elif s1 == s2:
        return 0
    elif s1 < s2:
        return -1

if __name__ == "__main__":
    sys.stdout.write(str(Lexicographical_order()))