import sys

def HelpfulMath():
    a = list(map(int, sys.stdin.readline().split('+')))
    b = sorted(a)
    c = []
    for i in range(len(b)):
        c.append(b[i])
        if i < len(b) - 1:
            c.append('+')
    return ''.join(str(item) for item in c)


if __name__ == '__main__':
    sys.stdout.write(str(HelpfulMath()))