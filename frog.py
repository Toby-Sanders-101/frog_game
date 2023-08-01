import pygame
import sys
sys.path.append('/usr/Modules/')
from time import sleep

pygame.init()
gameDisplay = pygame.display.set_mode((800,400))
pygame.display.set_caption('Wizard Frog')
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.Font(None,50)
frog1 = pygame.image.load('wizard-toad-a.png')
frog2 = pygame.image.load('wizard-toad-b.png')
frog3 = pygame.image.load('wizard-toad-b2.png')
skateboard = pygame.image.load('skateboard.png')
skateboard2 = pygame.image.load('skateboard2.png')
tree2 = pygame.image.load('tree2.png')
house = pygame.image.load('house.png')
bird = pygame.image.load('bird.png')

black = (0,0,0)
blue = (50,50,255)
yellow = (255,255,0)

def square():
	global x
	global gone
	global speed
	global score
	if gone==True:
		x = 800
	x -= int(speed)
	gone = False
	if x<-60:
		gone = True
		speed += 0.5
		score += 1
	gameDisplay.blit(bird,(x,250))

def treeConfig2():
	global treeX2
	global treeGone2
	global moreTrees
	if treeGone2==True:
		treeX2 = 800+550
	treeX2 -= 0+speed/2
	treeX2 = int(treeX2)
	treeGone2 = False
	if treeX2<-100:
		treeGone2 = True
	gameDisplay.blit(tree2,(treeX2,225))
	gameDisplay.blit(tree2,(treeX2-60,225))
	gameDisplay.blit(tree2,(treeX2-200,225))
	gameDisplay.blit(tree2,(treeX2-260,225))
	gameDisplay.blit(house,(treeX2-350,195))
	gameDisplay.blit(house,(treeX2-450,195))
	gameDisplay.blit(tree2,(treeX2-550,225))
	if treeX2<550: 
		moreTrees = True

def treeConfig():
	global treeX
	global treeGone
	global moreTrees
	if treeGone==True:
		treeX = 800+550
	treeX -= 0+speed/2
	treeX = int(treeX)
	treeGone = False
	if treeX<-100:
		treeGone = True
		moreTrees = False
	gameDisplay.blit(tree2,(treeX,225))
	gameDisplay.blit(tree2,(treeX-60,225))
	gameDisplay.blit(tree2,(treeX-260,225))
	gameDisplay.blit(tree2,(treeX-200,225))
	gameDisplay.blit(house,(treeX-300,195))
	gameDisplay.blit(tree2,(treeX-500,225))
	gameDisplay.blit(tree2,(treeX-550,225))

def draw():
	global when
	global jump
	gameDisplay.fill(black)
	pygame.draw.rect(gameDisplay,blue,(0,0,800,325))
	pygame.draw.circle(gameDisplay,yellow,(780,20),60)
	treeConfig2()
	if moreTrees==True:
		treeConfig()
	if jump==False:
		gameDisplay.blit(frog1,(100,250))
	else:
		when += speed/4
		if when<51:
			gameDisplay.blit(frog2,(100,int(250-when*2)))
		if when<100 and when>50:
			gameDisplay.blit(frog3,(100,int(80+when*2)))
		if when>99:
			jump = False
			when = 0
	gameDisplay.blit(skateboard,(80,265))
	scoretxt = font.render(str(score),True,black,blue)
	gameDisplay.blit(scoretxt,(390,120))
	pygame.draw.line(gameDisplay,(255,255,255),(30,265),(70,265),2)
	pygame.draw.line(gameDisplay,(255,255,255),(40,275),(70,275),2)
	pygame.draw.line(gameDisplay,(255,255,255),(30,285),(70,285),2)

def move():
	global jump
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if when==0:
				jump = True

def check():
	global alive
	if x<164 and x>100:
		if when<16 or when>70:
			alive = False

def main():
	while alive:
		draw()
		move()
		square()
		check()
		pygame.display.update()
		clock.tick(60)
	again()

def again():
	global score
	global alive
	global jump
	global gone
	global when
	global speed
	global treeGone2
	global treeGone
	global moreTrees
	sleep(1)
	treeGone2 = True
	treeGone = True
	moreTrees = False
	alive = True
	jump = False
	gone = True
	when = 0
	speed = 4
	score = 0
	intro()
	main()

def introDraw():
	gameDisplay.fill(black)
	pygame.draw.rect(gameDisplay,blue,(0,0,800,325))
	pygame.draw.circle(gameDisplay,yellow,(780,20),60)
	gameDisplay.blit(tree2,(i+350,225))
	gameDisplay.blit(tree2,(i+300,225))
	gameDisplay.blit(tree2,(i+250,225))
	gameDisplay.blit(tree2,(i+400,225))
	gameDisplay.blit(tree2,(i+450,225))
	pygame.draw.polygon(gameDisplay,black,((i,325),(i,190),(i+350,325)))
	txt = font.render('Watch out for',True,black,blue)
	txt2 = font.render('the birds!',True,black,blue)
	gameDisplay.blit(txt,(i+560,100))
	gameDisplay.blit(txt2,(i+600,150))
	if introPart==1:
		gameDisplay.blit(skateboard2,(int(10-i/5),int(170-i/2.1)))
		gameDisplay.blit(frog3,(int(30-i/5),int(170-i/2.1)))
	else:
		gameDisplay.blit(frog1,(100,250))
		gameDisplay.blit(skateboard,(80,265))
		pygame.draw.line(gameDisplay,(255,255,255),(30,265),(70,265),2)
		pygame.draw.line(gameDisplay,(255,255,255),(40,275),(70,275),2)
		pygame.draw.line(gameDisplay,(255,255,255),(30,285),(70,285),2)

def intro():
	global i
	global introPart
	introing = True
	i = 0
	introPart = 1
	while introing:
		introDraw()
		i -= 3
		if i==-240:
			introPart = 2
		if i==-600:
			introing = False
		pygame.display.update()
		clock.tick(60)

again()
pygame.quit()
quit
