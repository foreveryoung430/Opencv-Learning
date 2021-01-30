# -*- coding: utf-8 -*-
# @Time    : 2021/1/30 12:17
# @Author  : YangXin
# @Email   : Null
# @Software: PyCharm
'''
像素基本处理、ROI框选以及通道分割与合并

'''
import  cv2

img = cv2.imread('lena.jpg')
'''  像素值修改 '''
# #修改像素值
# px = img[100,90]
# print(px)
# px_blue = img[100,90,1]
# #img[y行,x列,B0/G1/R2]
# print(px_blue)
# img[100,90] = [255,255,255]
# print(img[100,90])
'''  图片属性 '''
# #获取图片属性
# print(img.shape)  # (263, 247, 3)
# # 形状中包括行数、列数和通道数
# height, width, channels = img.shape
# # img是灰度图的话：height, width = img.shape
# print(img.dtype)  # uint8
# print(img.size)  # 263*247*3=194883
'''  ROI截取  '''
# 截取脸部ROI
# face = img[100:200, 115:188]
# cv2.imshow('face', face)
# cv2.waitKey(0)
# #cv2中带的split分割方法，耗时长
# b, g, r = cv2.split(img)
# img = cv2.merge((b, g, r))


b = img[:,:,2]
#img[高度，宽度，通道数]
cv2.imshow('blue', b)
cv2.waitKey(0)



