from src.cells import Cells
import time
import torch

cells = Cells(torch.tensor(1))
cells.load_from_file(r'..\..\patterns\gunstar.rle')
start = time.time()
for _ in range(1000):
    cells.update()
print(time.time() - start)
