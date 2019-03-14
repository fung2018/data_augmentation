'''
Created on 2018年11月2日

@author: FENG
'''

#-*- coding: UTF-8 -*-   
 
from PIL import Image
from PIL import ImageEnhance
import numpy as np
import os
import random

file_path = '/xxxxxxxx/'
file_save_path = '/xxxxxxxx/'
filenames = []

for filename in os.listdir(file_path):
    filename = file_path+filename
    filenames.append(filename)

brightnessValue = []
colorValue = []
contrastValue = []
sharpnessValue = []



num = 10    #每张图片增强数据
ii = 0  #总图片张数
for i in range(len(filenames)):
    image = Image.open(filenames[i])
    for j in range(num): 
        #亮度增强
        brightness = random.uniform(5, 16) /10.
#         brightness = np.random.randint(5, 16) / 10.
        brightnessValue.append(brightness)
        image_brightened  = ImageEnhance.Brightness(image).enhance(brightness)
        color = random.uniform(10, 21) / 10.
#         color = np.random.randint(10, 21) / 10.
        colorValue.append(color)
        image_colored = ImageEnhance.Color(image_brightened).enhance(color)
        contrast = random.uniform(10, 16) / 10.
#         contrast = np.random.randint(10, 16) / 10.
        contrastValue.append(contrast)
        image_contrasted = ImageEnhance.Contrast(image_colored).enhance(contrast)
        sharpness = random.uniform(10, 21) / 10.
#         sharpness = np.random.randint(10, 21) / 10.
        sharpnessValue.append(sharpness)
        image_sharped = ImageEnhance.Sharpness(image_contrasted).enhance(sharpness)
        image_sharped.save(file_save_path+np.str(ii+1)+'.png')
        ii += 1
    

file = open('brightnessValue.txt','w')
file.write(str(brightnessValue))
file.close()

file = open('colorValue.txt','w')
file.write(str(colorValue))
file.close()

file = open('contrastValue.txt','w')
file.write(str(contrastValue))
file.close()

file = open('sharpnessValue.txt','w')
file.write(str(sharpnessValue))
file.close()


print("Done!")


