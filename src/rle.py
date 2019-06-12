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
            if count > 1:
                for _ in range(count - 1):
                    lines.append(line)
                count = 0
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


def encode_one_line(line):
    res = []

    count = 1
    pre = line[0]
    for i in range(1, len(line)):
        cur = line[i]
        if pre == cur:
            count += 1
        else:
            res.append((str(count) if count > 1 else '') + pre)
            count = 1
            pre = cur
    if line[-1] == 'o':
        res.append((str(count) if count > 1 else '') + line[-1])

    return ''.join(res)


def encode(lines):
    return '$'.join(map(encode_one_line, lines)) + '!'


def tensor2rle(tensor):
    tensor = tensor.type(torch.LongTensor)

    bos = {
        0: 'b',
        1: 'o'
    }

    # 把tensor 转成bbboo 的列表
    lines = [[bos[int(i)] for i in row] for row in tensor]

    return encode(lines)
