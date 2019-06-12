from src.cells import Cells
from src.draw import *
import torch
import time

if __name__ == '__main__':
    data = torch.zeros(10, 10)
    data[0][2] = 1
    data[1][2] = 1
    data[2][2] = 1
    data[2][1] = 1
    data[1][0] = 1

    cells = Cells(data)
    rects = Rects(10, 10, 20, [0, 0, 0], 50, 50)
    drawer = Drawer(rects, 'test', 500, 500)
    for _ in range(50):
        rects.load_list(cells.matrix)
        drawer.show()
        cells.update()
        time.sleep(0.1)
