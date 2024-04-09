import sys

def Translation():
    I = list(sys.stdin.readline().replace('\n', ''))
    I.reverse()
    s = list(sys.stdin.readline().replace('\n', ''))
    if I == s:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    sys.stdout.write(str(Translation()))