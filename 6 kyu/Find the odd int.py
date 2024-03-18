def find_it(seq):
    unique = set(seq)
    unique = list(unique)
    
    for i in unique:
        if seq.count(i) % 2 == 1:
            ret = i
    return ret