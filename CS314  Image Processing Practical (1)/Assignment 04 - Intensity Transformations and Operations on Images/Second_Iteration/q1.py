import cv2
import matplotlib.pyplot as plt
import numpy as np


image = cv2.imread(r'orion_spinelli_c1.jpg',cv2.IMREAD_GRAYSCALE)

# blur() ksize = (10,10)
ksize = (10,10)
blurred_image = cv2.blur(image,ksize)

# medianblur
image_median_Blur = cv2.medianBlur(image,5)

#guassian blur
image_guassian_blur = cv2.GaussianBlur(image,(5,5),0)


# Otzu's Thresholding
ret2,thresh_otzu = cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Otzu's Thresholding after Gaussian filtering
img_gaussian_blurred = cv2.GaussianBlur(image,(5,5),0)
ret3,thresh_otzu_blurred =cv2.threshold(image_guassian_blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)





plt.subplot(131)
plt.title("Original")
plt.xticks([]),plt.yticks([])
plt.imshow(image,cmap="Greys_r")

plt.subplot(132)
plt.title("Median Blur")
plt.xticks([]),plt.yticks([])
plt.imshow(thresh_otzu,cmap="Greys_r")

plt.subplot(133)
plt.title("Guassian Blur otuzu")
plt.xticks([]),plt.yticks([])
plt.imshow(thresh_otzu_blurred,cmap="Greys_r")

plt.show()


