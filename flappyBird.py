#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 18:45:36 2019

@author: matthew
"""

import pygame as py
import random as rand
import time

# pygame stuff
py.init()
screenWidth = 600
screenHeight = 700
screen = py.display.set_mode((screenWidth, screenHeight))
py.display.set_caption('Flappy Bird')
clock = py.time.Clock()
fps = 60

textFont = py.font.Font('Raleway-Bold.ttf', 25)

# colours
yellow = (255, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)
gray = (100, 100, 100)
green = (120, 255, 120)
blue = (0, 0, 255)
skyblue = (135, 206, 250)

# player coordinates
playerX = screenWidth / 2
playerY = screenHeight / 2

pipeX = 700
pipeHeight = 300

bottomPipeX = 700
bottomPipeY = pipeHeight + 150

score = 0
highscore = 0
run = False
displayScore = False
sleep = False

def drawText(textFont, surface, displayText, textColor, topLeftX, topLeftY):
    """
    """
    textSurface = textFont.render(displayText, 1, textColor)
    textRect = textSurface.get_rect()
    textRect.topleft = (topLeftX, topLeftY)
    surface.blit(textSurface, textRect)

def drawPipes():
    global pipeX, pipeHeight, bottomPipeX, bottomPipeY, bottomPipeHeight
    py.draw.rect(screen, green, (pipeX, 0, 50, pipeHeight))
    pipeX -= 15
    if pipeX < -50:
        pipeX = 600
        pipeHeight = rand.randint(100, 550)
        
    py.draw.rect(screen, green, (bottomPipeX, bottomPipeY, 50, 700))
    bottomPipeX -= 15
    if bottomPipeX < -50:
        bottomPipeX = 600
        bottomPipeY = pipeHeight + 150

def checkCollision():
    global run, sleep
    if playerY <= pipeHeight and playerX >= pipeX and playerX <= pipeX + 50:
        run = False
        sleep = True
    if playerY >= bottomPipeY and playerX >= bottomPipeX and playerX <= bottomPipeX + 50:
        run = False
        sleep = True

def drawScore():
    global score, highscore
    
    # draw current score
    drawText(textFont, screen, 'Score: ' + str(score), white, screenWidth / 2 - 250, 0)
    if playerX >= pipeX and playerX <= pipeX + 1:
        score += 1
    
    # draw high score
    drawText(textFont, screen, 'High Score: ' + str(highscore), white, screenWidth / 2 - 100, 0)
    if score >= highscore:
        highscore = score

def runGame():
    global playerY
    drawPipes()
    checkCollision()
    drawScore()
    
    py.draw.rect(screen, yellow, (playerX, playerY, 10, 10))
    playerY += 15

loaded = True

while True: # main game loop
    
    screen.fill(skyblue)
    
    if run:
        runGame()
    else:
        drawText(textFont, screen, 'Score: ' + str(score), white, screenWidth / 2 - 250, 0)
        drawText(textFont, screen, 'High Score: ' + str(highscore), white, screenWidth / 2 - 100, 0)
        drawText(textFont, screen, "Start Jumping to Play", white, screenWidth / 2 - 150, screenHeight / 1.5)
        
        if displayScore:
            drawText(textFont, screen, 'You Lost!', white, screenWidth / 2 - 150, screenHeight / 3.5)
            drawText(textFont, screen, 'Your Score Was: ' + str(score), white, screenWidth / 2 - 150, screenHeight / 2.5)
        
        playerX = screenWidth / 2
        playerY = screenHeight / 2
        py.draw.rect(screen, yellow, (playerX, playerY, 10, 10))
        
        # reset game
        playerX = screenWidth / 2
        playerY = screenHeight / 2
        
        pipeX = 700
        pipeHeight = 300
        
        bottomPipeX = 700
        bottomPipeY = pipeHeight + 150
        
        if sleep:
            time.sleep(2)
            sleep = False
    
    for event in py.event.get(): # event handling loop
        if event.type == py.KEYDOWN:
            if event.key == py.K_q:
                py.display.quit()
                py.quit()
            elif event.key == py.K_UP and run:
                playerY -= 75
            elif event.key == py.K_UP and not run:
                run = True
                displayScore = True
                score = 0
                playerY -= 75
                #print('called')
    
    if loaded:
        print('Loaded')
        loaded = False
    py.draw.rect(screen, white, (-20, 0, 10, 10))
    
    py.display.flip()
    clock.tick(fps)