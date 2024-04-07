import sys

def BoyOrGirl():
    I = sys.stdin.readline()
    uniqueI = set(I)
    if len(uniqueI) % 2 == 1:
        return "CHAT WITH HER!"
    else:
        return "IGNORE HIM!"

if __name__ == "__main__":
    sys.stdout.write(str(BoyOrGirl()))