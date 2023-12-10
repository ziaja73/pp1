def p1(p1: str,p2: str):
    s1 = 0
    s2 = 0
    karty = {'A': 10, 'K': 10, 'Q': 10, 'J': 10, 'T': 10}
    for i in p1:
        if i.isdigit():
            i = int(i)
            s1 += i
        else:
            s1 += karty.get(i)
    for i in p2:
        if i.isdigit():
            i = int(i)
            s2 += i
        else:
            s2 += karty.get(i)
    if s1 >= s2:
        return True
    else:
        return False