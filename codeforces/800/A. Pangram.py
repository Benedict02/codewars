import re
import sys

O = lambda s: sys.stdout.write(str(s))
def I(): return sys.stdin.readline().replace('\n', '')
def MI(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))

def main():
    n = int(I())
    if len(set(re.findall('[a-zA-Z]', I().lower()))) >= 26:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    O(main())