# -*- coding: utf-8 -*-
# @Time    : 2020/7/1 15:28
# @Author  : 李佳玮
# @Email   : lijiawei@symbio.com
# @File    : air_ocr.py
# @Software: PyCharm


from PIL import Image
from ocr import tesseract

image = Image.open(r'D:\ocr\images\微信截图_20200701171607.png')
text = tesseract.image_to_string(image, lang='chi_sim')
print("-----------初始数据为--------------")
print(text)