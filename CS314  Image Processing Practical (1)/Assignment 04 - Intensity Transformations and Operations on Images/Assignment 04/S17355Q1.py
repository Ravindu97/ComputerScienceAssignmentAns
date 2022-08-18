import numpy as np
import cv2
import matplotlib.pyplot as plt


img = cv2.imread(r'orion_spinelli_c1.jpg',cv2.IMREAD_COLOR)
imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

imgGrayScale = cv2.cvtColor(imgRGB,cv2.COLOR_BGR2GRAY)

blur=cv2.medianBlur(imgGrayScale,11)
ret,mask =cv2.threshold(blur,0,255,cv2.THRESH_BINARY +cv2.THRESH_OTSU)


masked =cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
output = cv2.bitwise_and(imgRGB,masked)


plt.subplot(1,3,1)
plt.title('Original image')
plt.imshow(imgRGB)

plt.subplot(1,3,2)
plt.title('mask')
plt.imshow(masked,cmap='Greys_r')

plt.subplot(1,3,3)
plt.title('Output')
plt.imshow(output)

plt.show()
