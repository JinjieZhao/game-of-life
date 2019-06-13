from src.cells import Cells
from src.draw import *
import torch
import time


class MyDrawer(Drawer):

    def __init__(self, row_num, col_num, caption_text, width, height, data):
        super().__init__(row_num, col_num, caption_text, width, height)
        self.cells = Cells(data)

    def change_status(self):
        self.rects.load(self.cells.matrix)
        self.cells.update()

    def set_data(self, data):
        for i in range(len(data)):
            for j in range(len(data[0])):
                self.cells.matrix[i][j] = data[i][j]


if __name__ == '__main__':
    data = torch.zeros(10, 10)
    data[0][2] = 1
    data[1][2] = 1
    data[2][2] = 1
    data[2][1] = 1
    data[1][0] = 1

    drawer = MyDrawer(10, 10, 'GAME OF LIFE', 1000, 700, data)
    drawer.run(change_interval=1.5)