import torch
import src.rle


class Cells:
    def __init__(self, mat):
        self.matrix = mat.clone().type(torch.LongTensor)
        self.shape = mat.shape
        self.kernel = torch.tensor([[1., 1., 1.],
                                    [1., 0., 1.],
                                    [1., 1., 1.]]).view(1, 1, 3, 3)

    def conv(self):
        """
        对matrix 进行卷积操作，获取每个细胞周围存活的细胞数量矩阵
        :return: 数量矩阵
        """

        # 把matrix 转成适合卷积的形式
        mat = self.matrix.view(1, 1, *self.shape).type(torch.FloatTensor)
        # 进行卷积并转回原来的形式
        return torch.conv2d(mat, self.kernel, padding=1).view(*self.shape)

    def update(self):
        live_num_mat_nearby = self.conv()
        nearby_3_live = (live_num_mat_nearby == 3).type(torch.LongTensor)
        nearby_2_live = (live_num_mat_nearby == 2).type(torch.LongTensor) * self.matrix
        self.matrix = nearby_2_live + nearby_3_live

    def load_from_file(self, filename):
        with open(filename) as f:
            rle = []
            for line in f:
                line = line.strip()
                if line.startswith('#'):
                    pass
                elif line.startswith('x'):
                    data = line.split(',')
                    weight = int(data[0].split()[-1])
                    height = int(data[1].split()[-1])
                else:
                    rle.append(line)
            rle = ''.join(rle)
            self.matrix = src.rle.rle2tensor(rle, height, weight).type(torch.LongTensor)
            self.shape = self.matrix.shape
