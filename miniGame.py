import pygame
import random
import time
pygame.init()
pygame.font.init()
pygame.mixer.init()





#colro stuff
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (240, 10, 10)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
textColor = RED
def rainbowText():
    global textColor
    global RED
    global BLUE
    global GREEN
    global YELLOW
    global BLACK
    global WHITE

    if textColor == RED:
        textColor = BLUE
    elif textColor == BLUE:
        textColor = GREEN
    elif textColor == GREEN:
        textColor = RED



#textual stuff for intro and outro
font = pygame.font.SysFont('Comic Sans MS', 70)
font2 = pygame.font.SysFont('Comic Sans MS',45 )

introText = font.render("SAVING PRIVATE SLIME",True,(BLACK))
introSubText = font2.render("press RETURN to begin",True,(BLACK))
endText = font.render("GAME OVER", True, (WHITE))
endSubText = font.render("", True, (WHITE))
endSubSubText = font.render("", True, (textColor))

player1won = font2.render("RED WINS!", True,(RED))
player2won = font2.render("BLUE WINS!", True,(BLUE))


##CREDITS
ErickCredit = font.render("ERICK TORRES", True, (RED))
erick_Text = font2.render("Lead Programmer/ Sprite Designer", True, (WHITE))

ArturoCredit = font.render("ARTURO SANCHEZ", True, (PURPLE))
arturo_Text = font2.render("Programmer/ Music", True, (WHITE))

MemoText = font.render("GUILLERMO NIEVES", True, (GREEN))
memo_Text = font2.render("Lead Sprite Designer", True, (WHITE))

JesusCredit = font.render("JESUS RAMOS", True, (BLUE))
jesus_Text = font2.render("Sound FX", True, (WHITE))


#idk
luck = random.randrange(0,1)
image = pygame.image
screenWidth = (600,600)
clock = pygame.time.Clock()
timer  = 0
clockTimer = 2400
aftermath = 0
display = pygame.display
keys = pygame.key.get_pressed()
fallTrigger = False
dropNumber = 0
random.seed(time.time())

#scoreboard
myfont = pygame.font.SysFont('Comic Sans MS', 75)




#window and fps
win=pygame.display.set_mode(screenWidth)
pygame.display.set_caption("Collect-a-Coin")
#frames
FPS = 60
introFPS = 10
endingFPS = 15

#music
intromusicqueue = 0
musicqueue = 0
music = ["startupgame.mp3","opt4.mp3","last10.mp3"]

#for player one
playeroneX = 25
playeroneY = 481
isJump1 = False
jumpCount1 = 10
left1 = False
right1 = False
walkCount1 = 0
walkRight1 = image.load('R1.png')
walkLeft1 = image.load('L1.png')
char1 = image.load('Idle1.png')
player1pts = 0
#for player player two
playertwoX = 425
playertwoY = 481
isJump2 = False
jumpCount2 = 10
left2 = False
right2 = False
walkCount2 = 0
walkRight2 = image.load('R2.png')
walkLeft2 = image.load('L2.png')
char2 = image.load('Idle2.png')
player2pts = 0
#shared properties w/ p1 and p2
width = 20
height = 30
vel = 9
jumpHeight = .5
#jumpHeight must be a number less than 1 but more than 0

#position for the 'coin'
coinboxX = 275
coinboxY = 133
boxwidth = 40
boxheight = 60
startMovingL = True
startMovingR = False
boxLeft= False
boxRight = False
boxvel = 3
boxR = image.load('BoxR.png')
boxL = image.load('BoxL.png')
temp = image.load('BoxIdle.png')
coin = image.load('slime.png')
coinX = coinboxX
coinY = coinboxY

##COINCOINCOINCOIN
coinspawnX = playeroneX + 10
coinspawnY = playeroneY
coinMovingR = False
coinMovingL = False
isJump3 = False
coinJumpCount1 = 10
coinCollected = False


"""
coin will pop out from the (coinboxX, coinboxY)
THERE WILL ONLY BE ONE COIN INN THE SCREEN AT THE TIME
Coin bounces off the edge when it collides on the edge
when the coin collides within the range of either player, it will add
1 to the one of the player's point
"""
#colors :)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (240,10,10)
YELLOW = (255,255,0)
BLUE = (0,0,255)

bg = image.load('abg1.png')
          #load('abg2.png'),
         # load('abg3.png'),
         # load('abg4.png'),
         # load('abg5.png'),
         # load('abg6.png'),
         # load('abg7.png'),
         # load('abg8.png'),
         # load('abg9.png')]

##
class sprite:

    def __init__(self,x,y, name):
        self.x=x

        self.y=y

        self.image = pygame.display.load(name)

        self.rect = self.image.get_rect()

    def render(self):
        window.blit(self.image, (self.x,self.y))
##sprite(pos,image)
##

screenColor = RED

def rainbowscreen():
    global screenColor
    global RED
    global BLUE
    global GREEN
    global YELLOW
    global BLACK
    global WHITE

    if screenColor == RED:
        screenColor = BLUE
    elif screenColor == BLUE:
        screenColor = GREEN
    elif screenColor == GREEN:
        screenColor = YELLOW
    elif screenColor == YELLOW:
        screenColor = RED







def animationRefresh():
    global walkCount1
    global walkCount2
    global startMovingL
    global startMovingR
    global coinboxX
    global text
    global boxL
    global boxR
    global coinspawnX
    global coinspawnY
    global isJump3
    global coinJumpCount
    win.blit(bg, (0,0))
#PLAYER 1 ANIMATIONS
    if walkCount1 + 1 >= 6:
        walkCount1 = 0

    if left1:
        win.blit(walkLeft1, (playeroneX,playeroneY))
        walkCount1 += 1
    elif right1:
        win.blit(walkRight1, (playeroneX,playeroneY))
        walkCount1 += 1
    else:
        win.blit(char1, (playeroneX, playeroneY))
        walkCount1 = 0

#PLAYER 2 ANIMATIONS
    if walkCount2 + 1 >= 27:
        walkCount2 = 0
    if left2:
        win.blit(walkLeft2, (playertwoX,playertwoY))
        walkCount2 += 1
    elif right2:
        win.blit(walkRight2, (playertwoX,playertwoY))
        walkCount2 += 1
    else:
        win.blit(char2, (playertwoX,playertwoY))
        walkCount2 = 0

#Coinbox Movement from LEFT to RIGHT
         ##LEFT
    if startMovingL:
        coinboxX -= boxvel
        win.blit(boxL,(coinboxX,coinboxY))
        if coinboxX <= -35:
            startMovingL = False
            startMovingR = True
            boxRight = True
            boxLeft = False
        ##RIGHT
    if startMovingR:
        coinboxX += boxvel
        win.blit(boxR,(coinboxX,coinboxY))
        if coinboxX >= 500:
            startMovingR = False
            startMovingL = True
            boxRight = False
            boxLeft = True



runIntro = True
runEnding = False

#intro

while runIntro:

    if musicqueue == 0:
        pygame.mixer.music.load(music[musicqueue])
        pygame.mixer.music.play(-1)
        musicqueue += 1


    display.set_caption("PRESS RETURN")
    clock.tick(introFPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runIntro = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        runIntro =  False

    rainbowscreen()
    win.fill(screenColor)
    win.blit(introText, (300 - introText.get_width() // 2, 240 - introText.get_height() // 2))
    win.blit(introSubText, (370 - introText.get_width() // 2, 300 - introText.get_height() // 2))
    display.update()

#main game

musicqueue = 2;

run = True
while run:

    clock.tick(FPS)
    display.set_caption("SLIME COLLECTION")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()


#music queues
    if musicqueue == 2:
        pygame.mixer.music.load(music[musicqueue - 1])
        pygame.mixer.music.play(-1)
        musicqueue += 1
    if musicqueue == 4:
        pygame.mixer.music.stop()
        pygame.mixer.music.load(music[musicqueue - 2])
        pygame.mixer.music.play(-1)
        musicqueue += 1




#PLAYER ONE CONTROLS : UP,LEFT,RIGHT
    if keys[pygame.K_LEFT] and playeroneX > -37:
        playeroneX -= vel
        left1 = True
        right1 = False
    elif keys[pygame.K_RIGHT]and playeroneX < 540 - width - vel:
        playeroneX += vel
        left1 = False
        right1 = True
    else:
        left1 = False
        right1 = False
        walkCount1 = 0
    if not (isJump1):
        if keys[pygame.K_UP]:
               isJump1 = True
    else:
        if jumpCount1 >= -10:
            playeroneY -= (jumpCount1 * abs(jumpCount1)) * jumpHeight
            jumpCount1 -= 1
        else:
            isJump1 = False
            jumpCount1 = 10

#PLAYER TWO CONTROLS : W,A,D
    if keys[pygame.K_a] and playertwoX>-35:
        playertwoX -= vel
        left2 = True
        right2 = False

    if keys[pygame.K_d] and playertwoX<540-width-vel:
        playertwoX += vel
        left2 = False
        right2 = True


    else:
        left2 = False
        right2 = False
        walkCount2 = 0
    if not (isJump2):
        if keys[pygame.K_w]:
            isJump2 = True
    else:

        if jumpCount2 >= -10:
            playertwoY -= (jumpCount2 * abs(jumpCount2)) * jumpHeight
            jumpCount2 -= 1
        elif playertwoY >= playeroneY - 49 and playertwoY <= playeroneY - 50:
            if playertwoX >= playeroneX -10 and playertwoX <= playeroneX +10 :
                playertwoY = playeroneY -49
        else:
            isJump2 = False
            jumpCount2 = 10

    win.fill((0,0,0))

#this is the timer
    clockTimer -= 1
    if clockTimer == 400:
        print("fasteeer")##replace(stop the other music, play the) faster music
        musicqueue = 4
    if clockTimer == 0:
        print("done") # stop the music
        run = False

    animationRefresh()
##COIN drop and collection
    if coinCollected == False:
        coinX = coinboxX
        coinY = coinboxY
        if dropNumber == 0:
            #generates random num to determine how long before coin drops
            dropTimer = random.randint(30,120)
        if dropNumber <= 1:
            dropNumber += 1
        if startMovingR == True and coinCollected == False:
            win.blit(coin ,(coinX + 45,coinY + 10))
        if startMovingL == True and coinCollected == False:
            win.blit(coin ,(coinX + 45,coinY + 10))
        if dropTimer >= 0:
            dropTimer -= 1
        if dropTimer == 0:
            fallTrigger = True
#starts the coin drop
    if fallTrigger == True:
        coinCollected = True
        if coinY <= 530 and dropTimer <= 0:
            coinY += 5
            win.blit(coin, (coinX + 45, coinY + 10))
        if coinY >= 530:
            win.blit(coin, (coinX + 45, coinY +10))

#player one collection
    if playeroneX <= coinX + 30 and playeroneX >= coinX - 20:
        if playeroneY <= coinY - 52 and playeroneY >= coinY - 100:
            coinCollected = False
            fallTrigger = False
            dropNumber = 0
            player1pts += 1

#player two collection
    if playertwoX <= coinX + 30 and playertwoX >= coinX - 20:
        if playertwoY <= coinY - 52 and playertwoY >= coinY - 100:
            coinCollected = False
            fallTrigger = False
            dropNumber = 0
            player2pts += 1

#player one score card
    textsurface1 = myfont.render(str(player1pts), False, (0, 0, 126))
    win.blit(textsurface1,(45, 60))
#player two score card
    textsurface2 = myfont.render(str(player2pts), False, (0, 0, 126))
    win.blit(textsurface2,(525, 60))

    display.update()

runEnding = True

#outro

musicqueue = 0

while runEnding: #ENDING SCEN WHICH DISPLAYS WINNER and POINTS
    rainbowText()
    itsADraw = font2.render("IT'S A DRAW!", True, (textColor))
    if musicqueue == 0:
        pygame.mixer.music.load(music[musicqueue])
        pygame.mixer.music.play(-1)
        musicqueue += 1

    display.set_caption("GAME OVER")
    clock.tick(endingFPS)
    win.fill(BLACK)
    win.blit(endText, (300 - endText.get_width() //
                       2, 240 - endText.get_height() // 2))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runEnding = False
    keys = pygame.key.get_pressed()
    clockTimer -= 1
    rainbowText()
    if int(player1pts) > int(player2pts):
        win.blit(player1won, (440 - introText.get_width() //2, 300 - introText.get_height() // 2))
    if int(player2pts) > int(player1pts):
        win.blit(player2won, (440 - introText.get_width() // 2, 300 - introText.get_height() // 2))
    if int(player1pts) == int(player2pts):
        win.blit(itsADraw, (440 - introText.get_width() // 2, 300 - introText.get_height() // 2))
    if clockTimer == 100:
        runEnding = False
    if keys[pygame.K_RETURN] and clockTimer > 1000:
        pygame.quit()
    pygame.display.flip()
runCredits = True
#while runCredits:

