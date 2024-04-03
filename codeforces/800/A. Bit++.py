import sys

def bitpp():
    n = int(input())
    x = 0
    for i in range(0, n):
        a = input()
        if a.lower() == '++x':
            x += 1
        if a.lower() == 'x++':
            x += 1
        if a.lower() == '--x':
            x -= 1
        if a.lower() == 'x--':
            x -= 1
    return x

if __name__ == '__main__':
    sys.stdout.write(str(bitpp()))