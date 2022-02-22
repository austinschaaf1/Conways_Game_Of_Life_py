import numbers
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from array import *
from cell import Cell
import numpy as np


        

class gameOfLife(QWidget):
   def __init__(self):
      super(gameOfLife, self).__init__()
      self.initUI()

   def initUI(self):
      self.text = "hello world"
      self.setGeometry(100,100, 500,500)
      self.setWindowTitle('Draw Demo')
      self.color = Qt.black
      self.cells = self.createCells()
      self.show()
   
   def keyPressEvent(self, event):
      if event.key() == Qt.Key_Space:
         self.color = Qt.black
         self.update()
      if event.key() == Qt.Key_Alt:
         #self.cells[2,1].qp = qp
         self.cells[2,1].color = Qt.blue
         self.color = Qt.blue
         #self.cells[2,1].drawCell()
         #self.paintEvent()
         print("hi2")
         #self.update()

   def paintEvent(self, event):
      widthM = 500
      heightM = 500
      qp = QPainter()
      qp.begin(self)
      #cells = np.empty(0)
      columns =  widthM // 20
      rows =  heightM // 20
      print("hi1")
      # for i in range(columns * rows):
      #     cells = np.append(cells, Cell())
      # cells = cells.reshape(columns, rows)
      xCords = 0
      yCords = 0
      for i in range(columns):
         for j in range(rows):
            self.cells[i, j].qp = qp
            self.cells[0,2].color = self.color
            #self.cells[i, j].xCords = xCords
            #cells[i, j].yCords = yCords
            self.cells[i, j].drawCell()
            xCords += 20
         yCords += 20
         xCords = 0
      qp.end()
   def createCells(self):
      widthM = 500
      heightM = 500
      qp = QPainter()
      qp.begin(self)
      cells = np.empty(0)
      columns =  widthM // 20
      rows =  heightM // 20
      print("hi")
      for i in range(columns * rows):
          cells = np.append(cells, Cell())
      cells = cells.reshape(columns, rows)
      xCords = 0
      yCords = 0
      for i in range(columns):
         for j in range(rows):
            cells[i, j].qp = qp
            cells[i, j].xCords = xCords
            cells[i, j].yCords = yCords
            #cells[i, j].drawCell()
            xCords += 20
         yCords += 20
         xCords = 0
      return cells


def main():
   app = QApplication(sys.argv)
   ex = gameOfLife()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()



# rectangle = Rectange()
# print(rectangle)
# rectangle.qp = qp
# rectangle.widthR = widthM
# rectangle.heightR = heightM
# rectangle.drawRectange()
#   qp.setPen(QColor(Qt.red))
#   qp.setFont(QFont('Arial', 20))
#   qp.drawText(10,50, "hello Python")
#   qp.setPen(QColor(Qt.blue))
#   qp.drawLine(10,100,100,100)
#   qp.drawRect(10,150,150,100)
#   qp.setPen(QColor(Qt.yellow))
#   qp.drawEllipse(100,50,100,50)
#   qp.drawPixmap(220,10,QPixmap("pythonlogo.png"))
#   qp.fillRect(20,175,130,70,QBrush(Qt.SolidPattern))