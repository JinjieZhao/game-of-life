from src.cells import Cells
import torch

data = torch.zeros(10, 10)
data[0][2] = 1
data[1][2] = 1
data[2][2] = 1
data[2][1] = 1
data[1][0] = 1

cells = Cells(data)

for _ in range(10):
    print(cells.matrix)
    cells.update()
