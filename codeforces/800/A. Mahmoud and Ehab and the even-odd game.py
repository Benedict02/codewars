import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def II(): return int(int(sys.stdin.readline().replace('\n', '')))
def SI(): return sys.stdin.readline().replace('\n', '')
def MII(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))
def MSI(): return list(sys.stdin.readline().replace('\n', ''))

def MahmoudNEhabNTheEvenOddGame():
    n = II()
    if n%2:
        return "Ehab"
    else:
        return "Mahmoud"


if __name__ == '__main__':
    O(MahmoudNEhabNTheEvenOddGame())