from src.cells import Cells
from src.draw import *
import torch
import time


class MyDrawer(Drawer):

    def __init__(self, rects, caption_text, width, height, data):
        super().__init__(rects, caption_text, width, height)
        self.cells = Cells(data)

    def change_status(self):
        self.rects.load(self.cells.matrix)
        self.cells.update()

if __name__ == '__main__':
    data = torch.zeros(10, 10)
    data[0][2] = 1
    data[1][2] = 1
    data[2][2] = 1
    data[2][1] = 1
    data[1][0] = 1

    rects = Rects(10, 10, 20, [0, 0, 0], 50, 50)
    drawer = MyDrawer(rects, 'test', 500, 500, data)
    drawer.run(change_interval=1.5)
