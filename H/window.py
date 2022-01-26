import opc, pygame, time, math, random, colorsys

WIDTH = 60
HEIGHT = 80
SCALE = 4
WINDOW_WIDTH = WIDTH*SCALE
WINDOW_HEIGHT = HEIGHT*SCALE
NUMLEDS = WIDTH*HEIGHT
CLIENT = opc.Client("199.17.162.78:7890")
SCREEN = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
ORIENTATION = 1 # 0 regular, 1 to flip
pixels = [ (0,0,0) ] * NUMLEDS
test = 0
x_pos = 0
gamescreen = None
default_font = "Project/Kaku.ttf"
timer = 0

def draw_rect_outline(x,y,width,height,col):
    pygame.draw.line(gamescreen,col,(x,y),(x+width,y))
    pygame.draw.line(gamescreen,col,(x,y),(x,y+height))
    pygame.draw.line(gamescreen,col,(x+width,y),(x+width,y+height))
    pygame.draw.line(gamescreen,col,(x,y+height),(x+width,y+height))

def draw_screen_border(col):
    width = WIDTH-1
    height = HEIGHT-1
    pygame.draw.line(SCREEN,col,(0,0),(0+width,0))
    pygame.draw.line(SCREEN,col,(0,0),(0,0+height))
    pygame.draw.line(SCREEN,col,(0+width,0),(0+width,0+height))
    pygame.draw.line(SCREEN,col,(0,0+height),(0+width,0+height))

def draw_text(str,x,y,col,font=default_font):
    pygame.font.init() # you have to call this at the start, 
    myfont = pygame.font.Font(font, 8)
    textsurface = myfont.render(str, False, col)
    gamescreen.blit(textsurface,(x,y))

def draw_line(x1,y1,x2,y2,col):
    pygame.draw.line(gamescreen,col,(x1,y1),(x2,y2))

def hsv2rgb(h, s, v):
    #redesigned to work with 255 instead of 1.0
    return tuple(255*val for val in colorsys.hsv_to_rgb(h/255, s/255, v/255))

while True:
    timer+=1
    if ORIENTATION == 0:
        gamescreen = pygame.Surface((WIDTH,HEIGHT))
        gamescreen.fill((0,0,0))
        pygame.draw.circle(gamescreen,(0,100,100),(15,15),6)
        pygame.draw.circle(gamescreen,(0,100,100),(40,40),20)
        draw_text("Winowona State Univewstity",0,0,(127,0,127))
        SCREEN.blit(pygame.transform.scale(gamescreen, (WINDOW_WIDTH,WINDOW_HEIGHT)),(0,0))
        draw_screen_border((255,255,255))
        pygame.display.flip()

        for column in range(0,HEIGHT):
            for row in range(0,WIDTH):
                pixels[(WIDTH-row-1)+(column)*WIDTH] = gamescreen.get_at((row,column))[0:3]
    else:
        gamescreen = pygame.Surface((HEIGHT,WIDTH))
        draw_screen_border((255,0,0))
        draw_text("Tetris",1,-3,(0,255,255))
        draw_line(1,9,31,9,(0,255,255))
        text_col = hsv2rgb(timer % 255, 255, 255)
        draw_text("Play",3,9+math.sin(math.radians(timer))*1.5,text_col)
        
        #pygame.draw.circle(gamescreen,(129,100,0),(15,15),6)
        pygame.display.flip()
        SCREEN.blit(gamescreen, (0,0))

        for column in range(0,HEIGHT):
            for row in range(0,WIDTH):
                pixels[row+column*WIDTH] = gamescreen.get_at((column,row))[0:3]
    CLIENT.put_pixels(pixels)