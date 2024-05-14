import sys
from datetime import datetime

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MI(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))

def convert12(t):
    t = datetime.strptime(t, '%H:%M')
    return t.strftime('%I:%M %p')

def ClockConversion():
    n = int(I())
    for _ in range(n):
        s = I()
        O(convert12(s))


if __name__ == '__main__':
    ClockConversion()