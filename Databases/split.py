def div_first_last(string):
    n = string.split()[:-1]
    n = " ".join(n)
    s = string.split()[-1].strip()
    return n, s
