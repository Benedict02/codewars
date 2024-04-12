import sys

# spamming sys.stdout.write is annoying. I'll use this output template from now onwards.
O = lambda s: sys.stdout.write(str(s))
def I(): return sys.stdin.readline().replace('\n', '')

def Queue():
    n, t = map(int, I().split())
    s = I()
    while t != 0:
        t -= 1
        s = s.replace('BG', 'GB')
    return s


if __name__ == '__main__':
    O(Queue())