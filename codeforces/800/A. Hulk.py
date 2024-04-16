import sys

O = lambda s: sys.stdout.write(str(s))
def I(): return sys.stdin.readline().replace('\n', '')

def Hulk():
    n = int(I())
    s = []
    # False hate True love
    switch = False
    for i in range(n):
        if i == n-1:
            if switch:
                s.append('I love it')
                switch = False
            else:
                s.append('I hate it')
                switch = True
        else:
            if switch:
                s.append('I love that ')
                switch = False
            else:
                s.append('I hate that ')
                switch = True

    return "".join(s)

if __name__ == '__main__':
    O(Hulk())