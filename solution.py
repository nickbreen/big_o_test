def solution(N):
    pass
    # create binary sequence
    n = N
    b = []
    while n > 0:
        # print(n)
        b.append(int(n % 2))
        n = int(n / 2)
    # print(b)
    i = None  # sequence index
    s = []
    one = False  # found the first one yet?
    for d in b:
        if not one and d == 1:
            one = True
            continue
        elif not one:
            continue
        if d == 1:
            i = None
        if one and d == 0:
            if i is None:
                s.append(0)
            i = len(s) - 1
            s[i] = s[i] + 1
    # print(s)
    return max(s) if len(s) else 0

