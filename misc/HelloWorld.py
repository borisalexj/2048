import pygame, sys, pygame.mixer

pygame.init()
pygame.mixer.init()
windowSize = (600, 400)
screen = pygame.display.set_mode(windowSize)

mpf = pygame.font.SysFont("Courier", 28)
hw = mpf.render("Hello World", 1, (255, 0, 255), (255, 255, 255))

# hw = pygame.image.load("PS circle.png")

snd = pygame.mixer.Sound("Pluralsight.wav")
# snd2 = pygame.mixer.
hws = hw.get_size()
pygame.mouse.set_visible(False)
x, y = 20, 20
ad = 1
directionX, directionY = 1, 1
clock = pygame.time.Clock()

while 1:
    hw = mpf.render('%4s:%4s' % (str(int(x)), str(int(y))), 1, (255, 0, 255), (255, 255, 255))
    hws = hw.get_size()

    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            mousePos = pygame.mouse.get_pos()
            #print(mousePos)
            x = mousePos[0] - hws[0] / 2
            y = mousePos[1] - hws[1] / 2

        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                x += 5
            if event.key == pygame.K_LEFT:
                x -= 5
            if event.key == pygame.K_UP:
                y -= 5
            if event.key == pygame.K_DOWN:
                y += 5
            if event.key == pygame.K_q:
                sys.exit()
                #print(event.key)

                #if event.key == pygame pygame.K_F4:
                #   sys.exit()

    #print(x,y)

    '''x += ad * directionX
    y += ad * directionY
   # ad +=1
    if x + hws[0] >= windowSize[0] or x <= 0:
        directionX *= -1
        ad =1
    if y + hws[1] >= windowSize[1] or y <= 0:
        directionY *= -1
        ad =1'''

    mousePos = pygame.mouse.get_pos()
    #    print(mousePos)
    #x = mousePos[0] - hws[0] / 2
    #y = mousePos[1] - hws[1] / 2
    if x + hws[0] >= windowSize[0]: x = windowSize[0] - hws[0]; snd.stop(); snd.play()
    if y + hws[1] >= windowSize[1]: y = windowSize[1] - hws[1]; snd.stop();snd.play()
    if x < 0: x = 0; snd.stop(); snd.play()
    if y < 0: y = 0; snd.stop(); snd.play()

    screen.fill((0, 50, 100))
    screen.blit(hw, (x, y))

    pygame.display.update()