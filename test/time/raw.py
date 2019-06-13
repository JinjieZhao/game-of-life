from src.cells import Cells
import time
import torch

cells = Cells(torch.tensor(1))
cells.load_from_file(r'..\..\patterns\gunstar.rle')
lives = int(torch.sum(cells.matrix))
print(lives)
start = time.time()
for _ in range(1000):
    total = 0
    for i in range(lives):
        total += cells.matrix[i % 149][(i + 3) * 2 % 149]
print(time.time() - start)
