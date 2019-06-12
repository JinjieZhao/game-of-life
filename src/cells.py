import torch


class Cells:
    def __init__(self, mat):
        self.matrix = mat.clone()
        self.shape = mat.shape
        self.kernel = torch.tensor([[1., 1., 1.],
                                    [1., 0., 1.],
                                    [1., 1., 1.]]).view(1, 1, 3, 3)

    def conv(self):
        mat = self.matrix.view(1, 1, *self.shape).type(torch.FloatTensor)
        return torch.conv2d(mat, self.kernel, padding=1).view(*self.shape)

    def update(self):
        live_nums_nearby = self.conv()
        self.matrix = (live_nums_nearby == 3)
