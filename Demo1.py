import pygame, sys, pygame.mixer, random
# from constants import *
from logic import *

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

Score =0
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

        if event.type == pygame.KEYDOWN and GameOver: #reset game after "Game Over"
            Score =0
            changed = False
            GameOver = False
            arr = clear()
            insNum(arr, first=True)
            for i in range(1, startNumbers):
                if i < xCount * yCount:
                    insNum(arr, first=False)

        if event.type == pygame.KEYDOWN and not GameOver:
            changed = False
            if event.key == pygame.K_r: #reset game
                changed = False
                GameOver = False
                arr = clear()
                insNum(arr, first=True)
                for i in range(1, startNumbers):
                    if i < xCount * yCount:
                        insNum(arr, first=False)

            if event.key == pygame.K_RIGHT:
                arr = horizFlip(arr)
                for c in range(0, len(arr)): # образец
                    row = arr[c]
                    arr[c], tmpScore = act(row)
                    ScoreAdd += tmpScore
                    if not arr[c] == row:
                        changed = True
                arr = horizFlip(arr)

            if event.key == pygame.K_LEFT:
                for c in range(0, len(arr)): # образец
                    row = arr[c]
                    arr[c], tmpScore = act(row)
                    ScoreAdd += tmpScore
                    #print(row,arr[c])
                    if not arr[c] == row:
                        changed = True

            if event.key == pygame.K_UP:
                arr = centerFlip(arr)
                for c in range(0, len(arr)): # образец
                    row = arr[c]
                    arr[c], tmpScore = act(row)
                    ScoreAdd += tmpScore
                    if not arr[c] == row:
                        changed = True
                arr = centerFlip(arr)

            if event.key == pygame.K_DOWN:
                arr = centerFlip(arr)
                arr = horizFlip(arr)
                for c in range(0, len(arr)): # образец
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
                #print("ins")
                changed = False

            # Быстрый гейм овер для 4х4
            if event.key == pygame.K_g and xCount == 4 and yCount == 4:
                arr = [[2,4,2,4],[4,2,4,2],[2,4,2,4],[4,2,4,2]]

        GameOver = checkGameOver(arr)
        Score += ScoreAdd

    screen.fill(bgColour)

    # рисование окна
    pygame.display.set_caption("2048 : "+ str(Score))
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
        #print('Game Over')
        fnt = pygame.font.SysFont(fontName, fontSize+15)
        GameOverText1 = fnt.render("    Game Over!    ", 1,(255,0,0),(0,0,0))
        GameOverTxtSize1 = GameOverText1.get_size()
        screen.blit(GameOverText1, (windowSize[0]//2-GameOverTxtSize1[0]//2,windowSize[1]//2-GameOverTxtSize1[1]//2))

        fnt = pygame.font.SysFont(fontName, fontSize+7)
        GameOverText2 = fnt.render("  Your score - "+str(Score)+"  ", 1,(255,0,0),(0,0,0))
        GameOverTxtSize2= GameOverText2.get_size()
        screen.blit(GameOverText2, (windowSize[0]//2-GameOverTxtSize2[0]//2,windowSize[1]//2+GameOverTxtSize1[1]//2))

        fnt = pygame.font.SysFont(fontName, fontSize-10)
        GameOverText3 = fnt.render("     press any key to continue...     ", 1,(255,0,0),(0,0,0))
        GameOverTxtSize3= GameOverText3.get_size()
        screen.blit(GameOverText3, (windowSize[0]//2-GameOverTxtSize3[0]//2,windowSize[1]//2+GameOverTxtSize1[1]//2+GameOverTxtSize2[1]))

    pygame.display.update()