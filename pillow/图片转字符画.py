# author: 杭导
# date: 2021-01-14

from PIL import Image
# 打开一张图片，后续将生成文件名相同的txt文件
picPath = '1.jpg'
img = Image.open(picPath)

# 将图片转换为灰度模式
out = img.convert('L')
# out.show()

# 缩放大小
zoom = 0.1
# 缩放纵横比，数值越大图片会变得越“瘦”
vscale = 0.5

# 重新计算图片宽度和高度
width,height = out.size
out = out.resize((int(width * zoom),int(height * zoom * vscale)))
width,height = out.size

# 获取每个像素点的黑度。数值越小，颜色越黑
# print(out.getpixel((100,100)))
# print(out.getpixel((208,88)))

# 灰度转换成字符串
# asciis = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
asciis = '@%#*+=-. '
texts = ''
for row in range(height):
    for col in range(width):
        gray = out.getpixel((col,row))
        texts += asciis[int(gray/255 * (len(asciis) - 1))]
    texts += '\n'

sList = picPath.split('.')
txtPath = sList[0] + '.txt'
with open(txtPath, 'w') as file:
    file.write(texts)

































































