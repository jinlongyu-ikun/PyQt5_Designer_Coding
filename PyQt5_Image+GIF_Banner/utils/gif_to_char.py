# author jinyunlong
# createtime 2023/3/15 22:55
# 职业 锅炉房保安

from PIL import Image, ImageDraw, ImageFont
import random
import os


def img2char(img, scale, font_file):
    # 定义字符集，可以根据需要修改
    ascii_chars = 'MNHQ$CXKAO67+>!:-. '

    # 计算缩放后的图片大小并进行缩放
    w, h = img.size
    new_height = int((h * scale))
    new_width = int(w * scale * 3)
    img = img.resize((new_width, new_height))

    # 加载字体文件
    font = ImageFont.truetype(font_file, int(6 * scale))

    # 获取图片数据
    data = img.getdata()

    # 根据灰度值映射到字符集上，并组成每行的字符串
    rows = []
    for y in range(new_height):
        row = ''.join(ascii_chars[int(data[y * new_width + x] / 256 * len(ascii_chars))] for x in range(new_width))
        rows.append(row)

    # 将字符串组装成图像并输出
    char_img = Image.new('RGB', (font.getsize(rows[0])[0], font.getsize(rows[0])[1] * len(rows)), (255, 255, 255))
    char_draw = ImageDraw.Draw(char_img)
    for i, row in enumerate(rows):
        char_draw.text((0, font.getsize(rows[0])[1] * i), row, (0, 0, 0), font=font)

    return char_img


def gif2char(gif_path, scale, font_file):

    # 打开GIF文件并分割为单帧
    gif = Image.open(gif_path)
    frames = []
    try:
        while True:
            frames.append(gif.copy())
            gif.seek(len(frames)) # skip to next frame
    except EOFError:
        pass

    # 遍历单帧图片并输出字符画
    char_imgs = []
    for i, frame in enumerate(frames):
        print(f"Processing frame {i+1}/{len(frames)}...")
        char_img = img2char(frame, scale, font_file)
        char_imgs.append(char_img)

    # 将字符画序列转换成GIF图片并保存
    gif_name, gif_ext = os.path.splitext(os.path.basename(gif_path))
    new_gif_name = f"{gif_name}_{random.randint(0, 9999)}{gif_ext}"
    char_imgs[0].save(new_gif_name, save_all=True, append_images=char_imgs[1:], duration=gif.info['duration'], loop=0)

    return new_gif_name



# 示例用法
# 获取当前脚本所在文件夹的路径
# current_dir = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(current_dir, '..', 'gif', 'ciacaizi.gif')
# gif2char(file_path, scale=0.5, font_file='arial.ttf')