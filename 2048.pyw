import pygame, sys, pygame.mixer

import random
from constants import *

def clear():
    arr = []
    for y in range(yCount):
        row = []
        for x in range(xCount):
            # print(x+y)
            row.append(0)
        arr.append(row)
    return arr

def insNum(arr, first=True):
    if first:
        num = 2
    else:
        if random.randint(1, 4) == 4:
            num = 4
        else:
            num = 2

    x = random.randint(1, xCount) - 1
    y = random.randint(1, yCount) - 1

    if first:
        arr[y][x] = num

    else:
        while not arr[y][x] == 0:
            x = random.randint(1, xCount) - 1
            y = random.randint(1, yCount) - 1
        arr[y][x] = num


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
    # if res == [0]:
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
    # if res == [0]:
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
    Score = 0
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
            # print(c,"*",res)
            #print(c,"-",res[0:c],[res[c]*res[c+1]],clearLeft(res[c+2:]))
            if c == 0:
                res = [res[c] * 2] + clearLeft(res[c + 2:])
                Score += res[c]
            elif c > 0 and c < len(res) - 2:
                #print("!")
                res = res[0:c] + [res[c] * 2] + clearLeft(res[c + 2:])
                Score += res[c]
            else:
                pass
                res = res[0:c] + [res[c] * 2]
                Score += res[c]
            #print("**",res)
            c += 1

    res = addRightZero(res, arrLen)
    return res, Score

def getCol(arr, colNum):
    res = []
    for y in range(len(arr)):
        res.append(arr[y][colNum])
    return res

def putCol(arr, colNum, col):
    res = arr[:]
    # print(colNum)
    # print(col)
    for y in range(len(col)):
        #print(col,y)

        res[y][colNum] = col[y]
    return res

def horizFlip(arr):
    res = []
    for row in arr:
        # print('+', row)
        # res.append(list(reversed(row)))
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
    for y in range(len(arr)):
        for x in range(len(arr[y])):
            if arr[y][x] == 0:
                GameOver = False
                return GameOver
    for y in range(len(arr) - 1):
        for x in range(len(arr[y]) - 1):
            if arr[y][x] == arr[y + 1][x] or arr[y][x] == arr[y][x + 1]:
                GameOver = False
                return GameOver
                # print(x,y)
    return GameOver

if __name__ == "__ma!in__":
    arr2 = [0, 2, 0, 2, 0, 2, 0, 2, 8, 8, 0]
    # arr2 = [2,2,0,0]
    print("Input            - ", arr2)
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

pygame.init()
pygame.mixer.init()
windowSize = ((xCount + 1) * borderWidth + xCount * edge, (xCount + 1) * borderWidth + xCount * edge)
screen = pygame.display.set_mode(windowSize)

clock = pygame.time.Clock()
'''
arr = []
c = 1
for y in range(yCount):
    row = []
    for x in range(xCount):
        # row.append(2 ** random.randint(1,10))
        if c < 11:
            #print(x+y)
            row.append(2 ** c)
            c += 1
        else:
            row.append(2)
    arr.append(row)
'''
# arr = [[2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 0, 0]]

Score = 0
GameOver = False
arr = clear()
insNum(arr, first=True)
for i in range(1, startNumbers):
    if i < xCount * yCount:
        insNum(arr, first=False)

while 1:

    clock.tick(100)
    ScoreAdd = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN and GameOver:  # reset game after "Game Over"
            Score = 0
            changed = False
            GameOver = False
            arr = clear()
            insNum(arr, first=True)
            for i in range(1, startNumbers):
                if i < xCount * yCount:
                    insNum(arr, first=False)

        if event.type == pygame.KEYDOWN and not GameOver:
            changed = False
            if event.key == pygame.K_r:  # reset game
                changed = False
                GameOver = False
                arr = clear()
                insNum(arr, first=True)
                for i in range(1, startNumbers):
                    if i < xCount * yCount:
                        insNum(arr, first=False)

            if event.key == pygame.K_RIGHT:
                arr = horizFlip(arr)
                for c in range(0, len(arr)):  # образец
                    row = arr[c]
                    arr[c], tmpScore = act(row)
                    ScoreAdd += tmpScore
                    if not arr[c] == row:
                        changed = True
                arr = horizFlip(arr)

            if event.key == pygame.K_LEFT:
                for c in range(0, len(arr)):  # образец
                    row = arr[c]
                    arr[c], tmpScore = act(row)
                    ScoreAdd += tmpScore
                    # print(row,arr[c])
                    if not arr[c] == row:
                        changed = True

            if event.key == pygame.K_UP:
                arr = centerFlip(arr)
                for c in range(0, len(arr)):  # образец
                    row = arr[c]
                    arr[c], tmpScore = act(row)
                    ScoreAdd += tmpScore
                    if not arr[c] == row:
                        changed = True
                arr = centerFlip(arr)

            if event.key == pygame.K_DOWN:
                arr = centerFlip(arr)
                arr = horizFlip(arr)
                for c in range(0, len(arr)):  # образец
                    row = arr[c]
                    arr[c], tmpScore = act(row)
                    ScoreAdd += tmpScore
                    if not arr[c] == row:
                        changed = True
                arr = horizFlip(arr)
                arr = centerFlip(arr)

            if event.key == pygame.K_q:
                sys.exit()

            if changed:
                insNum(arr, first=False)
                # print("ins")
                changed = False

            # Быстрый гейм овер для 4х4
            if event.key == pygame.K_g and xCount == 4 and yCount == 4:
                arr = [[2, 4, 2, 4], [4, 2, 4, 2], [2, 4, 2, 4], [4, 2, 4, 2]]

        GameOver = checkGameOver(arr)
        Score += ScoreAdd

    screen.fill(bgColour)

    # рисование окна
    pygame.display.set_caption("2048 : " + str(Score))
    for y in range(yCount):
        for x in range(xCount):
            pygame.draw.rect(screen, rColors[arr[y][x]],
                             ((x + 1) * borderWidth + x * edge,
                              (y + 1) * borderWidth + y * edge,
                              edge,
                              edge), 0)
            if not arr[y][x] == 0:
                fnt = pygame.font.SysFont(fontName, fontSize)
                txt = fnt.render(str(arr[y][x]), 1,
                                 tColors[arr[y][x]],
                                 rColors[arr[y][x]])
                txtSize = txt.get_size()
                screen.blit(txt, ((x + 1) * borderWidth + (x + 0.5) * edge - txtSize[0] / 2,
                                  (y + 1) * borderWidth + (y + 0.5) * edge - txtSize[1] / 2))
    if GameOver:
        # print('Game Over')
        fnt = pygame.font.SysFont(fontName, fontSize + 15)
        GameOverText1 = fnt.render("    Game Over!    ", 1, (255, 0, 0), (0, 0, 0))
        GameOverTxtSize1 = GameOverText1.get_size()
        screen.blit(GameOverText1,
                    (windowSize[0] // 2 - GameOverTxtSize1[0] // 2, windowSize[1] // 2 - GameOverTxtSize1[1] // 2))

        fnt = pygame.font.SysFont(fontName, fontSize + 7)
        GameOverText2 = fnt.render("  Your score - " + str(Score) + "  ", 1, (255, 0, 0), (0, 0, 0))
        GameOverTxtSize2 = GameOverText2.get_size()
        screen.blit(GameOverText2,
                    (windowSize[0] // 2 - GameOverTxtSize2[0] // 2, windowSize[1] // 2 + GameOverTxtSize1[1] // 2))

        fnt = pygame.font.SysFont(fontName, fontSize - 10)
        GameOverText3 = fnt.render("     press any key to continue...     ", 1, (255, 0, 0), (0, 0, 0))
        GameOverTxtSize3 = GameOverText3.get_size()
        screen.blit(GameOverText3, (windowSize[0] // 2 - GameOverTxtSize3[0] // 2,
                                    windowSize[1] // 2 + GameOverTxtSize1[1] // 2 + GameOverTxtSize2[1]))

    pygame.display.update()