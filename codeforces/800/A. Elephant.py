import sys, math

def Elephant():
    I = int(sys.stdin.readline())
    return math.ceil(I/5)

if __name__ == '__main__':
    sys.stdout.write(str(Elephant()))