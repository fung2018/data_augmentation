# -*- coding: UTF-8 -*-
'''
Created on 2018年12月7日

@author: FENG
'''
# import the necessary packages
from imutils import paths
import cv2
import os
import numpy as np
 
def variance_of_laplacian(image):
    # compute the Laplacian of the image and then return the focus
    # measure, which is simply the variance of the Laplacian
    return cv2.Laplacian(image, cv2.CV_64F).var()

# 有序获取文件名称
def getFilePath(filePath, fileType):
    filenames = []
    sortedPath = os.listdir(filePath)
    sortedPath.sort()
    
    for filename in sortedPath:
        if os.path.splitext(filename)[1] ==  fileType:
                filename = os.path.join(filePath,filename)
                filenames.append(filename)
    return filenames

def rotate_bound(image, angle):
    # grab the dimensions of the image and then determine the
    # center
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)
 
    # grab the rotation matrix (applying the negative of the
    # angle to rotate clockwise), then grab the sine and cosine
    # (i.e., the rotation components of the matrix)
    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
 
    # compute the new bounding dimensions of the image
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))
 
    # adjust the rotation matrix to take into account translation
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY
 
    # perform the actual rotation and return the image
    return cv2.warpAffine(image, M, (nW, nH))

def checkPath(imagePath):
    save_dir = imagePath
    if os.path.exists(save_dir) is False:
        os.makedirs(save_dir)
    return save_dir

def del_file(path):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.remove(c_path)

imagePath = '/xxxxxxx/'
clearSavePath = '/xxxxxxx/'
blurrySavePath = '/xxxxxxx/'

clearSavePath = checkPath(clearSavePath)
blurrySavePath = checkPath(blurrySavePath)
del_file(clearSavePath)
del_file(blurrySavePath)

threshold = 800.0
fileType = '.jpg'
filenames = getFilePath(imagePath, fileType)

ii = 1
for filename in filenames:
    image = cv2.imread(filename)
    width, height, channels= image.shape
#     print(width)
    if (width < height):
        image = rotate_bound(image, 90)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fm = variance_of_laplacian(gray)
#     text = "Not Blurry"
#   
#       
#     if fm < threshold :
#         text = "Blurry"
#       
#     cv2.putText(image, "{}: {:.2f}".format(text, fm), (int(width*0.05), int(height*0.05)),
#                 cv2.FONT_HERSHEY_SIMPLEX, width/800, (0, 0, 255), 2)
#     cv2.imwrite(savePath+'blur'+str(ii)+'.jpg', image)
    if fm > threshold:
        cv2.imwrite(clearSavePath+'clear'+str(ii)+'.jpg', image)
    else:
        cv2.imwrite(blurrySavePath+'blur'+str(ii)+'.jpg', image)
    ii += 1

print("Done!")