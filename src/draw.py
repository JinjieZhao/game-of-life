"""
负责绘画的类，负责界面
包括以下类
Drawer：整个界面
Rect：单元矩形点
Rects：二维矩阵
"""
import pygame


class Rect:
    """
    矩形单元，代表每个点
    """

    def __init__(self, x, y, side, color, border=0):
        """
        初始化，边长，坐标x y 颜色
        :param x: 所在横坐标
        :param y: 所在纵坐标
        :param side: 单元格边长
        :param color: 单元格颜色
        :param border: 单元格边框
        """
        self.x = x
        self.y = y
        self.side = side
        self.color = color
        self.border = border
        # self.rect = pygame.Rect(x, y, side, side)

    def set_color(self, color):
        """
        修改单元格颜色
        :param color:  要修改的颜色
        :return: None
        """
        self.color = color


class Rects:
    """
    矩阵表格 包含x*y个矩形
    """

    def __init__(self, row_num, col_num, side, color, start_x, start_y):
        """
        初始化矩阵
        :param row_num: 矩阵的行数
        :param col_num: 矩阵的列数
        :param side: 矩阵单元格边长
        :param color: 矩阵背景颜色
        :param start_x: 矩阵左上角起始横坐标
        :param start_y: 矩阵左上角起始纵坐标
        """
        self.row_num = row_num
        self.col_num = col_num
        self.side = side
        self.color = color
        self.start_x = start_x
        self.start_y = start_y
        self.rects = self.init_rects()

    def init_rects(self):
        """
        初始化矩阵
        :return: [] 返回二维矩阵
        """
        rects = []  # 二维矩阵边框
        rects_border = []  # 二维矩阵内部颜色
        for i in range(self.row_num):
            rects.append([])
            rects_border.append([])
            for j in range(self.col_num):
                rects[i].append(Rect(self.get_n(self.start_x, j),
                                     self.get_n(self.start_y, i),
                                     self.side,
                                     self.color,
                                     2
                                     ))
        return rects

    def get_n(self, start_position, n):
        """
        计算第n列(行)的矩形左上角的坐标, 从第0个开始计算
        :param n: 第n列（行）个矩形
        :return: int 距离左边或顶端的距离
        """
        return start_position + n * self.side

    def draw(self, screen):
        """
        绘画矩阵
        :param screen: 界面
        :return:
        """
        for i in range(self.row_num):
            for j in range(self.col_num):
                rect = self.rects[i][j]
                pygame.draw.rect(screen, [255, 255, 0], [rect.x, rect.y, rect.side, rect.side], rect.border)
                pygame.draw.rect(screen, rect.color,
                                 [rect.x + rect.border, rect.y + rect.border, rect.side - rect.border * 2, rect.side],
                                 0)

    def load_list(self, data_list):
        """
        装载二维矩阵 如果矩阵值为1 显示蓝色 值为0显示红色
        :param data_list: 装载二维矩阵
        :return: None
        """
        for i in range(len(data_list)):
            for j in range(len(data_list[0])):
                if data_list[i][j] == 1:
                    self.rects[i][j].set_color([125, 125, 125])
                else:
                    self.rects[i][j].set_color([0, 0, 0])


class Drawer:
    """
    界面 绘画
    """

    def __init__(self, rects, caption_text, width, height):
        """
        初始化
        :param rect: 设置矩阵
        """
        pygame.init()
        pygame.display.set_caption(caption_text)
        self.screen = pygame.display.set_mode((width, height), 0, 32)
        self.rects = rects
        self.screen.fill([255, 255, 255])

    def show(self):
        self.rects.draw(self.screen)
        pygame.display.update()

    def run(self):
        self.show()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
