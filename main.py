from array import *
from cell import Cell
import numpy as np
import pygame
from functions.createCells import *
from functions.FillRandomCells import *
from random import *
import datetime
from functions.WriteTimeToF import *
from functions.AliveByClick import *
class life:
    def __init__(self) -> None:
        self.ScreenWidth = 1000 #self.ScreenWidth = 500
        self.ScreenHeight = 1000 # self.ScreenHeight = 500
        self.clock = 10
        self.cellW_H = 20
        self.cells = createCells(self.ScreenWidth ,self.ScreenHeight, self.cellW_H)
        self.rows, self.columns = np.shape(self.cells)
        self.cellsCount = self.rows * self.columns
    def gameLoop(self):
        pygame.init()
        win = pygame.display.set_mode((self.ScreenWidth, self.ScreenHeight))
        pygame.display.set_caption("autamita life")
        win.fill((211,211,211))
        timeCount = 0
        totalTime = datetime.datetime.now()
        clock = pygame.time.Clock()
        currentTime = 0
        drawTime = 0
        
        totalTime = totalTime - datetime.datetime.now()
        run = True
        while run:
            win.fill((211,211,211))
            start_time = datetime.datetime.now()
            pygame.time.delay(self.clock)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    aliveByClick(self.cellW_H,self.cells)

            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE]:
                fillRandomCells(keys,self.columns,self.rows,self.cells,4)

            #redraw cells
            for i in range(self.rows):
                for j in range(self.columns):
                    ranCol = np.random.randint(0,3)
                    if (i != self.columns -1  and j != self.rows - 1) and (i != 0  and j != self.rows - 1):
                        if ranCol == 1:
                            self.cells[i,j].changeAliveDead = (True, True)
                            self.cells[i,j].Changed = True
                        else:
                            self.cells[i,j].changeAliveDead = (False, True)
                            self.cells[i,j].Changed = False

            #redraw cells
            for i in range(self.rows):
                for j in range(self.columns):
                    

                    #Check if there is 3 cells next to it
                    #temp start game = column row 24 24
                    if ((self.cells[self.columns - 1,self.rows - 1].alive == True) and i != self.columns -1  and j != self.rows - 1):
                    #if ((self.cells[4,4].alive == True) and i != 4 and j != 4):
                        nebAlive = 0
                        drawTime = pygame.time.get_ticks()
                        if (j != 0):
                            if(self.cells[i,j-1].alive == True): #left
                                nebAlive += 1
                                #print("{neb} = left {row} col = {col}".format(row=i, col=j,neb=nebAlive))
                                print("left")
                        if j != self.columns - 1:
                            if(self.cells[i,j+1].alive == True): #right
                                nebAlive += 1
                                #print("{neb} = right {row} col = {col}".format(row=i, col=j,neb=nebAlive))
                                print("right")
                        if i != 0:
                            if self.cells[i-1,j].alive == True: #up
                                nebAlive += 1
                                print("up")
                        if i != self.rows - 1:
                            if self.cells[i+1,j].alive == True: #down
                                nebAlive += 1
                                #print("{neb} = down {row} col = {col}".format(row=i, col=j,neb=nebAlive))
                                print("down")
                        if i != 0 and j != 0:
                            if self.cells[i-1,j-1].alive == True: #top left
                                nebAlive += 1
                                print("top Left")
                        if i != 0 and j != self.columns - 1:
                            if self.cells[i -1, j + 1].alive == True: #top Right
                                nebAlive += 1
                                print("top right")
                        if i != self.rows - 1 and j != 0: #down left I believe
                            if self.cells[i + 1, j - 1].alive == True:
                                nebAlive += 1
                                print("down left")
                        if i != self.rows -1 and j != self.columns - 1: # down right
                            if self.cells[i + 1, j + 1].alive == True:
                                nebAlive += 1
                                print("down right")
                        if nebAlive >= 4:
                            #self.cells[i,j].changeAliveDead = (False, True)
                            self.cells[i,j].Changed = False
                        
                        if(nebAlive == 3 and self.cells[i,j].alive == False):
                            #self.cells[i,j].changeAliveDead = (True, True)
                            self.cells[i,j].Changed = True
                        if(nebAlive == 0 or nebAlive == 1):
                            #self.cells[i,j].changeAliveDead = (False, True)
                            self.cells[i,j].Changed = False
                            #self.cells[0,0].changeAliveDead = True
                            #self.cells[0,0].drawCell(win)
                        
                    currentTime = pygame.time.get_ticks()
                    #if currentTime - drawTime > 1000:

            if self.cells[0,self.rows - 1].alive == True:
                for i in range(self.rows):
                    for j in range(self.columns):
                        #print("in")
                        self.cells[i,j].Changed = False
                        self.cells[i,j].changeAliveDead = (False, True)
            
            for i in range(self.rows):
                for j in range(self.columns):
                    if self.cells[i,j].changed == True:
                        self.cells[i,j].changeAliveDead = (True, True)
                    if self.cells[i,j].changed == False:
                        self.cells[i,j].changeAliveDead = (False, True)
                    self.cells[i,j].drawCell(win)

                #pygame.time.delay(self.clock)
            pygame.display.flip()
            clock.tick(60)
            end_time = datetime.datetime.now()
            timeCount +=1
            totalTime = totalTime + end_time - start_time
        writeTimeToF(totalTime,timeCount)
        pygame.quit()

def main():
   gameM = life()
   gameM.gameLoop()


if __name__ == '__main__':
   main()