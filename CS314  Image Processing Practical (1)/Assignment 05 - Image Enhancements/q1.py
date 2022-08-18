import cv2
import numpy as np
import matplotlib.pyplot as plt


##read image
img=cv2.imread('fire.jpg',cv2.IMREAD_COLOR)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#split to hsv
h,s,v=cv2.split(cv2.cvtColor(img,cv2.COLOR_RGB2HSV))
eq_v=cv2.equalizeHist(v)

##merge
eq_img=cv2.merge([h,s,eq_v])
eq_img=cv2.cvtColor(eq_img,cv2.COLOR_HSV2RGB)

##threshold
# through trail and error Threshold value was selected as 200
ret,thresh=cv2.threshold(eq_img,200,255,cv2.THRESH_BINARY_INV)

##mask
mask=cv2.inRange(thresh,(0,0,255),(0,255,255))

##applying a mask to the image
result=cv2.bitwise_and(eq_img,eq_img,mask=mask)

plt.subplot(1,3,1)
plt.title('Original')
plt.imshow(img)
plt.xticks([]),plt.yticks([])

plt.subplot(1,3,2)
plt.title('Mask')
plt.imshow(mask,cmap='Greys_r')
plt.xticks([]),plt.yticks([])

plt.subplot(1,3,3)
plt.title('Result')
plt.imshow(result)
plt.xticks([]),plt.yticks([])

plt.show()
