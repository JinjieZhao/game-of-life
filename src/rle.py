import torch


def decode(rle_str):
    """
    把rle 字符串转成嵌套的列表
    嵌套结构：行->列->(num, c)
    :param rle_str:
    :return:嵌套的列表
    """

    lines = []

    count = 0
    line = []
    for c in rle_str:
        if c == '!':
            lines.append(line)
            break
        elif c in ['b', 'o']:
            if count == 0:
                line.append((1, c))
            else:
                line.append((count, c))
                count = 0
        if c.isdigit():
            count *= 10
            count += int(c)
        if c == '$':
            lines.append(line)
            line = []
    return lines


def rle2tensor(rle_str, height, weight):
    tensor = torch.zeros(height, weight)

    lines = decode(rle_str)

    for row, line in enumerate(lines):
        col = 0
        for num, c in line:
            if c == 'b':
                col += num
            elif c == 'o':
                for _ in range(num):
                    tensor[row][col] = 1
                    col += 1
    return tensor
