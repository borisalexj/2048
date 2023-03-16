"""
arr = [[0, 4, 8, 12], [1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15]]
print(arr)
print([arr[0][0],arr[1][0],arr[2][0],arr[3][0]])
print(list(reversed([arr[0][0],arr[1][0],arr[2][0],arr[3][0]])))
print(arr[0:len(arr)][0])
"""

def clearLeft(arr):
    res = []
    # print("----", res, res[0])
    #if res == [0]:
    #    res = []
    if not len(arr) == 0:
        c = 0
        while c < len(arr) and arr[c] == 0:
            if not arr[c] == 0:
                res.append(arr[c])
            c += 1
        #print(c)
        res = res + arr[c:]
    return res


def clearRight(arr):
    res = arr[:]
    # print("----", res, res[0])
    #if res == [0]:
    #    res = []
    while len(res) > 0 and res[len(res) - 1] == 0:
        res.pop()
    return res

def addRightZero(arr, ln):
    res = arr[:]
    while len(res) < ln:
        res.append(0)
    return res

def act(arr):
    arrLen = len(arr)
    res = clearLeft(arr)
    c = 0
    while c < len(res) - 1:
        # print(res)
        if res[c + 1] == 0:
            res = res[0:c + 1] + clearLeft(res[c + 1:])
        elif not res[c] == res[c + 1]:
            c += 1
        else:
            #print(c,"*",res)
            #print(c,"-",res[0:c],[res[c]*res[c+1]],clearLeft(res[c+2:]))
            if c == 0:
                res = [res[c] * res[c + 1]] + clearLeft(res[c + 2:])
            elif c > 0 and c < len(res) - 2:
                #print("!")
                res = res[0:c] + [res[c] * res[c + 1]] + clearLeft(res[c + 2:])
            else:
                pass
                res = res[0:c] + [res[c] * res[c + 1]]
            #print("**",res)
            c += 1

    res = addRightZero(res, arrLen)
    return res

if __name__ == "__main__":
    arr2 = [0, 2, 0, 2, 0, 2, 0, 2, 8, 8, 0]
    # print(list(reversed(arr2)))
    #arr2 = [2,2,0,0]
    print("Input            - ", arr2)
    print("Input reversed   - ", list(reversed(arr2)))
    print("result clearLeft - ", clearLeft(arr2))
    print("result clear+add - ", addRightZero(clearLeft(arr2), len(arr2)))
    print("result act       - ", act(arr2))
    print("---")
    print("arr2      - ", arr2)
    print("result2 L - ", clearLeft(arr2))
    arr3 = [0, 0]
    print("arr3 - ", arr3)
    print("result2 L - ", clearLeft(arr3))
    print("result2 R - ", clearRight(arr3))
    arr3 = [0, 2, 0]
    print("arr3 - ", arr3)
    print("result2 L - ", clearLeft(arr3))
    print("result2 R - ", clearRight(arr3))
    arr3 = [0, 0, 2, 0, 2, 0, 0]
    print("arr3 - ", arr3)
    print("result2 L - ", clearLeft(arr3))
    print("result2 R - ", clearRight(arr3))
    

