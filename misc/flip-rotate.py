__author__ = 'user'

def horizFlip(arr):
    res = []
    for row in arr:
        # print('+', row)
        #res.append(list(reversed(row)))
        newRow = []
        for c in range(len(row)):
            newRow.append(row[len(row) - 1 - c])
        res.append(newRow)

    return res


def centerFlip(arr):
    res = []
    for x in range(len(arr[0])):
        row = []
        for y in range(len(arr)):
            row.append(arr[y][x])
        res.append(row)
    return res

def checkGameOver(arr):
    GameOver = True
    for y in range(len(arr)-1):
        for x in range(len(arr[y])-1):
            if arr[y][x] == arr[y+1][x] or arr[y][x] == arr[y][x+1]:
                GameOver = False
                return GameOver
            #print(x,y)
    return GameOver

if __name__ == '__main__':
    arr = [[1, 2, 3, 4],
           ['q', 'w', 'e', 'r'],
           [5, 6, 7, 8],
           ['a', 's', 'd', 'f']]

    print('-' * 5, ' Тest horizontal flip : ', '-' * 5)
    for row in arr:
        print(row)
    res = horizFlip(arr)
    print('-' * 5, ' Results : ', '-' * 5)
    for row in res:
        print(row)

    print('-' * 5, ' Тest center flip : ', '-' * 5)
    for row in arr:
        print(row)
    res = centerFlip(arr)
    print('-' * 5, ' Results : ', '-' * 5)
    for row in res:
        print(row)

    print('-' * 5, ' Тest \"GameOver\" : ', '-' * 5)
    arr = [[2,4,2,4,2,4],
           [4,2,4,2,4,2],
           [2,4,2,4,2,4],
           [4,2,4,2,4,2],
           [2,4,2,4,2,4],
           [4,2,4,2,4,2]]
    print("True -",checkGameOver(arr))
    arr = [[2,4,2,4,2,4],
           [2,2,4,2,4,2],
           [2,4,2,4,2,4],
           [4,2,4,2,4,2],
           [2,4,2,4,2,4],
           [4,2,4,2,4,2]]
    print("False -",checkGameOver(arr))
    arr = [[2,2,2,4,2,4],
           [4,2,4,2,4,2],
           [2,4,2,4,2,4],
           [4,2,4,2,4,2],
           [2,4,2,4,2,4],
           [4,2,4,2,4,2]]
    print("False -",checkGameOver(arr))
    arr = [[2,2,2,4,2,4],
           [4,2,4,2,4,2],
           [2,4,2,4,2,4],
           [4,2,4,2,4,2],
           [2,4,2,4,2,2],
           [4,2,4,2,4,2]]
    print("False -",checkGameOver(arr))
    arr = [[2,4,2,4,2,4],
           [4,2,4,2,4,2],
           [2,4,2,4,2,4],
           [4,2,4,2,4,2],
           [2,4,2,4,2,4],
           [4,2,4,2,2,2]]
    print("False -",checkGameOver(arr))
