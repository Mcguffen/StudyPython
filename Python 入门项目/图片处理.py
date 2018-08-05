# 先介绍一个新函数, 原型如下
# mode 是字符串, 我们使用 'RGBA' 表示生成一个每个像素由 rgba 四字节组成的图片
# size 是一个 (w, h) 表示宽高的 tuple
log = print
# Image.new(mode, size)
from math import *
# 思路如下
# 先将图片传入
# 生成空白画布
# 遍历原始图片的像素
# 按公式填充到画布上
# 保存

# 例子如下

from PIL import Image
# from turtle import *
# 生成一个宽高都是 100 的 rgba 模式的图片
# img = Image.new("RGBA", (100, 100))


# 实现以下几个函数
def xuanzhuan(image, jiaodu):
    # 接收一个图片
    # 将图片旋转指定角度
    # 打开图像文件
    img = Image.open("demo.jpg")
    # 注意由于不是每个图像都有 a 所以这里强制转换成 RGBA 格式
    img = img.convert('RGB')
    # img = image
    jd = jiaodu
    w, h = img.size
    x = 1
    y = 2
    a = jd
    a = 90
    # # 逆时针旋转a角度
    # 角度=180°×弧度÷π ，弧度=角度×π÷180°。
    hd = a * pi / 180

    img_new = Image.new("RGB", (w, h * 2))
    size = img.size
    max_x = size[0]
    max_y = size[1]
    # log('max_x', max_x, 'max_y', max_y)
    # 读取图片的所有像素点的值
    # 循环处理像素的值
    for i in range(0, max_x):
        x = i
        i += 1
        for j in range(0, max_y):
            y = j
            j = j + 1
            position = (x, y)

            r, g, b,  = img.getpixel(position)
            log('get pixel  inner', r, g, b, x)
            log('position', x, y)
    # 读取座标 (x, y) 处的像素点的像素值
    # 计算灰度值
    # 修改坐标点的值
            # 图片以左上角为坐标
            # 遍历原始图片的像素
            # 读取座标 (x, y) 处的像素点的像素值
            # 坐标转换
            # 旋转之前的坐标
            # 旋转之后的坐标
            x1 = x * cos(hd) - y * sin(hd)
            # x = int(x)
            y1 = y * cos(hd) + x * sin(hd)
            position1 = (x1, y1)
            log('position1', x1, y1)
            # c = (255, 255, 255)

            # img_new.putpixel(position, (r, g, b,))
            img_new.putpixel(position1, (r, g, b,))
    result = img_new
    img_new.save('dog_sxjx.jpg')
    return result

def crop(image, frame):
    """
    image 是一个 Image 对象
    frame 是一个 tuple 如下 (x, y, w, h)
        用于表示一个矩形的左上角座标 x y 和 宽高 w h

    不修改原图像
    返回一个 Image 对象, 它是用 frame 把 image 裁剪出来的新图像
    """
    # 打开图像文件
    img = Image.open("dog.jpg")
    # 注意由于不是每个图像都有 a 所以这里强制转换成 RGBA 格式
    img = img.convert('RGB')
    frame = (0, 119, 111, 120)
    img_old = img
    x, y, w, h = frame
    img_new = Image.new("RGB", (w, h))
    size = img_old.size
    max_x = size[0]
    max_y = size[1]
    log('max_x', max_x, 'max_y', max_y)
    # 假设原图像的宽为w，高为h，（x0,y0）为原坐标内的一点
    # 转换坐标后的点为（x1，y1）。那么不难得到
    # x1 = x0 - w/2; y1 = -y0 + h/2;
    # 读取图片的所有像素点的值
    # 循环处理像素的值
    a = 39
    for i in range(0, max_x):
        x = i
        i += 1
        for j in range(0, max_y):
            y = j
            j = j + 1
            position = (x, y)
            r, g, b, a = img_old.getpixel(position)
            # x1 = x0 - w/2; y1 = -y0 + h/2;

            log('get pixel  inner', r, g, b, a, x)
            # 图片以左上角为坐标
            # 遍历原始图片的像素
            # 读取座标 (x, y) 处的像素点的像素值
            # 坐标转换
            x0 = int (x - w / 2)
            y0 = int (-y + h / 2)
            # 旋转之前的坐标
            # 旋转之后的坐标
            # x1 = x0 * cos(a) + y0 * sin(a)
            # y1 = -x0 * sin(a) + y0 * cos(a)
            # # 转换到原始坐标系
            # a = int(x1 + w / 2)
            # b = int(-y1 + h / 2)
            # if a < 0:
            #     a = 0
            # if a > max_x - 1:
            #     a = max_x - 1
            # if b < 0:
            #     b = 0
            # if b > max_y -1:
            #     b = max_y - 1
            # position = (a, b)
            log("postion", position)
            # 按公式填充到画布上
            # 修改旋转之后的坐标的值
            img_new.putpixel(position, (r, g, b, a))
    # 返回图片

    result = img_new
    img_new.save('dog_new.png')
    return result


def flip(image):
    """
    image 是一个 Image 对象

    不修改原图像
    返回一个 Image 对象, 它是 image 上下镜像的图像
    """
    img = Image.open("demo.jpg")
    # 注意由于不是每个图像都有 a 所以这里强制转换成 RGBA 格式
    img = img.convert('RGB')
    w, h = img.size
    x, y = 0, h - 1
    img_new = Image.new("RGB", (w, h * 2))
    size = img.size
    max_x = size[0]
    max_y = size[1]
    # log('max_x', max_x, 'max_y', max_y)
    # 读取图片的所有像素点的值
    # 循环处理像素的值
    for i in range(0, max_x):

        for j in range(0, max_y):
            x = i
            i += 1
            y = j
            j = j + 1
            position = (x, y)
            r, g, b,  = img.getpixel(position)
            # log('get pixel  inner', r, g, b, x)
            # log('position', x, y)

    # 读取座标 (x, y) 处的像素点的像素值
    # 计算灰度值
    # 修改坐标点的值
            x1 = x
            y1 = 2 * h - y - 1
            position1 = (x1, y1)
            # log('position1', x1, y1)

            img_new.putpixel(position, (r, g, b,))
            img_new.putpixel(position1, (r, g, b,))
    result = img_new
    img_new.save('dog_sxjx.jpg')
    return result