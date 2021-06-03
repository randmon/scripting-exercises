def slug(name):
    parts = (name).lower().split()
    return "-".join(s for s in parts[1:] + [parts[0]])