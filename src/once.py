def once(inp):
    count = 0
    if count == 0:
        count += 1
        return inp()
    print(inp())
    # else:
    #     print(inp())