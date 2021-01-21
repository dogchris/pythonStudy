# author: 杭导
# date: 2021-01-21
# update: E酱
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple captcha

import string
import random
import matplotlib.pyplot as plt
from captcha.image import ImageCaptcha

length = 4

# 随机码字典
s = string.ascii_letters + string.digits

# 这是简单写法
# code = ''.join([random.choice(s) for i in range(length)])
# 这是复杂写法
code = ''
for i in range(length):
    code += random.choice(s)

# 参数可以不要，有默认值
generator = ImageCaptcha(width=150,height=100,fonts=['C:\Windows\Fonts\simkai.ttf',\
       'C:\Windows\Fonts\simfang.ttf'])
    
plt.imshow(generator.generate_image(code))
plt.axis('off') # 不显示坐标轴
plt.show()

# image.write('审计audit','captcha.png')

