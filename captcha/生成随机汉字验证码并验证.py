# author: E酱
# date: 2021-01-21
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple captcha

import re
import random
import matplotlib.pyplot as plt
from captcha.image import ImageCaptcha

length = 4

def getCaptha():
    f = open('s.txt', 'r', encoding='UTF-8')
    s = f.read()
    l = re.findall('[\u4e00-\u9fa5]', s)
    l = list(set(l))
    f.close()
    
    code = ''
    for i in range(length):
        code += random.choice(l)
    
    # 参数可以不要，有默认值
    generator = ImageCaptcha(width=150,height=100,fonts=['C:\Windows\Fonts\simkai.ttf',\
           'C:\Windows\Fonts\simfang.ttf'])
        
    plt.imshow(generator.generate_image(code))
    plt.axis('off') # 不显示坐标轴
    plt.show()
    
    return code

code = getCaptha()
s = input('请输入验证码：')
while code != s:
    print('验证码错误，请重试！')
    code = getCaptha()
    s = input('请输入验证码：')
print('验证码正确！')
