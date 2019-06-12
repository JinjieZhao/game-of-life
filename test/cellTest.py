import torch
import unittest

from src.cells import Cells


class CellsTest(unittest.TestCase):

    def test_should_3_live(self):
        tensor = torch.tensor([[0, 1, 0],
                               [1, 0, 1],
                               [0, 0, 0]])
        target = torch.tensor([[0, 0, 0],
                               [0, 1, 0],
                               [0, 0, 0]])
        cells = Cells(tensor)
        cells.update()

        self.assertEqual(target, cells.matrix)
