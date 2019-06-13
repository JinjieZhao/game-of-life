"""
模块中自定义控件
本模块主要包括按钮
Button
"""
import pygame


# 按钮类
class Button(object):
    # 构造函数
    def __init__(self, buttonUpImage, buttonDownImage, pos):
        # 按钮未按下的图片样式
        self.buttonUp = pygame.image.load(buttonUpImage).convert_alpha()
        # 按钮按下的图片样式
        self.buttonDown = pygame.image.load(buttonDownImage).convert_alpha()
        # 按钮在窗口中的位置
        self.pos = pos

    # 检查鼠标是否在按钮图片范围内
    def inButtonRange(self):
        w, h = self.buttonUp.get_size()
        return inImgRange([self.pos[0] - w/2, self.pos[1] -h/2], w, h)

    # 在窗口中显示按钮
    def show(self, screen):
        w, h = self.buttonUp.get_size()
        x, y = self.pos
        # 根据鼠标位置变换样式
        if self.inButtonRange():
            screen.blit(self.buttonDown, (x - w / 2, y - h / 2))
        else:
            screen.blit(self.buttonUp, (x - w / 2, y - h / 2))


class Font:

    def __init__(self, cont, x, y, color, back_color):
        fontObj = pygame.font.Font('PAPYRUS.ttf', 48)  # 通过字体文件获得字体对象
        self.textSurfaceObj = fontObj.render('Hello world!', True, color, back_color)  # 配置要显示的文字
        self.textRectObj = self.textSurfaceObj.get_rect()  # 获得要显示的对象的rect
        self.textRectObj.center = (x, y)  # 设置显示对象的坐标

    def draw(self, screen):
        screen.blit(self.textSurfaceObj, self.textRectObj)  # 绘制字体
        

def inImgRange(pos, w, h):
    # 获取鼠标的位置
    mouseX, mouseY = pygame.mouse.get_pos()
    x, y = pos
    inX = x < mouseX < x + w
    inY = y < mouseY < y + h
    return inX and inY