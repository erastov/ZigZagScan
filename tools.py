def create_indexes(n):
    """Create start and stop indexes for i"""
    indexes = []

    for i in range(n):
        indexes.append(list([i, 0]))
    for i in range(1, n):
        indexes.append(list([n - 1, i]))
    for i in range(n * 2 - 1):
        if i % 2 != 0:
            indexes[i].reverse()
            indexes[i].append(1)
        else:
            indexes[i].append(-1)

    return indexes
