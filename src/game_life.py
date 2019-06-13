from src.cells import Cells
from src.draw import *
import torch
import time


class MyDrawer(Drawer):

    def __init__(self, caption_text, width, height, data):
        row_num, col_num = data.shape
        super().__init__(row_num, col_num, caption_text, width, height)
        self.cells = Cells(data)

    def change_status(self):
        self.rects.load(self.cells.matrix)
        self.cells.update()

    def set_data(self, data):
        for i in range(len(data)):
            for j in range(len(data[0])):
                self.cells.matrix[i][j] = data[i][j]

    def open_file(self):
        from tkinter import filedialog
        path = filedialog.askopenfilename()
        self.cells.load_from_file(path)
        return self.cells.shape

if __name__ == '__main__':
    data = torch.zeros(50, 50)

    drawer = MyDrawer('GAME OF LIFE', 1000, 650, data)
    drawer.run(change_interval=0.1)