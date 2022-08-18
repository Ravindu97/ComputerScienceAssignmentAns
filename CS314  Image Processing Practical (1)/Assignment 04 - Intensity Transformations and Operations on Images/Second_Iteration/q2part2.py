import cv2
import numpy as np
import matplotlib.pyplot as plt


def globalThresholdTrial(image , T):

    ret,thresh1 = cv2.threshold(image,T,255,cv2.THRESH_BINARY)
    ret,thresh2 = cv2.threshold(image,T,255,cv2.THRESH_BINARY_INV)
    ret,thresh3 = cv2.threshold(image,T,255,cv2.THRESH_TRUNC)
    ret,thresh4 = cv2.threshold(image,T,255,cv2.THRESH_TOZERO)
    ret,thresh5 = cv2.threshold(image,T,255,cv2.THRESH_TOZERO_INV)

    labels = ["Original","THRESH_BINARY","THRESH_BINARY_INV","THRESH_TRUNC","THRESH_TOZERO","THRESH_TOZERO_INV"]
    images = [image,thresh1,thresh2,thresh3,thresh4,thresh5]

    for i in range(6):
        plt.subplot(2,3,i+1)
        plt.title(labels[i],fontsize=7)
        plt.xticks([])
        plt.yticks([])
        plt.imshow(images[i],cmap='Greys_r')

    plt.show()


img = cv2.imread(r'numbers.jpg', cv2.IMREAD_GRAYSCALE)

globalThresholdTrial(img,100)

thresholdTrialValues = [100,80,60,40,20,10,5]


for i in range(len(thresholdTrialValues)):
    globalThresholdTrial(img,thresholdTrialValues[i])
