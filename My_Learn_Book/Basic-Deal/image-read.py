'''
Image file reading and writing

'''

import cv2
import numpy
img_color = cv2.imread('lena.jpg',-1)
img_gray = cv2.imread('lena.jpg',0)
img_test = cv2.imread('lena.jpg',-1)


##(-1：原色, 0:灰度, 1:彩色, 2:深度 4:任意颜色格式
# 16/17:1/2 灰度/彩色缩减       32/33： 1/4   64/65 1/8
# 128：不旋转)
'''
C++:
读取
Mat cv::imread	(	const String & 	filename,
int 	flags = IMREAD_COLOR )		
保存
bool cv::imwrite	(	const String & 	filename,
InputArray 	img,
const std::vector< int > & 	params = std::vector< int >() 
)	
Python:
retval	=	cv.imread(	filename[, flags]	).
retval	=	cv.imwrite(	filename, img[, params]	)
'''
cv2.namedWindow('lean.jpg', cv2.WINDOW_NORMAL) ##cv2.WINDOW_NORMAL//cv2.WINDOW_AUTOSIZE
cv2.imshow('lean.jpg',img_test)
cv2.imwrite('lena_test.jpg',img_test)
cv2.waitKey(0)