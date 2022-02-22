import numpy as np
from cell import Cell
def createCells(widthM,heightM,cellW_H):
    cells = np.empty(0)
    columns =  widthM // cellW_H
    rows =  heightM // cellW_H
    for i in range(columns * rows):
        cells = np.append(cells, Cell())
    
    cells = cells.reshape(columns, rows)
    xCords = 0
    yCords = 0
    for i in range(columns):
        for j in range(rows):
            cells[i, j].setInitialCellAtributes(cellW_H,xCords,yCords)
            xCords += cellW_H
        yCords += cellW_H
        xCords = 0
    return cells