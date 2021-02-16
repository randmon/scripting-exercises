def median(ns):
    ns = sorted(ns)
    n = len(ns)
    if (n % 2 == 0):
        return (ns[n//2 - 1] + ns[n//2]) / 2
    else:
        return ns[n//2]