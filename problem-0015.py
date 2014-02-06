def numGridPaths(rows, cols, valCache):
    cacheKey = "{0},{1}".format(max(rows,cols),min(rows,cols))
    if rows == 0 or cols == 0:
        return 1
    elif cacheKey not in valCache:
        valCache[cacheKey] = numGridPaths(rows-1, cols, valCache) + numGridPaths(rows, cols-1, valCache)
    return valCache[cacheKey]

cache = {}
print numGridPaths(20,20,cache)
print cache["3,2"]
print cache["3,1"]