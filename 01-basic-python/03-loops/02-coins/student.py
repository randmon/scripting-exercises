def coins(one, two, five, goal):
    #range(x,y) is (inclusive, exclusive) so from and counting x to and not counting y
    for x in range(0, one+1):
        for y in range(0, two+1):
            for z in range(0, five+1):
                if x + 2 * y + 5 * z == goal:
                    return True

    return False