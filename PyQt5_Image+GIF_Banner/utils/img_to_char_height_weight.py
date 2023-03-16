# author jinyunlong
# createtime 2023/3/15 23:06
# 职业 锅炉房保安

from PIL import Image

def img2charTxt(filename, new_width, new_height, txtname):
    # 定义字符集，可以根据需要修改
    ascii_chars = 'MNHQ$CXKAO67+>!:-. '

    # 打开图片并转换为灰度图像
    img = Image.open(filename).convert('L')

    # 进行缩放
    img = img.resize((new_width, new_height))

    # 获取图片数据
    data = img.getdata()

    # 根据灰度值映射到字符集上，并组成每行的字符串
    rows = []
    for y in range(new_height):
        row = ''.join(ascii_chars[int(data[y * new_width + x] / 256 * len(ascii_chars))] for x in range(new_width))
        rows.append(row)

    # 将字符串写入文件
    with open(txtname, 'w') as f:
        f.write('\n'.join(rows))

# 示例用法
img2charTxt('cai.jpg', new_width=100, new_height=50, txtname='example.txt')