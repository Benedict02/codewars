import sys

def team():
    n = int(input())
    a = []
    b = []
    t = 0
    for i in range(0, n):
        a.append(input().split(' '))
    
    for j in range(0, len(a)):
        if a[j].count('1') < 2:
            pass
        else:
            t += 1
    return t


if __name__ == '__main__':
    sys.stdout.write(f"{team()}")