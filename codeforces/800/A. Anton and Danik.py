import sys

def AntonDanik():
    n = int(sys.stdin.readline())
    s = list(sys.stdin.readline())

    if s.count("D") > s.count("A"):
        return "Danik"
    elif s.count("D") == s.count("A"):
        return "Friendship"
    else:
        return "Anton"

if __name__ == "__main__":
    sys.stdout.write(str(AntonDanik()))