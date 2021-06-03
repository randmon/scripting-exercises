def greatest_sum(ns):
    return max([(i, j) for i in range(len(ns)) for j in range(i + 1, len(ns) + 1)], key=lambda p:sum(ns[p[0]:p[1]]))
