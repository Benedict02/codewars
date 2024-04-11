import sys

def EasyOrHard():
    sys.stdin.readline()
    if list(sys.stdin.readline().replace('\n', '')).count('1') != 0:
        return "HARD"
    else:
        return "EASY"

if __name__ == '__main__':
    sys.stdout.write(str(EasyOrHard()))