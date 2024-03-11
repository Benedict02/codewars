def possibly_perfect(key, answers):
    right = 0
    wrong = 0
    removedUnderScore = 0
    for i in range(len(key)):
        if key[i] != "_":
            if key[i] == answers[i]:
                right += 1
            elif key[i] != answers[i]:
                wrong += 1
        else:
            removedUnderScore += 1
    if (right == (len(key) - removedUnderScore)) or (wrong == (len(key) - removedUnderScore)):
        return True
    else:
        return False

#In the future, Go make this code efficient