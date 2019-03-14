from pygame_functions import *
# This will import pygame functions
#Pressing Escape key will close window

screenSize(1000, 750) #Feel free to change the screen size  
setBackgroundImage("moon.jpg") #Change this to an image file location on your computer. 


rocket = makeSprite("trumpii.jpg") #Change this to an image file location on your computer. 
addSpriteImage(rocket, "trumpii.jpg") #Change this to an image file location on your computer. 


xPos = 500 #starting x position
yPos = 320 #starting y position
xSpeed = 0 #Initial starting x pos speed. Set it to 100 to have some fun :p
ySpeed = 0 #Initial starting y pos speed.
moveSprite(rocket, xPos, yPos) #To move Mr Trump!
showSprite(rocket) #To show Mr Trump

while True: #While loop to get the game going
    if keyPressed("up"): #Pressing up key will move Trump up. Customize it as you see fit.
        changeSpriteImage(rocket, 1)
        transformSprite(rocket, 0, 1)
        ySpeed -= 2

    elif keyPressed("down"): #Pressing down key will move Trump down. Customize it as you see fit.
        changeSpriteImage(rocket, 1)
        transformSprite(rocket, 180, 1)
        ySpeed += 2

    elif keyPressed("right"):
        changeSpriteImage(rocket, 1)
        transformSprite(rocket, 90, 1)
        xSpeed += 2

    elif keyPressed("left"):
        changeSpriteImage(rocket, 1)
        transformSprite(rocket, -90, 1)
        xSpeed -= 2

    else:
        changeSpriteImage(rocket, 0)

    xPos += xSpeed
    if xPos > 960:
        xPos = -100
    elif xPos < -100:
        xPos = 960
#This will reset x position of trump to ensure his position comes back in frame if he moves out of screen
        
    yPos += ySpeed
    if yPos > 700:
        yPos = -100
    elif yPos < -100:
        yPos = 700
##This will reset y position of trump to ensure his position comes back in frame if he moves out of screen
        
    moveSprite(rocket, xPos, yPos)

    tick(30) #Controls the speed of Mr Trump



