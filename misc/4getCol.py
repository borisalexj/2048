arr = [[0, 4, 8, 12], [1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15]]
arr2 = arr[:]

def getCol(arr, colNum):
    res = []
    for y in range(len(arr)):
        res.append(arr[y][colNum])
    return res

def putCol(arr, colNum, col):
    res = arr[:]
    # print(colNum)
    #print(col)
    for y in range(len(arr)):
        #print(col[y],y)
        res[y][colNum] = col[y]
    return res


for a in arr:
    print(a)
print("-" * 25)
print(getCol(arr, 0))
print(getCol(arr, 1))
print(getCol(arr, 2))
print(getCol(arr, 3))

print("-" * 25)
for a in arr2:
    print(a)
print("-" * 25)
arr2 = putCol(arr2, 1, list(reversed(getCol(arr2, 1))))
arr2 = putCol(arr2, 2, list(reversed(getCol(arr2, 2))))
for a in arr2:
    print(a)
