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
PURPLE = (190,10,255)
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
font3 = pygame.font.SysFont('Comic Sans MS', 58)
introText = font.render("SAVING PRIVATE SLIME",True,(BLACK))
introSubText = font2.render("press RETURN to begin",True,(BLACK))
endText = font.render("GAME OVER", True, (WHITE))
endSubText = font.render("", True, (WHITE))
endSubSubText = font.render("", True, (textColor))

player1won = font2.render("RED WINS!", True,(RED))
player2won = font2.render("BLUE WINS!", True,(BLUE))

##Controls
playerredtext = font3.render("RED'S CONTROLS",True,(RED))
playerredcontrols = font2.render("Arrow Keys", True,(RED))
playerbluetext = font3.render("BLUE'S CONTROLS", True,(BLUE))
playerbluecontrols = font2.render("WASD Keys", True,(BLUE))
clickReturn = font2.render("Click RETURN when done",True,(WHITE))

##CREDITS
ErickCredit = font3.render("ERICK TORRES", True, (RED))
ErickCreditX = 320
ErickCreditY = -270
erick_Text = font2.render("Lead Programmer/ Sprite Designer", True, (WHITE))
erick_TextX = 320
erick_TextY = -240

ArturoCredit = font3.render("ARTURO SANCHEZ", True, (PURPLE))
ArturoCreditX = 320
ArturoCreditY = -200
arturo_Text = font2.render("Programmer/ Music", True, (WHITE))
arturo_TextX = 320
arturo_TextY = -170

MemoCredit = font3.render("GUILLERMO NIEVES", True, (GREEN))
MemoCreditX = 320
MemoCreditY = -130
memo_Text = font2.render("Lead Sprite Designer", True, (WHITE))
memo_TextX = 320
memo_TextY = -100

JesusCredit = font3.render("JESUS RAMOS", True, (BLUE))
JesusCreditX = 320
JesusCreditY = -60
jesus_Text = font2.render("Sound FX", True, (WHITE))
jesus_TextX = 320
jesus_TextY = -30


scrollVel = 1
def scrollingText():
    global scrollVel
    global ErickCreditX
    global ErickCreditY
    global erick_TextX
    global erick_TextY
    global ArturoCreditX
    global ArturoCreditY
    global arturo_TextX
    global arturo_TextY
    global MemoCreditX
    global MemoCreditY
    global memo_TextX
    global memo_TextY
    global JesusCreditX
    global JesusCreditY
    global jesus_TextX
    global jesus_TextY


    ErickCreditY += scrollVel
    erick_TextY += scrollVel
    ArturoCreditY += scrollVel
    arturo_TextY += scrollVel
    MemoCreditY += scrollVel
    memo_TextY += scrollVel
    JesusCreditY += scrollVel
    jesus_TextY += scrollVel



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
jumpSound = pygame.mixer.Sound("jump.wav")
collisionSound = pygame.mixer.Sound("wallhit.wav")
shootSound = pygame.mixer.Sound("coinshoot.wav")



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

controlsFPS = 15
runControls = True
while runControls:
    win.fill(BLACK)
    clock.tick(controlsFPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runControls = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        runControls = False
    win.blit(playerredtext,(300 - introText.get_width() // 2, 240 - introText.get_height() // 2))
    win.blit(playerredcontrols,(300 - introText.get_width() // 2, 280 - introText.get_height() // 2))
    win.blit(playerbluetext, (300 - introText.get_width() //2, 140 - introText.get_height() // 2))
    win.blit(playerbluecontrols, (300 - introText.get_width() //2, 180 - introText.get_height() // 2))
    win.blit(clickReturn, (300 - introText.get_width() //2, 550 - introText.get_height() // 2))
    display.update()
runIntro = True

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

musicqueue = 2

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
    if keys[pygame.K_LEFT] and playeroneX > -35:
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
               jumpSound.play()
               isJump1 = True

    else:
        if jumpCount1 >= -10:
            playeroneY -= (jumpCount1 * abs(jumpCount1)) * jumpHeight
            jumpCount1 -= 1
        else:
            isJump1 = False
            jumpCount1 = 10

#PLAYER TWO CONTROLS : W,A,D
    if keys[pygame.K_a] and playertwoX>-34:
        playertwoX -= vel
        left2 = True
        right2 = False
    
    if keys[pygame.K_d] and playertwoX<540-width-vel:
        playertwoX += vel
        left2 = False
        right2 = True
    if keys[pygame.K_d] and playertwoX == 515:
        collisionSound.play()
    if keys[pygame.K_a] and playertwoX == -34:
        collisionSound.play()
    if keys[pygame.K_LEFT] and playeroneX == -38:
        collisionSound.play()
    if keys[pygame.K_RIGHT] and playeroneX == 511:
        collisionSound.play()

    else:
        left2 = False
        right2 = False
        walkCount2 = 0
    if not (isJump2):
        if keys[pygame.K_w]:
            jumpSound.play()
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
            shootSound.play()
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
    print(playeroneX,",",playeroneY,"::",playertwoX,",",playertwoY)

    display.update()

runEnding = True

#outro
creditsFPS = 60
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
while runCredits:
    win.fill(BLACK)
    screenWidth = (700,400)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runCredits = False
    clock.tick(creditsFPS)
    scrollingText()
    win.blit(ErickCredit, (ErickCreditX - introText.get_width() // 2, ErickCreditY - introText.get_height() // 2))
    win.blit(erick_Text, (erick_TextX - introText.get_width() // 2, erick_TextY - introText.get_height() // 2))
    win.blit(ArturoCredit, (ArturoCreditX - introText.get_width() // 2, ArturoCreditY - introText.get_height() // 2))
    win.blit(arturo_Text, (arturo_TextX - introText.get_width() // 2, arturo_TextY - introText.get_height() // 2))
    win.blit(MemoCredit, (MemoCreditX - introText.get_width() // 2, MemoCreditY - introText.get_height() // 2))
    win.blit(memo_Text, (memo_TextX - introText.get_width() // 2, memo_TextY - introText.get_height() // 2))
    win.blit(JesusCredit, (JesusCreditX - introText.get_width() // 2, JesusCreditY - introText.get_height() // 2))
    win.blit(jesus_Text, (jesus_TextX - introText.get_width() // 2, jesus_TextY - introText.get_height() // 2))
    display.flip()
