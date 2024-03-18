# I feel like this is not supposed to be a 5 kyu kata
def generate_hashtag(s):
    s = s.title()
    repl = s.replace(" ", "")
    ret = ("#" + repl)
    if len(ret) > 140 or repl == "":
        return False
    else:
        return ret

# This should be placed in 7 kyu