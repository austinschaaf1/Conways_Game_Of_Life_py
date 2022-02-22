import pygame
def aliveByClick(cellW_H,cells):
    #make cells alive by CLLICK
    pos = pygame.mouse.get_pos()
    clickRow = pos[0] // cellW_H
    clickColumn = pos[1] // cellW_H
    #print(str(clickColumn)+ " " + str(clickRow))
    if cells[clickColumn,clickRow].alive == False:
        cells[clickColumn,clickRow].changeAliveDead = (True, False)
        cells[clickColumn,clickRow].Changed = True
    elif cells[clickColumn,clickRow].alive == True:
        cells[clickColumn,clickRow].changeAliveDead = (False, False)
        cells[clickColumn,clickRow].Changed = False