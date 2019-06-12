import torch
import unittest

from src.cells import Cells


class CellsTest(unittest.TestCase):

    def test_should_3_live(self):
        tensor = torch.tensor([[0, 0, 1],
                               [0, 0, 1],
                               [1, 0, 0]])
        target = torch.tensor([[0, 0, 0],
                               [0, 1, 0],
                               [0, 0, 0]])
        cells = Cells(tensor)
        cells.update()
        self.assertTrue(torch.equal(target, cells.matrix.type(torch.LongTensor)))

    def test_should_2_keep(self):
        tensor = torch.tensor([[0, 0, 0],
                               [1, 0, 1],
                               [0, 0, 0]])
        target = torch.tensor([[0, 0, 0],
                               [0, 0, 0],
                               [0, 0, 0]])
        cells = Cells(tensor)
        cells.update()
        self.assertTrue(torch.equal(target, cells.matrix))

        tensor = torch.tensor([[0, 1, 0],
                               [1, 0, 1],
                               [0, 0, 0]])
        target = torch.tensor([[0, 1, 0],
                               [0, 1, 0],
                               [0, 0, 0]])
        cells = Cells(tensor)
        cells.update()
        self.assertTrue(torch.equal(target, cells.matrix))

    def test_should_less_die(self):
        """
        如果周围细胞数量小于2 细胞会死亡
        """
        tensor = torch.tensor([[0, 1, 0],
                               [1, 0, 0],
                               [0, 0, 0]])
        target = torch.tensor([[0, 0, 0],
                               [0, 0, 0],
                               [0, 0, 0]])
        cells = Cells(tensor)
        cells.update()
        self.assertTrue(torch.equal(target, cells.matrix))

    def test_should_more_die(self):
        """
        如果周围细胞数量小于2 细胞会死亡
        """
        tensor = torch.tensor([[1, 1, 1],
                               [1, 1, 1],
                               [1, 1, 1]])
        target = torch.tensor([[1, 0, 1],
                               [0, 0, 0],
                               [1, 0, 1]])
        cells = Cells(tensor)
        cells.update()
        self.assertTrue(torch.equal(target, cells.matrix))

    def test_load_from_file(self):
        # TODO: 需要重构 构造函数
        cells = Cells(torch.tensor(0))
        filename = 'patterns/gunstar.rle'
        cells.load_from_file(filename)
        target = torch.zeros(3, 10)
        ones = [
            [0, 7],
            [0, 8],
            [1, 3],
            [1, 5],
            [1, 8],
            [2, 0],
            [2, 1],
            [2, 5],
            [2, 6]
        ]

        for i, j in ones:
            target[i][j] = 1

        self.assertTrue(torch.equal(target, cells.matrix))
