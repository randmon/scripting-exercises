def contains_duplicates(xs):
    n = len(xs)
    for x in range(n):
        for y in range(x+1, n):
            if (xs[x] == xs[y]):
                return True
    return False

