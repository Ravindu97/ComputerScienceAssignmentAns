import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread(r'numbers.jpg', cv2.IMREAD_GRAYSCALE)


#Global thresholding
T1 = 100

ret,thresh1 = cv2.threshold(img, T1, 255, cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img, T1, 255, cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img, T1, 255, cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img, T1, 255, cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img, T1, 255, cv2.THRESH_TOZERO_INV)

#Adaptive thresholding
thresh6 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 2)
thresh7 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 2)
thresh8 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 2)
thresh9 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 2)

#Otsu's thresholding
ret2,thresh10 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#Otsu's thresholding after Gaussian filtering
blur = cv2.GaussianBlur(img, (5,5), 0)
ret3,thresh11 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

titles = ['Original','Global-binary','Global-binary-inverse','Global-trunc','Global-toZero','Global-toZero-inverse','adaptive-mean-binary','adaptive-mean-binary-inverse',
          'adaptive-Gaussian-binary','adaptive-Gaussian-binary-inverse',"Otsu's thresholding",'Otsu-after-GaussianFilter']

images = [img,thresh1,thresh2,thresh3,thresh4,thresh5,thresh6,thresh7,thresh8,thresh9,thresh10,thresh11]

for i in range(12):
    plt.subplot(3,4,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i],fontsize=7)
    plt.xticks([]),plt.yticks([])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
