# author: 杭导
# date: 2021-01-21
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple captcha

import captcha

from captcha.image import ImageCaptcha

# 参数可以不要，有默认值
image = ImageCaptcha(width=350,height=200,fonts=['C:\Windows\Fonts\simkai.ttf',\
       'C:\Windows\Fonts\simfang.ttf'])

image.write('审计audit','captcha.png')

