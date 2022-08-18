import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r'orion_spinelli_c1.jpg',cv2.IMREAD_GRAYSCALE)

# global thresholding value

T1 = 100

ret,thresh1 = cv2.threshold(img,T1,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,T1,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,T1,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,T1,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,T1,255,cv2.THRESH_TOZERO_INV)


# adaptive Thresholding

img_median_blurred = cv2.medianBlur(img,5)

# Adaptive Threshold Method mean
adpThresh1 = cv2.adaptiveThreshold(img_median_blurred,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,21,2)
adpThresh2 = cv2.adaptiveThreshold(img_median_blurred,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,21,2)

# Adaptive Threshold Method Gaussian
adpThresh3 = cv2.adaptiveThreshold(img_median_blurred,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,2)
adpThresh4 = cv2.adaptiveThreshold(img_median_blurred,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,21,2)


# Otzu's Thresholding
ret2,thresh_otzu = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Otzu's Thresholding after Gaussian filtering
img_gaussian_blurred = cv2.GaussianBlur(img,(5,5),0)
ret3,thresh_otzu_blurred =cv2.threshold(img_gaussian_blurred,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

labels = ["Original_image","THRESH_BINARY","THRESH_BINARY_INV","THRESH_TRUNC","THRESH_TOZERO","THRESH_TOZERO_INV","ADAPTIVE_THRESH_MEAN_Binary","ADAPTIVE_THRESH_MEAN_Binary_INV","ADAPTIVE_THRESH_GAUSSIAN_Binary","ADAPTIVE_THRESH_GAUSSIAN_Binary_INV","thresh_otzu","thresh_otzu_blurred"]
images = [img,thresh1,thresh2,thresh3,thresh4,thresh5,adpThresh1,adpThresh2,adpThresh3,adpThresh4,thresh_otzu,thresh_otzu_blurred]



for i in range(12):
    plt.subplot(4,3,i+1)
    plt.title(labels[i],fontsize=7)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(images[i],cmap='Greys_r')


plt.show()


thresh_otzu_blurred_Guassian_result_blur = cv2.GaussianBlur(img_gaussian_blurred,(5,5),0)

cv2.imshow("test",thresh_otzu_blurred_Guassian_result_blur)
