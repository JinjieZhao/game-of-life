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
        live_mat_nearby = self.conv()
        nearby_3_live = (live_mat_nearby == 3).type(torch.LongTensor)
        nearby_2_live = (live_mat_nearby == 2).type(torch.LongTensor) * self.matrix
        self.matrix = nearby_2_live + nearby_3_live
