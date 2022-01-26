import opc, pygame, time, math

WIDTH = 60
HEIGHT = 80
SCALE = 4
NUMLEDS = WIDTH*HEIGHT
CLIENT = opc.Client("199.17.162.78:7890")
SCREEN = pygame.display.set_mode((WIDTH*SCALE, HEIGHT*SCALE))
ORIENTATION = 1 # 0 regular, 1 to flip
pixels = [ (0,0,0) ] * NUMLEDS
test = 0
x_pos = 0
GAMESCREEN = None

pygame.font.init()
myfont = pygame.font.Font('/home/sbada/Desktop/FadeCandyPy/Project/COMIC.TTF', 32)
"""
    x_pos = (x_pos+1) 
    pixels = [ (0,0,0) ] * NUMLEDS
    pixels[((x_pos*WIDTH) % NUMLEDS)+x_pos//HEIGHT] = (255,255,255)
    CLIENT.put_pixels(pixels)
    time.sleep(0.05)
"""
def drawRectangleBorder(x,y,width,height,col):
    pygame.draw.line(GAMESCREEN,col,(x,y),(x+width,y))
    pygame.draw.line(GAMESCREEN,col,(x,y),(x,y+height))
    pygame.draw.line(GAMESCREEN,col,(x+width,y),(x+width,y+height))
    pygame.draw.line(GAMESCREEN,col,(x,y+height),(x+width,y+height))

def drawScreenBorder(col):
    width = WIDTH-1
    height = HEIGHT-1
    pygame.draw.line(SCREEN,col,(0,0),(0+width,0))
    pygame.draw.line(SCREEN,col,(0,0),(0,0+height))
    pygame.draw.line(SCREEN,col,(0+width,0),(0+width,0+height))
    pygame.draw.line(SCREEN,col,(0,0+height),(0+width,0+height))

while True:
    test+=0.001
    ORIENTATION = math.floor(test % 1.99)
    if ORIENTATION == 0:
        GAMESCREEN = pygame.Surface((WIDTH,HEIGHT))
        GAMESCREEN.fill((0,0,0))
        pygame.draw.circle(GAMESCREEN,(0,100,100),(15,15),6)
        pygame.draw.circle(GAMESCREEN,(0,100,100),(40,40),20)
        pygame.transform.scale(GAMESCREEN, (WIDTH*SCALE, HEIGHT*SCALE))
        textsurface = myfont.render('Eric', False, (255, 100, 100))
        x_pos=(x_pos+0.1) % WIDTH
        GAMESCREEN.blit(textsurface,(-WIDTH+x_pos*2,20))
        SCREEN.blit(GAMESCREEN, (0,0))
        drawScreenBorder((255,0,0))
        pygame.display.flip()

        for column in range(0,HEIGHT):
            for row in range(0,WIDTH):
                pixels[(WIDTH-row-1)+(column)*WIDTH] = GAMESCREEN.get_at((row,column))[0:3]
    else:
        GAMESCREEN = pygame.Surface((HEIGHT,WIDTH))
        GAMESCREEN.fill((0,0,0))
        pygame.draw.circle(GAMESCREEN,(0,100,100),(15,15),6)
        pygame.draw.circle(GAMESCREEN,(0,100,100),(40,40),20)
        pygame.transform.scale(GAMESCREEN, (WIDTH*SCALE, HEIGHT*SCALE))
        textsurface = myfont.render('Eric', False, (255, 100, 100))
        x_pos=(x_pos+0.1) % HEIGHT
        GAMESCREEN.blit(textsurface,(-HEIGHT+x_pos*2,20))
        drawScreenBorder((255,0,0))
        pygame.display.flip()
        SCREEN.blit(GAMESCREEN, (0,0))

        for column in range(0,HEIGHT):
            for row in range(0,WIDTH):
                pixels[row+column*WIDTH] = GAMESCREEN.get_at((column,row))[0:3]
    CLIENT.put_pixels(pixels)