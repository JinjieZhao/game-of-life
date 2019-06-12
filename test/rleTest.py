import torch
import unittest

import src.rle


class relTest(unittest.TestCase):
    def test_rel_decode(self):
        rle_str = '7b2o$3bobo2bo$2o3b2o!'
        h, w = 3, 10
        target = torch.zeros(h, w)
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

        self.assertTrue(torch.equal(target, src.rle.rle2tensor(rle_str, h, w)))
