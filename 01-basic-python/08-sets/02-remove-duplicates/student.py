def remove_duplicates(xs):
    result = []
    found = set()
    for x in xs:
        if x not in found:
            found.add(x)
            result.append(x)
    return result