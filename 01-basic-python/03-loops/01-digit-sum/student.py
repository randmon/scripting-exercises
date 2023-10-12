def count_turns(ns):
    count = 0
    for x, y, z in zip(ns, ns[1:], ns[2:]):
        if x < y > z or x > y < z:
            count += 1
    return count