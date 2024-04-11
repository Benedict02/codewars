import sys

def BeautifulYear():
    n = list(map(int, sys.stdin.readline().replace('\n', '')))
    while True:
        n = int("".join(list(map(str, n))))
        n += 1
        n = list(map(int, str(n)))
        if len(n) == len(set(n)):
            return int("".join(list(map(str, n))))

if __name__ == '__main__':
    sys.stdout.write(str(BeautifulYear()))