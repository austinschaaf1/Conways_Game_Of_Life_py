import pygame
import time

class Cell:
    def __init__(self) -> None:
        self.cellW_H = 20
        self.xCords , self.yCords = 0, 0
        self.color = (0,0,0)
        self.alive = False
        self.changed = False

        self.boxWidth = 1
    def setInitialCellAtributes(self,CellW_H_p,xCords_p,yCords_p):
        self.CellW_H = CellW_H_p
        self.xCords = xCords_p
        self.yCords = yCords_p

    def drawCell(self,win):

        pygame.draw.rect(win,self.color,(self.xCords,self.yCords,self.cellW_H,self.cellW_H),self.boxWidth)
    @property
    def changeAliveDead(self):
        return self.alive
    @changeAliveDead.setter
    def changeAliveDead(self,value):
        self.alive = value[0]
        #pygame.time.delay(10)
        if value[1] == True:
            pass
            #pygame.time.set_timer()
        if self.alive == False:
            self.color = (0,0,0)
            self.boxWidth = 1
        if self.alive == True:
            self.color = (0,0,255)
            self.boxWidth = 0


    @property
    def Changed(self):
        return self.changed
    @Changed.setter
    def Changed(self,value):
        self.changed = value
 
    def loc(self):
        return self.xCords, self.yCords