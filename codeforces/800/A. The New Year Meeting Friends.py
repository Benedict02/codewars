import sys

def O(s, sep='\n'): sys.stdout.write(str(s) + sep)
def I(): return sys.stdin.readline().replace('\n', '')
def MII(): return list(map(int, sys.stdin.readline().replace('\n', '').split()))
def MSI(): return list(sys.stdin.readline.replace('\n', ''))

def TheNewYearMeetingFriends():
    x = MII()
    x.sort()
    return (x[1]-x[0]) + (x[2] - x[1])
    

if __name__ == '__main__':
    O(TheNewYearMeetingFriends())