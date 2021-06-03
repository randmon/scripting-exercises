def mode(ns):
    return sorted({n:ns.count(n) for n in set(ns)}.items(), key=lambda item:item[1], reverse=True)[0][0]
    