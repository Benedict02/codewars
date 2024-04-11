import sys

def Tram():
    a = 0
    p = 0
    for i in [0] * int(sys.stdin.readline()):
        p -= eval(sys.stdin.readline().replace(' ', '-'))
        a = max(a, p)
    return a



if __name__ == '__main__':
    sys.stdout.write(str(Tram()))