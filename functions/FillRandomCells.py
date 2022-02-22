import pygame
import numpy as np
def fillRandomCells(keys,columns,rows,cells,boxWidthN):
    if keys[pygame.K_SPACE]:
        ranCol = np.random.randint(0,columns)
        randRow = np.random.randint(0,rows)
        randR = np.random.randint(0,255)
        randG = np.random.randint(0,255)
        randB = np.random.randint(0,255)
        cells[ranCol,randRow].color = (randR,randG,randB)
        cells[ranCol,randRow].boxWidth = boxWidthN